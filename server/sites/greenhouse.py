from time import sleep
from utils import field_match, find_fields_by_label, handle_input_field, handle_select_child_options
from selenium.webdriver.common.by import By

def handle_greenhouse_autocomplete(driver, data, field_name):

    def handle_input(input, user_data):
        input.send_keys(user_data)
        sleep(1.5)
        drop_element = driver.find_element(By.ID, "selectedOption")
        drop_element.click()

    autocomplete_fields = driver.find_elements(By.XPATH, '//div[@class="select2-search"]')

    for field in autocomplete_fields:
        try:
            # Handle Autocomplete Fields
            if "School" in field_name:
                handle_input(field.find_element(By.TAG_NAME, "input"), data['user']['school'])
            if "Are you 18" in field_name:
                handle_input(field.find_element(By.TAG_NAME, "input"), "Yes")
            if "authorized" in field_name:
                handle_input(field.find_element(By.TAG_NAME, "input"), data['user']['workAuthorization'])
            if "Degree" in field_name or "degree" in field_name:
                handle_input(field.find_element(By.TAG_NAME, "input"), "Associate")
            if "Discipline" in field_name:
                handle_input(field.find_element(By.TAG_NAME, "input"), "Business")
        except BaseException:
            continue

def handle_hidden_field(field_name, element, driver, data):

    # Handle Hidden Option Fields
    if "security clearance" in field_name:
        handle_select_child_options(element, data['user']['securityClearance'])
    if "willing to relocate" in field_name:
        handle_select_child_options(element, "No")
    if "race" in field_name:
        handle_select_child_options(element, data['user']['race'])
    if "authorized" in field_name or "legal right to work" in field_name:
        handle_select_child_options(element, data['user']['workAuthorization'])
    if "sponsorship" in field_name:
        handle_select_child_options(element, data['user']['immigrationSponsorship'])
    if "Disability" in field_name:
        handle_select_child_options(element, data['user']['disabilityStatus'])
    if "Veteran" in field_name:
        handle_select_child_options(element, data['user']['veteranStatus'].lower())
    if "Hispanic/Latino" in field_name:
        handle_select_child_options(element, data['user']['isHispanic'])
    if "Gender" in field_name:
        handle_select_child_options(element, data['user']['gender'])
    if "hear about this job" in field_name:
        handle_select_child_options(element, data['user']['applicationReferral'])
    if "Do you have any relatives currently employed by" in field_name:
        handle_select_child_options(element, "No")

    # Handle Hidden Input Fields
    x_path = './label/input[@type="text"]'
    if "LinkedIn" in field_name:
        handle_input_field(element, data['user']['linkedin'], x_path)
        sleep(1.5)
    if "Github" in field_name:
        handle_select_child_options(element, data['user']['portfolio'])
        sleep(1.5)
    if "Wesbite" in field_name:
        handle_input_field(element, data['user']['website'], x_path)
        sleep(1.5)
    if "country of residence" in field_name:
        handle_input_field(element, data['user']['country'], x_path)
    if "hear about this job" in field_name:
        handle_input_field(element, "LinkedIn", x_path)
    if "salary" in field_name:
        handle_input_field(element, data['user']['salary'], x_path)
    if "require" in field_name and "immigration" in field_name:
        btns = driver.find_elements(By.CLASS_NAME, "application-answer-alternative")
        for btn in btns:
            if field_match(btn.get_attribute('textContent'), data=data['user']['immigrationSponsorship']):
                btn.click()

def handle_greenhouse(driver, data):

    # Get Fields
    dropdowns = driver.find_elements(By.CLASS_NAME, "field")
    input_fields = find_fields_by_label(driver=driver)

    for input in input_fields:
        if "First" in input['label']:
            if input['element'].get_attribute('value') == "":
                input['element'].send_keys(data['user']['firstName'])
        if "Last" in input['label']:
            if input['element'].get_attribute('value') == "":
                input['element'].send_keys(data['user']['lastName'])
        if "Email" in input['label']:
            if input['element'].get_attribute('value') == "":
                input['element'].send_keys(data['user']['email'])
        if "Phone" in input['label']:
            if input['element'].get_attribute('value') == "":
                input['element'].send_keys(data['user']['phoneNumber'])
    
    for element in dropdowns:
        try:
            element.click()
            field_name = element.find_element(By.XPATH, "./label").get_attribute('innerText')

            if "School" or "Degree" or "Discipline" in field_name:
                handle_greenhouse_autocomplete(driver, data, field_name)
                sleep(1)
            
            handle_hidden_field(field_name, element, driver, data)

        except BaseException as err:
            print(err)
            continue