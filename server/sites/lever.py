from datetime import datetime
from utils import handle_input_field, handle_select_child_options
from selenium.webdriver.common.by import By


def handle_lever_fields(field_name, element, data):
    # Handle Inputs
    x_path = './label/div/input'
    if "City" in field_name:
        handle_input_field(element,data['user']['city'], x_path)
    if "Your name" in field_name:
        handle_input_field(element, f"{data['user']['firstName']} {data['user']['lastName']}", x_path)
    if "Today's date" in field_name:
        handle_input_field(element, datetime.today().strftime('%m/%d/%Y'), x_path)
    if "annual compensation" in field_name or "looking to start" in field_name or "salary" in field_name:
        handle_input_field(element, 'Open', x_path)

    # Handle Selects
    if "Country" in field_name:
        handle_select_child_options(element, data['user']['country'])
    if "job posting" in field_name:
        handle_select_child_options(element, "linkedin")
    if "State" in field_name:
        handle_select_child_options(element, data['user']['state'])


def handle_lever(driver, data):
    elements = driver.find_elements(By.CLASS_NAME, "application-question")

    elements += driver.find_elements(By.CLASS_NAME, "custom-question")

    elements += driver.find_elements(By.CLASS_NAME, "application-dropdown")

    elements += driver.find_elements(By.CLASS_NAME, "application-additional")

    for element in elements:
        try:
            field_name =  element.find_element(By.XPATH, "./label").get_attribute('innerText')
            handle_lever_fields(field_name, element, data)

        except BaseException:
            continue