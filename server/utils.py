from datetime import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

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


def handle_hidden_fields(driver, field_name, data):
    dropdowns = driver.find_elements(By.CLASS_NAME, field_name)
    for element in dropdowns:
        try:
            element.click()
            field_name = element.get_attribute('innerText')

            options = []


            if field_name == "field":
                options = driver.find_elements(
                    By.CLASS_NAME, "select2-result-label")
            elif field_name == "tr":
                options = driver.find_elements(
                    By.TAG_NAME, field_name)
            else:
                options = driver.find_elements(
                    By.TAG_NAME, "option")

            select_field(options, field_name, element, driver, data)

        except BaseException as err:
            # print(err)
            continue

        
    
