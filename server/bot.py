import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from algo import enter_fields
from wd import handle_workdayjobs
from utils import click_preapplication_button, handle_bamboo, handle_greenhouse, handle_lever, handle_smartrecruiters, handle_underdog_fields, upload_smartrecruiters_resume

def execute(data):
    options = Options()
    user_agent = str(os.environ.get('USER_AGENT'))
    # options.add_argument("--headless")
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Firefox()

    driver.get(data['url'])

    sleep(5)

    # Handle iFrame -- Route to greenhouse

    if "workdayjobs" in data['url']:
        handle_workdayjobs(driver, data)
        return

    if "bamboohr" in data['url']:
        click_preapplication_button(driver)
        handle_bamboo(driver=driver, data=data)

    if "smartrecruiters" in data['url']:
        upload_smartrecruiters_resume(driver=driver)

        # handle ashbyhq.com
        # handle adp.com

    try:
        if "smartrecruiters" in data['url']:
            handle_smartrecruiters(driver=driver, data=data)
        elif "greenhouse" in data['url']:
            handle_greenhouse(driver=driver, data=data)
            enter_fields(driver)
        elif "lever" in data['url']:
            handle_lever(driver=driver, data=data)
        elif "underdog.io" in data['url']:
            handle_underdog_fields(driver=driver, data=data)
        else:
            enter_fields(driver)
    except BaseException:
        pass
