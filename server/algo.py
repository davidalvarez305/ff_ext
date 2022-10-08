import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.webdriver.remote.webelement import WebElement

from list import COMMON_QUESTIONS


def has_children(element: WebElement):
    return len(element.find_elements(By.XPATH, ".//*")) > 0


def child_nodes(element: WebElement):
    return element.find_elements(By.XPATH, ".//*")


def is_label(element: WebElement):
    try:
        return element.get_attribute('tagName') == 'LABEL'
    except AttributeError:
        pass


def recurse(element: WebElement):
    if has_children(element) and not is_label(element):
        nodes = child_nodes(element)
        for node in nodes:
            recurse(node)
    else:
        return element


def find_form_fields(driver):
    # Handle iFrame
    form_elements = []

    tag_names = ['label', 'select', 'input', 'button', 'textarea']

    for tag in tag_names:
        form_elements += driver.find_elements(By.TAG_NAME, tag)

    labels = []
    for element in form_elements:
        el = recurse(element)
        if is_label(el):
            labels.append(el)
    return labels


def traverse_dom(driver):
    labels = find_form_fields(driver)

    fields = []

    # Append fields by label.
    for label in labels:
        field = {}

        html_for = label.get_attribute('for')
        if html_for:
            try:

                field['label'] = label.get_attribute('innerText')
                field['id'] = label.get_attribute('for')

                # Element
                input_field = driver.find_element(By.ID, field['id'])
                field['tagName'] = input_field.get_attribute('tagName')
                field['element'] = input_field

                fields.append(field)

            except BaseException:
                continue

    for field in fields:
        print('label: ', field['label'])
        try:
            # Handle Resume Upload
            if field['tagName'] == 'BUTTON':
                resume_fields = [
                    field['label'],
                    field['element'].get_attribute('textContent'),
                    field['element'].get_attribute('id'),
                    field['element'].get_attribute('name'),
                    field['element'].get_attribute('class')
                ]
                if "resume" in resume_fields:
                    field['element'].send_keys(str(os.environ.get('RESUME_PATH')))
                if "cover" in resume_fields:
                    field['element'].send_keys(str(os.environ.get('COVER_PATH')))

            # Handle Select Buttons
            elif field['tagName'] == 'SELECT':
                for question in COMMON_QUESTIONS:
                    if question['question'].lower() in field['label'].lower():
                        field['element'].click()

                        options = field['element'].find_elements(By.TAG_NAME, 'option')

                        for option in options:
                            if option.get_attribute('textContent').lower() == question['data']:
                                option.click()

            # Handle Checkboxes & Radio Buttons
            elif field['tagName'] == 'INPUT' and field['element'].get_attribute('type') in ['checkbox', 'radio']:
                for question in COMMON_QUESTIONS:
                    if question['question'].lower() in field['label'].lower():
                        field['element'].click()

            # Handle Normal Inputs
            else:
                for question in COMMON_QUESTIONS:
                    if question['question'].lower() in field['label'].lower():
                        field['element'].send_keys(question['data'])
        except BaseException as err:
            print("Error: ", err)
            continue

    input("Handle next step & hit enter: ")


def dfs():
    load_dotenv()
    options = Options()
    user_agent = str(os.environ.get('USER_AGENT'))
    # options.add_argument("--headless")
    options.add_experimental_option("detach", True)
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    URL = 'https://accelbyte.bamboohr.com/jobs/view.php?id=285'
    driver.get(URL)

    while (True):
        try:
            traverse_dom(driver)
        except NoSuchElementException as err:
            print("Error: ", err)
            input("Handle case & hit enter: ")


dfs()
