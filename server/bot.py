import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from wd import handle_workdayjobs
from utils import click_preapplication_button, handle_bamboo, handle_greenhouse, handle_lever, handle_smartrecruiters, handle_underdog_fields, upload_smartrecruiters_resume


def get_data(el):
    if el['data'] == 'resume':
        return os.environ.get('RESUME_PATH')
    elif el['data'] == 'cover':
        return os.environ.get('COVER_PATH')
    else:
        return el['data']

def execute(data):
    options = Options()
    user_agent = str(os.environ.get('USER_AGENT'))
    # options.add_argument("--headless")
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Firefox()

    driver.get(data['url'])

    sleep(5)

    if "workdayjobs" in data['url']:
        handle_workdayjobs(driver, data)
        return

    if "bamboohr" in data['url']:
        click_preapplication_button(driver)

    if "smartrecruiters" in data['url']:
        upload_smartrecruiters_resume(driver=driver)

    for el in data['results']:
        try:
            if el['field'] == 'name':
                name = driver.find_element(By.NAME, el['name'])
                if name.get_attribute('value') == "":
                    name.send_keys(get_data(el))
            if el['field'] == 'id':
                name = driver.find_element(By.ID, el['name'])
                if name.get_attribute('value') == "":
                    name.send_keys(get_data(el))
            if el['field'] == 'className':
                name = driver.find_element(By.CLASS_NAME, el['name'])
                if name.get_attribute('value') == "":
                    name.send_keys(get_data(el))
        except BaseException as error:
            # print(f"Error: {error}. Element: {el}")
            continue

        # handle ashbyhq.com
        # handle adp.com

    try:
        if "smartrecruiters" in data['url']:
            handle_smartrecruiters(driver=driver, data=data)
        if "bamboohr" in data['url']:
            handle_bamboo(driver=driver, data=data)
        if "greenhouse" in data['url']:
            handle_greenhouse(driver=driver, data=data)
        if "lever" in data['url']:
            handle_lever(driver=driver, data=data)
        elif "underdog.io" in data['url']:
            handle_underdog_fields(driver=driver, data=data)
    except BaseException as error:
        print(f"Error: {error}. Element: {el}")
        pass
