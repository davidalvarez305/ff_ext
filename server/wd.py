from lib2to3.pytree import Base
import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from list import NO_APPLICATION_QUESTIONS, YES_APPLICATION_QUESTIONS
URL = 'https://capitalone.wd1.myworkdayjobs.com/Capital_One/login?redirect=%2FCapital_One%2Fjob%2FRichmond-VA%2FSenior-Software-Engineer--Full-Stack-Remote-Eligible_R156218-1%2Fapply%3Futm_campaign%3Denterprise_tech_2022%26utm_medium%3Djobad%26utm_content%3Dpj_board%26utm_source%3Dlinkedin%2520slotted%26p_uid%3D5uCFnQkcK0%26source%3Drd_linkedin_job_posting_tm%26p_sid%3DVpVix0b%26ss%3Dpaid%26dclid%3DCMKRnqaOwvoCFQHihwodcgsCbw'


def click_hidden_button(driver, btn_xpath):
    submit_button = driver.find_element(By.XPATH, btn_xpath)
    actions = ActionChains(driver=driver)
    actions.move_to_element(submit_button).click().perform()


def enter_login(driver, btn_xpath):
    form = driver.find_element(By.TAG_NAME, 'form')

    elements = form.find_elements(By.XPATH, './*')

    for element in elements:
        try:
            label = element.find_element(
                By.TAG_NAME, "label").get_attribute('innerText')
            input = element.find_element(By.TAG_NAME, 'input')

            if "Email" in label:
                input.send_keys(os.environ.get('EMAIL'))

            if "Password" in label:
                input.send_keys(os.environ.get('PASSWORD'))

        except BaseException:
            continue

    click_hidden_button(driver, btn_xpath)


def select_options(driver, attr, input_id):
    try:

        if "Fluent" in attr:

            btn_xpath = f'//button[@id="{input_id}"]'
            click_hidden_button(driver, btn_xpath)

            elements = driver.find_elements(By.TAG_NAME, 'li')
            for el in elements:
                if attr in el.get_attribute('textContent'):
                    el.click()
                    break
        else:
            element = driver.find_element(By.ID, input_id)
            element.click()

            elements = driver.find_elements(By.TAG_NAME, 'li')
            for el in elements:
                if attr in el.get_attribute('textContent'):
                    el.click()
                    break
    except BaseException as err:
        print(err)


def handle_multiple_input(input, skills):
    for skill in skills:
        input.send_keys(skill)
        input.send_keys(Keys.RETURN)
        sleep(0.5)


def handle_inputs(driver):
    elements = driver.find_elements(By.TAG_NAME, 'input')
    elements += driver.find_elements(By.TAG_NAME, 'button')

    for el in elements:
        try:
            if el.get_attribute('tagName') == "INPUT":
                input_id = el.get_attribute('id')
                if len(input_id) > 0:
                    label = driver.find_element(
                        By.XPATH, f'//label[@for="{input_id}"]').get_attribute('innerText')

                    if "First Name" in label:
                        el.send_keys('David')
                    if "Last Name" in label:
                        el.send_keys('Alvarez')
                    if label == "Name":
                        el.send_keys('David Alvarez')
                    if "Address Line 1" in label:
                        el.send_keys('MY STREET ADDRESS')
                    if "City" in label:
                        el.send_keys('MY CITI')
                    if "Postal Code" in label:
                        el.send_keys('MY ZIP CODE')
                    if "Phone Number" in label:
                        el.send_keys('MY NUMBER')
                    if "Job Title" in label:
                        el.send_keys(os.environ.get('TITLE'))
                    if "Company" in label:
                        el.send_keys('CURRENT COMPANY')
                    if "Location" in label:
                        el.send_keys(os.environ.get('COMPANY_LOCATION'))
                    if "currently working here" in label or "No, I Don't Have A Disability" in label:
                        el.click()
                    if "fluent in this language" in label or "terms and conditions" in label:
                        el.click()
                    if "Role Description" in label:
                        el.send_keys(os.environ.get('JOB_DESCRIPTION'))
                    if "School or University" in label:
                        el.send_keys('MY UNI')
                    if "Field of Study" in label:
                        handle_multiple_input(el, ['Marketing', 'Advertising'])
                    if "Skills" in label:
                        handle_multiple_input(el, ['Javascript', 'Python', 'Go', 'AWS', 'GCP',
                                              'Docker', 'Linux', 'Nginx', "SQL", "GraphQL", 'Postgres', 'MongoDB'])

            if el.get_attribute('tagName') == "BUTTON":
                input_id = el.get_attribute('id')
                if len(input_id) > 0 and "input" in input_id:
                    label = driver.find_element(
                        By.XPATH, f'//label[@for="{input_id}"]').get_attribute('innerText')
                    if "State" in label:
                        select_options(
                            driver=driver, input_id=input_id, attr="Florida")
                    if "Phone Device Type" in label:
                        select_options(
                            driver=driver, input_id=input_id, attr="Mobile")
                    if "Degree" in label:
                        select_options(driver=driver, input_id=input_id,
                                       attr="Associate")
                    if "Veteran" in label:
                        select_options(driver=driver, input_id=input_id,
                                       attr="No")
                    if "Gender" in label:
                        select_options(driver=driver, input_id=input_id,
                                       attr="Male")
                    if "Race" in label:
                        select_options(driver=driver, input_id=input_id,
                                       attr="Hispanic")
                    if "Language" in label:
                        select_options(driver=driver, input_id=input_id,
                                       attr="English")
                    if "Reading" in label or "Speaking" in label or "Assessment" in label or "Writing" in label:
                        el.send_keys(Keys.ARROW_DOWN)
                        select_options(driver=driver, input_id=input_id,
                                       attr="Fluent")
                    if any(sub_str in label for sub_str in YES_APPLICATION_QUESTIONS):
                        select_options(driver=driver, input_id=input_id,
                                       attr="Yes")
                    if any(sub_str in label for sub_str in NO_APPLICATION_QUESTIONS):
                        select_options(driver=driver, input_id=input_id,
                                       attr="No")
        except BaseException:
            continue


