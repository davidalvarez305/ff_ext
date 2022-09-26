from selenium.webdriver.common.by import By


def handle_hidden_fields(driver, class_name, select_class_name):
    dropdowns = driver.find_elements(By.CLASS_NAME, class_name)
    for dp in dropdowns:
        try:
            dp.click()
            field_name = dp.get_attribute('textContent')

            options = []

            if len(select_class_name) > 0:
                options = driver.find_elements(
                    By.CLASS_NAME, select_class_name)
            else:
                options = driver.find_elements(
                    By.TAG_NAME, "option")

            for option in options:
                if "citizen" in field_name:
                    if "Yes" in option.get_attribute('textContent'):
                        option.click()
                if "relocate" in field_name:
                    if "No" in option.get_attribute('textContent'):
                        option.click()
                if "race" in field_name:
                    if "Hispanic or Latino" == option.get_attribute('textContent'):
                        option.click()
                if "legally authorized" in field_name:
                    if "Yes" in option.get_attribute('textContent'):
                        option.click()
                if "sponsorship" in field_name:
                    if "No" in option.get_attribute('textContent'):
                        option.click()
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
            print("Hidden field")
