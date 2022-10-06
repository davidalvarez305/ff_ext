import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
from selenium.webdriver.remote.webelement import WebElement

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
    form = driver.find_element(By.TAG_NAME, 'form')
    form_elements = form.find_elements(By.XPATH, ".//*")
    labels = []
    for element in form_elements:
        el = recurse(element)
        if is_label(el):
                labels.append(el)
    return labels

def dfs():
    load_dotenv()
    options = Options()
    user_agent = str(os.environ.get('USER_AGENT'))
    options.add_argument("--headless")
    # options.add_experimental_option("detach", True)
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    URL = 'https://boards.greenhouse.io/path/jobs/4691838004#app'
    driver.get(URL)

    while (True):
        labels = find_form_fields(driver)

        fields = []

        # Append fields by label.
        for label in labels:
            field = {}

            html_for = label.get_attribute('for')
            if html_for:

                field['label'] = label.get_attribute('innerText')
                field['id'] = label.get_attribute('for')

                # Element
                input_field = driver.find_element(By.ID, field['id'])
                field['tagName'] = input_field.get_attribute('tagName')
                field['element'] = input_field

                fields.append(field)

        # Handle case where there is no input. User responds to input until fields are available. Then re-call function.
        input("Handle case & hit enter: ")


dfs()