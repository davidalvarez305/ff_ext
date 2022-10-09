import os
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

from helpers.sheets import get_values

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
    labels = driver.find_elements(By.TAG_NAME, 'label')

    fields = []

    # Append fields by label.
    for label in labels:
        field = {}

        html_for = label.get_attribute('for')
        if html_for:
            try:

                field['label'] = label.get_attribute('innerText')
                field['id'] = label.get_attribute('for')

                input_field = driver.find_element(By.ID, field['id'])
                field['tagName'] = input_field.get_attribute('tagName')
                field['element'] = input_field

                fields.append(field)

            except BaseException:
                continue

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
                        field['element'].click()

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
