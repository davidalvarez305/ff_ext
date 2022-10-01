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

def select_field(options, field_name, element, driver, data):
    if "Degree" in field_name:
        select_opts = element.find_elements(By.XPATH, "./*")
        for option in select_opts:
            print(option.get_attribute('textContent'))
            if field_match(option=option.get_attribute('textContent'), data=data['user']['degree']):
                option.click()
                return
    if "School" in field_name:

        # I need to improve how this backend works. First, I need to get all of the input and select fields.
        # If input field, send keys. If select field, find all options, and then click the one.
        # Right now, I am traversing through every element in the form and clicking it, which is unnecessary for some forms.
        # Separate the forms, and do this more cleanly.

        els = element.find_elements(By.XPATH, "./*")
        for el in els:
            if "INPUT" in el.get_attribute('tagName'):
                print(el.get_attribute('outerHTML'))
                el.click()
                el.send_keys(data['user']['school'])
                print(el.get_attribute('value'))
                sleep(1.5)
                auto_complete(driver, "span")

    if "security clearance" in field_name:
        for option in options:
            if field_match(option=option.get_attribute('textContent'), data=data['user']['securityClearance']):
                option.click()
                return
    if "willing to relocate" in field_name:
        for option in options:
            if "No" in option.get_attribute('textContent'):
                option.click()
                return
    if "race" in field_name:
        for option in options:
            if field_match(option=option.get_attribute('textContent'), data=data['user']['race']):
                option.click()
                return
    if "legally authorized" in field_name:
        for option in options:
            if field_match(option=option.get_attribute('textContent'), data=data['user']['workAuthorization']):
                option.click()
                return
    if "sponsorship" in field_name:
        for option in options:
            if field_match(option=option.get_attribute('textContent'), data=data['user']['immigrationSponsorship']):
                option.click()
                return
    if "Disability" in field_name:
        for option in options:
            if field_match(option=option.get_attribute('textContent'), data=data['user']['disabilityStatus']):
                option.click()
                return
    if "Veteran" in field_name:
        for option in options:
            if field_match(option=option.get_attribute('textContent'), data=data['user']['veteranStatus']):
                option.click()
                return
    if "Hispanic/Latino" in field_name:
        for option in options:
            if field_match(option=option.get_attribute('textContent'), data=data['user']['isHispanic']):
                option.click()
                return
    if "Gender" in field_name:
        for option in options:
            if field_match(option=option.get_attribute('textContent'), data=data['user']['gender']):
                option.click()
                return
    if "Your name" in field_name:
        element.send_keys(f"{data['firstName']} {data['lastName']}")
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
            field_name = element.get_attribute('innerText')

            options = driver.find_elements(
                    By.CLASS_NAME, "select2-result-label")

            select_field(options, field_name, element, driver, data)

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

            select_field(options, field_name, element, driver, data)

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