import os
from time import sleep
from selenium.webdriver.common.by import By
from list import COMMON_QUESTIONS
from selenium.webdriver.common.keys import Keys

def find_fields_by_label(driver):
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
    
    return fields

def click_preapplication_button(driver):
    button = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/button")
    button.click()

def auto_complete(driver, tag):
    hidden_input = driver.find_element(By.TAG_NAME, tag)
    hidden_input.click()

def handle_underdog(options, data, driver):
    select_fields = driver.find_elements(By.TAG_NAME, "select")

    def select_option(selection):
        options = driver.find_elements(By.TAG_NAME, "option")
        for option in options:
            option_name = option.get_attribute('textContent')
            if option_name == selection:
                option.click()

    for select_field in select_fields:
        select_field.click()
        field_name = select_field.get_attribute('name')
        if "location" in field_name.lower():
            select_option("Remote")
        if "search_status" in field_name.lower():
            select_option("Actively interviewing")
        if "technical" in field_name.lower():
            select_option("Technical")
        if "experience_level" in field_name.lower():
            select_option("1-2 years")
        if "visa_toggle" in field_name.lower():
            select_option("I am a U.S. citizen or a lawful permanent resident")

    hidden_inputs = driver.find_elements(By.CLASS_NAME, "autocomplete__input")

    for input in hidden_inputs:
        input_name = input.find_element(By.XPATH, ".//ancestor::label").get_attribute('textContent')
        try:
            if "Current location" in input_name:
                input.send_keys("Hialeah, FL, USA")
                input.click()
                sleep(1.5)
                auto_complete(driver, "li")
            if "Location preference" in input_name:
                input.send_keys("Remote")
                input.click()
                auto_complete(driver, "li")
            if "Skills" in input_name:
                input.send_keys("Python, Javascript, SQL, Go, Docker, AWS, Linux, Google Cloud Platform")
                input.click()
                auto_complete(driver, "li")
            if "Job type preference(s)" in input_name:
                input.send_keys("I want a full")
                input.click()
                auto_complete(driver, "li")
        except BaseException as err:
            print(err)

    for element in options:
        if element.get_attribute('value') == "":
            field_name = element.get_attribute('name')
            if "first" in field_name.lower():
                element.send_keys(data['user']['firstName'])
            if "last" in field_name.lower():
                element.send_keys(data['user']['lastName'])
            if "email" in field_name.lower():
                element.send_keys(data['user']['email'])
            if "website" in field_name.lower():
                element.send_keys(data['user']['linkedIn'])
            if "github" in field_name.lower() or "portfolio" in field_name.lower():
                element.send_keys(data['user']['portfolio'])

def field_match(option, data):
    if option == data or data in option:
        return True

    option_arr = option.split(' ')
    data_arr = data.split(' ')

    count = 0
    for f in option_arr:
        for d in data_arr:
            if f.lower() == d.lower():
                count += 1
    return count / len(option_arr) >= .35

def handle_select_child_options(element, user_data):
    options = element.find_elements(By.XPATH, '//li[@role="option"]')

    if (len(options)) == 0:
        options = element.find_elements(By.TAG_NAME, 'option')

    for option in options:
        if field_match(option=option.get_attribute('innerText'), data=user_data):
            option.click()
            return
    
def handle_input_field(element, user_data, xpath):
    input = element.find_element(By.XPATH, xpath)
    if input.get_attribute('value') == "":
        input.send_keys(user_data)

def handle_underdog_fields(driver, data):
    dropdowns = driver.find_elements(By.CLASS_NAME, "div-block-37")
    for element in dropdowns:
        try:
            element.click()

            options = driver.find_elements(
                    By.TAG_NAME, "option")

            handle_underdog(options, data, driver)

        except BaseException as err:
            # print(err)
            continue

def handle_textarea(element, user_data):
    textarea = element.find_element(By.TAG_NAME, "textarea")
    if textarea.get_attribute('value') == "":
        textarea.send_keys(user_data)

def handle_select_div(driver, user_data):
    options = driver.find_elements(By.CLASS_NAME, "fab-MenuOption__row")
    for option in options:
        option_name = option.get_attribute('innerText')
        if user_data.lower() in option_name.lower():
            option.click()

def handle_bamboo(driver, data):
    elements = driver.find_elements(By.CLASS_NAME, "CandidateForm__row")

    for element in elements:
        try:
            field_name = element.find_element(By.TAG_NAME, "label").get_attribute('innerText')

            # Handle Radiobuttons
            if "Veteran" in field_name:
                btns = driver.find_elements(By.XPATH, '//*[@type="radio"]')
                for btn in btns:
                    label = btn.find_element(By.XPATH, '../label').get_attribute('innerText')
                    if data['user']['veteranStatus'].lower() in label.lower():
                        btn.click()

            # Handle Selects
            if "Gender" in field_name:
                element.click()
                handle_select_div(driver, data['user']['gender'])
            elif "Disability" in field_name:
                element.click()
                handle_select_div(driver, data['user']['disabilityStatus'])
            elif "Ethnicity" in field_name:
                element.click()
                handle_select_div(driver, data['user']['race'])

            # Handle Inputs
            else:
                for question in COMMON_QUESTIONS:
                    if question['question'].lower() in field_name.lower():
                        field = question['data']
                        handle_textarea(element, data['user'][f"{field}"])

        except BaseException as err:
            print(err)
            continue

def handle_smart_autocomplete_fields(input, user_data):
    input.send_keys(user_data)
    sleep(1)
    input.send_keys(Keys.ARROW_DOWN)
    input.send_keys(Keys.RETURN)

def handle_calendar_select(driver, user_data):
    elements = driver.find_elements(By.CLASS_NAME, 'mat-calendar-body-cell-content')
    for el in elements:
        if user_data in el.get_attribute('textContent'):
            el.click()
            return
        