def get_correct_year(driver):
    try:
        year = driver.find_element(
            By.XPATH, '//*[@data-automation-id="monthPickerSpinnerLabel"]').get_attribute('innerText')
        while int(os.environ.get('JOB_START_YEAR')) < int(year):
            driver.find_element(
                By.XPATH, '//*[@aria-label="Previous Year"]').click()
            current_year = driver.find_element(
                By.XPATH, '//*[@data-automation-id="monthPickerSpinnerLabel"]').get_attribute('innerText')
            year = current_year
    except BaseException as err:
        print(err)


def click_save_and_continue(driver):
    driver.find_element(
        By.XPATH, '//button[@data-automation-id="bottom-navigation-next-button"]').click()
    sleep(3)


def main():
    load_dotenv()
    options = Options()
    user_agent = str(os.environ.get('USER_AGENT'))
    # options.add_argument("--headless")
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Firefox()

    driver.get(URL)

    WebDriverWait(driver, timeout=10).until(
        lambda d: d.find_element(By.TAG_NAME, "html"))
    sleep(2)

    # Navigate to Create Account
    # enter_login(driver, '//button[@data-automation-id="createAccountSubmitButton"]')
    # input("Verify email and come back: ")

    # Submit & Verify Email -- Then Login
    enter_login(driver, '//button[@data-automation-id="signInSubmitButton"]')
    sleep(5)

    # Apply Manually
    # click_hidden_button(driver, '//button[@data-automation-id="applyManually"]')

    # Enter Fields
    # handle_inputs(driver)

    # Save & Continue
    click_save_and_continue(driver)

    # Add Work Experience
    """     driver.find_element(
            By.XPATH, '//button[@aria-label="Add Work Experience"]').click()

        # Click "I Currently Work Here"
        driver.find_element(
            By.XPATH, '//input[@data-automation-id="currentlyWorkHere"]').click()

        # Click Calendar for Dates & Handle Dates
        driver.find_element(
            By.XPATH, '//*[@data-automation-id="dateIcon"]').click()
        get_correct_year(driver)

        months = driver.find_elements(By.TAG_NAME, 'li')

        for month in months:
            if month.get_attribute('innerText') == "Nov":
                month.click()
                break

        # Add Education
        driver.find_element(
            By.XPATH, '//button[@aria-label="Add Education"]').click()

        # Upload Resume
        driver.find_element(
            By.XPATH, '//input[@data-automation-id="file-upload-input-ref"]').send_keys(os.environ.get('RESUME_PATH'))

        # Add Websites
        driver.find_element(
            By.XPATH, '//button[@aria-label="Add Websites"]').click()
        driver.find_element(
            By.XPATH, '//input[@data-automation-id="website"]').send_keys('https://github.com/davidalvarez305')

        # Add LinkedIn
        driver.find_element(
            By.XPATH, '//input[@data-automation-id="linkedinQuestion"]').send_keys(os.environ.get('LINKED_URL'))

        # Add Languages
        driver.find_element(
            By.XPATH, '//button[@aria-label="Add Languages"]').click()

        handle_inputs(driver) """

    # Save & Continue
    click_save_and_continue(driver)

    # Handle Application Questions
    # handle_inputs(driver)

    # Save & Continue
    click_save_and_continue(driver)

    # Handle Voluntary Disclosures
    # handle_inputs(driver)
    input("Hold it partner: ")

    # Save & Continue
    click_save_and_continue(driver)

    # Handle Self-Identify
    handle_inputs(driver)

    # Select Today's Date
    driver.find_element(
        By.XPATH, '//*[@data-automation-id="dateIcon"]').click()
    driver.find_element(By.XPATH, '//*[@aria-selected="true"]').click()

    # Save & Continue
    click_save_and_continue(driver)


main()