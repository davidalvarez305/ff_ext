import os
from time import sleep
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from helpers.sheets import get_values
from utils import find_fields_by_label

def get_element(element, values):
    attributes = ['id', 'name', 'class']
    for attr in attributes:
        attribute = element.get_attribute(attr)
        for question in values:
            try:
                if attribute and attribute.lower() in question['question']:
                    field = {}

                    field['label'] = question['question'][0]
                    field[attr] = attribute

                    field['tagName'] = element.get_attribute('tagName')
                    field['element'] = element
                    return field
            except BaseException:
                continue

def find_form_fields(driver, values):
    form_elements = []
    fields = []

    tag_names = ['select', 'input', 'button', 'textarea']

    for tag in tag_names:
        form_elements += driver.find_elements(By.TAG_NAME, tag)

    for element in form_elements:
        field = get_element(element, values)
        if field:
            fields.append(field)

    return fields

def handle_fields(driver, values):

    # Find Fields by Form Label
    fields = find_fields_by_label(driver)

    # Append Form Fields
    form_fields = find_form_fields(driver, values)
    fields += form_fields

    for field in fields:
        try:
            # Handle Resume Upload
            if field['tagName'] == 'BUTTON':
                resume_fields = [
                    field['label'],
                    field['element'].get_attribute('textContent'),
                    field['element'].get_attribute('innerText'),
                    field['element'].get_attribute('innerHTML'),
                    field['element'].get_attribute('id'),
                    field['element'].get_attribute('name'),
                    field['element'].get_attribute('class')
                ]
                if "resume" in resume_fields:
                        if field['element'].get_attribute('value') == "":
                            field['element'].send_keys(str(os.environ.get('RESUME_PATH')))
                if "cover" in resume_fields:
                    if field['element'].get_attribute('value') == "":
                        field['element'].send_keys(str(os.environ.get('COVER_PATH')))

            # Handle Select Buttons
            elif field['tagName'] == 'SELECT':
                for question in values:
                    if any(substr in field['label'].lower() for substr in question['question']):
                        if field['element'].get_attribute('value') == "":
                            field['element'].click()
                            sleep(1)

                        options = field['element'].find_elements(By.TAG_NAME, 'option')
                        for option in options:
                            if option.get_attribute('textContent').lower() == question['data']:
                                option.click()

            # Handle Checkboxes & Radio Buttons
            elif field['tagName'] == 'INPUT' and field['element'].get_attribute('type') in ['checkbox', 'radio']:
                for question in values:
                    if any(substr in field['label'].lower() for substr in question['question']):
                        if field['element'].get_attribute('value') == False:
                            field['element'].click()

            # Handle Normal Inputs
            else:
                for question in values:
                    if any(substr in field['label'].lower() for substr in question['question']):
                        if field['element'].get_attribute('value') == "":
                            field['element'].send_keys(question['data'])
        except BaseException:
            continue

    input("Handle next step & hit enter: ")


def enter_fields(driver):

    rows = get_values(os.environ.get('SHEETS_ID'), f"{os.environ.get('TAB_NAME')}!A2:E")
    values = []

    for row in rows:
        values.append({ "data": row[0], "question": row[1:] })

    while (True):
        try:
            handle_fields(driver, values)
        except NoSuchElementException:
            input("Handle case & hit enter: ")
