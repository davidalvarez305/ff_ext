from selenium.webdriver.common.by import By


def handle_hidden_fields(driver):
    dropdowns = driver.find_elements(By.CLASS_NAME, "field")

    for dp in dropdowns:
        try:
            dp.click()
            field_name = dp.get_attribute('textContent')
            options = driver.find_elements(By.CLASS_NAME, "select2-result-label")
            for option in options:
                if "Disability" in field_name:
                    if "No, " in option.get_attribute('textContent'):
                        option.click()
                if "Veteran" in field_name:
                    if "I am not" in option.get_attribute('textContent'):
                        option.click()
                if "Hispanic/Latino" in field_name:
                    if "Yes" in option.get_attribute('textContent'):
                        option.click()
                if "Gender" in field_name:
                    if "Male" in option.get_attribute('textContent'):
                        option.click()
        except BaseException as err:
            print(err)
