from datetime import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def match_field(field, data):
    field_arr = field.split(' ')
    data_arr = data.split(' ')

    count = 0
    for f in field_arr:
        for d in data_arr:
            if f == d:
                count += 1

    return count / len(field) >= .35

def select_field(options, field_name, element, driver, data):
    if "security clearance" in field_name:
        for option in options:
            if match_field(option.get_attribute('textContent'), data['securityClearance']):
                option.click()
                return
    if "willing to relocate" in field_name:
        for option in options:
            if "No" in option.get_attribute('textContent'):
                option.click()
                return
    if "race" in field_name:
        for option in options:
            if match_field(option.get_attribute('textContent'), data['race']):
                option.click()
                return
    if "legally authorized" in field_name:
        for option in options:
            if match_field(option.get_attribute('textContent'), data['workAuthorization']):
                option.click()
                return
    if "sponsorship" in field_name:
        for option in options:
            if match_field(option.get_attribute('textContent'), data['immigrationSponsorship']):
                option.click()
                return
    if "Disability" in field_name:
        for option in options:
            if match_field(option.get_attribute('textContent'), data['disabilityStatus']):
                option.click()
                return
    if "Veteran" in field_name:
        for option in options:
            if match_field(option.get_attribute('textContent'), data['veteranStatus']):
                option.click()
                return
    if "Hispanic/Latino" in field_name:
        for option in options:
            if match_field(option.get_attribute('textContent'), data['isHispanic']):
                option.click()
                return
    if "Gender" in field_name:
        for option in options:
            if match_field(option.get_attribute('textContent'), data['gender']):
                option.click()
                return
    if "Your name" in field_name:
        element.send_keys('David Alvarez')
    if "Today's date" in field_name:
        element.send_keys(datetime.today().strftime('%m/%d/%Y'))
    if "annual compensation" in field_name:
        element.send_keys('Open')
    if "looking to start" in field_name:
        element.send_keys('Open')
    if "require" in field_name and "immigration" in field_name:
        btns = driver.find_elements(By.CLASS_NAME, "application-answer-alternative")
        for btn in btns:
            print(btn.get_attribute('textContent'))
            if "No." in btn.get_attribute('textContent'):
                btn.click()


def handle_hidden_fields(driver, class_name, data):
    dropdowns = driver.find_elements(By.CLASS_NAME, class_name)
    for element in dropdowns:
        try:
            element.click()
            field_name = element.get_attribute('innerText')

            options = []

            if class_name == "field":
                options = driver.find_elements(
                    By.CLASS_NAME, "select2-result-label")
            else:
                options = driver.find_elements(
                    By.TAG_NAME, "option")

            select_field(options, field_name, element, driver, data)

        except BaseException as err:
            print(err)

        
    
