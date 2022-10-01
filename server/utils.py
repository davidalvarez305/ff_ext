from datetime import datetime
from time import sleep
from selenium.webdriver.common.by import By

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
            if f == d:
                count += 1
    return count / len(option_arr) >= .35

def handle_select_child_options(element, user_data):
    options = element.find_elements(By.XPATH, '//li[@role="option"]')
    for option in options:
        if field_match(option=option.get_attribute('textContent'), data=user_data):
            option.click()
            return

def handle_autocomplete(driver, user_data, input_class):
    input = driver.find_element(By.ID, input_class)
    input.send_keys(user_data)
    sleep(1.5)
    drop_element = driver.find_element(By.ID, "selectedOption")
    drop_element.click()


def handle_hidden_field(field_name, element, driver, data):

    # Handle Autocomplete Fields
    if "School" in field_name:
        handle_autocomplete(driver, data['user']['school'], "s2id_autogen7_search")
    if "Degree" in field_name:
        handle_autocomplete(driver, "Associate", "s2id_autogen8_search")
    if "Discipline" in field_name:
        handle_autocomplete(driver, "Business", "s2id_autogen9_search")
    
    # Handle Hidden Fields
    if "security clearance" in field_name:
        handle_select_child_options(element, data['user']['securityClearance'])
    if "willing to relocate" in field_name:
        handle_select_child_options(element, "No")
    if "race" in field_name:
        handle_select_child_options(element, data['user']['race'])
    if "legally authorized" in field_name:
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

    # Handle Hidden Input Fields
    if "LinkedIn" in field_name:
        element.send_keys(data['user']['linkedin'])
    if "Wesbite" in field_name:
        element.send_keys(data['user']['website'])
    if "Your name" in field_name:
        element.send_keys(f"{data['user']['firstName']} {data['user']['lastName']}")
    if "Today's date" in field_name:
        element.send_keys(datetime.today().strftime('%m/%d/%Y'))
    if "annual compensation" in field_name:
        element.send_keys('Open')
    if "looking to start" in field_name:
        element.send_keys('Open')
    if "require" in field_name and "immigration" in field_name:
        btns = driver.find_elements(By.CLASS_NAME, "application-answer-alternative")
        for btn in btns:
            if field_match(btn.get_attribute('textContent'), data=data['user']['immigrationSponsorship']):
                btn.click()

def handle_greenhouse(driver, data):
    dropdowns = driver.find_elements(By.CLASS_NAME, "field")
    for element in dropdowns:
        try:
            element.click()
            field_name = element.find_element(By.XPATH, "./label").get_attribute('textContent')
            if "School" or "Degree" or "Discipline" in field_name:
                sleep(1)

            handle_hidden_field(field_name, element, driver, data)

        except BaseException as err:
            # print(err)
            continue

def handle_lever(driver, data):
    dropdowns = driver.find_elements(By.CLASS_NAME, "application-question")
    for element in dropdowns:
        try:
            element.click()
            field_name = element.get_attribute('innerText')

            options = driver.find_elements(
                    By.TAG_NAME, "input")

            handle_hidden_field(options, field_name, element, driver, data)

        except BaseException as err:
            # print(err)
            continue

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