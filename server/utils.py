from datetime import datetime
from lib2to3.pytree import Base
import os
from time import sleep
from selenium.webdriver.common.by import By
from list import COMMON_QUESTIONS
from selenium.webdriver.common.keys import Keys

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
    
def handle_input_field(element, user_data, xpath):
    input = element.find_element(By.XPATH, xpath)
    if input.get_attribute('value') == "":
        input.send_keys(user_data)

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
    dropdowns = driver.find_elements(By.CLASS_NAME, "field")
    for element in dropdowns:
        try:
            element.click()
            field_name = element.find_element(By.XPATH, "./label").get_attribute('innerText')
            if "School" or "Degree" or "Discipline" in field_name:
                handle_greenhouse_autocomplete(driver, data, field_name)
                sleep(1)

            handle_hidden_field(field_name, element, driver, data)

        except BaseException as err:
            # print(err)
            continue

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

def upload_smartrecruiters_resume(driver):
    resume_upload = driver.find_element(By.XPATH, '//input[@class="file-upload-input"]')
    resume_upload.send_keys(os.environ.get('RESUME_PATH'))
    sleep(5)

def handle_smartrecruiters(driver, data):
    sleep(1)

    # Delete Resume Fields
    field_options = driver.find_elements(By.XPATH, '//button[@aria-label="See options"]')
    for option in field_options:
        option.click()

        # Click 'Delete Position in Dropdown & Wait for Dialogue Box to Open'
        delete_position = driver.find_element(By.XPATH, '//button[@data-test="entry-delete"]')
        delete_position.click()
        sleep(2)

        yes_button = driver.find_element(By.XPATH, '//mat-dialog-container/oc-yes-no/div/div/button[2]')
        yes_button.click()

    sections = driver.find_elements(By.CLASS_NAME, 'form-section')

    for section in sections:
        try:
            section_header = section.find_element(By.TAG_NAME, 'h3').get_attribute('innerText')
            
            if "Experience" in section_header:
                button = section.find_element(By.TAG_NAME, 'button')
                button.click()

                form_fields = section.find_elements(By.CLASS_NAME, 'form-control')

                for field in form_fields:
                    label = field.find_element(By.TAG_NAME, 'label').get_attribute('innerText')

                    if "Title" in label:
                        input = field.find_element(By.TAG_NAME, 'input')
                        handle_smart_autocomplete_fields(input, os.environ.get('TITLE'))
                    if "Company" in label:
                        input = field.find_element(By.TAG_NAME, 'input')
                        handle_smart_autocomplete_fields(input, data['user']['currentCompany'])
                    if "Office location" in label:
                        input_element = field.find_element(By.CLASS_NAME, 'sr-location-autocomplete')
                        handle_smart_autocomplete_fields(input_element, os.environ.get('COMPANY_LOCATION'))
                    if "Description" in label:
                        input_element = field.find_element(By.TAG_NAME, 'textarea')
                        handle_smart_autocomplete_fields(input_element, os.environ.get('JOB_DESCRIPTION'))
                    if "From" in label:
                        work_here = field.find_element(By.XPATH, '//*[@data-test="experience-current"]')
                        work_here.click()
                        
                        calendar_button = field.find_element(By.XPATH, '//button[@aria-label="Open calendar"]')
                        calendar_button.click()

                        # Select Year
                        handle_calendar_select(driver, os.environ.get('JOB_START_YEAR'))
                        # Select Month
                        handle_calendar_select(driver, os.environ.get('JOB_START_MONTH'))

                        # Save
                        save_button = field.find_element(By.XPATH, '//button[@data-test="experience-save"]')
                        save_button.click()

            if "Education" in section_header:
                button = section.find_element(By.TAG_NAME, 'button')
                button.click()

                form_fields = section.find_elements(By.CLASS_NAME, 'form-control')

                for field in form_fields:
                    label = field.find_element(By.TAG_NAME, 'label').get_attribute('innerText')

                    if "Institution" in label:
                        input = field.find_element(By.TAG_NAME, 'input')
                        handle_smart_autocomplete_fields(input, data['user']['school'])
                    if "Major" in label:
                        input = field.find_element(By.TAG_NAME, 'input')
                        input.send_keys(data['user']['discipline'])
                    if "Degree" in label:
                        input = field.find_element(By.TAG_NAME, 'input')
                        input.send_keys(data['user']['degree'])
                    if "School location" in label:
                        input_element = field.find_element(By.CLASS_NAME, 'sr-location-autocomplete')
                        handle_smart_autocomplete_fields(input_element, os.environ.get('SCHOOL_LOCATION'))
                    if "Description" in label:
                        input_element = field.find_element(By.TAG_NAME, 'textarea')
                        handle_smart_autocomplete_fields(input_element, os.environ.get('DEGREE_DESCRIPTION'))
                    if "From" in label:
                        work_here = field.find_element(By.XPATH, '//*[@data-test="education-current"]')
                        work_here.click()
                        
                        calendar_button = field.find_element(By.XPATH, '//button[@aria-label="Open calendar"]')
                        calendar_button.click()

                        # Select Year
                        handle_calendar_select(driver, os.environ.get('SCHOOL_START_YEAR'))
                        # Select Month
                        handle_calendar_select(driver, os.environ.get('SCHOOL_START_MONTH'))

                        # Save
                        save_button = field.find_element(By.XPATH, '//button[@data-test="education-save"]')
                        save_button.click()


        except BaseException as err:
            print(err)
            continue
        