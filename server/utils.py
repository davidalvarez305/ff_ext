from datetime import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

def select_field(options, field_name, element):
    if "security clearance" in field_name:
        for option in options:
            if "Yes" in option.get_attribute('textContent'):
                option.click()
                return
    if "willing to relocate" in field_name:
        for option in options:
            if "No" in option.get_attribute('textContent'):
                option.click()
                return
    if "race" in field_name:
        for option in options:
            if "Hispanic or Latino" in option.get_attribute('textContent'):
                option.click()
                return
    if "legally authorized" in field_name:
        for option in options:
            if "Yes" in option.get_attribute('textContent'):
                option.click()
                return
    if "sponsorship" in field_name:
        for option in options:
            if "No" in option.get_attribute('textContent'):
                option.click()
                return
    if "Disability" in field_name:
        for option in options:
            if "No, " in option.get_attribute('textContent'):
                option.click()
                return
    if "Veteran" in field_name:
        for option in options:
            if "I am not" in option.get_attribute('textContent'):
                option.click()
                return
    if "Hispanic/Latino" in field_name:
        for option in options:
            if "Yes" in option.get_attribute('textContent'):
                option.click()
                return
    if "Gender" in field_name:
        for option in options:
            if "Male" in option.get_attribute('textContent'):
                option.click()
                return
    if "Your name" in field_name:
        element.send_keys('David Alvarez')
    if "Today's date" in field_name:
        element.send_keys(datetime.today().strftime('%m/%d/%Y'))


def handle_hidden_fields(driver, class_name):
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

            select_field(options, field_name, element)

        except BaseException as err:
            print(err)

        
    
