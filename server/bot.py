import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from handle_fields import enter_fields
from sites.lever import handle_lever
from sites.smartrecruiters import handle_smartrecruiters, upload_smartrecruiters_resume
from sites.greenhouse import handle_greenhouse
from sites.workdayjobs import handle_workdayjobs
from utils import click_preapplication_button, handle_bamboo, handle_underdog_fields

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
        handle_bamboo(driver=driver, data=data)

    if "smartrecruiters" in data['url']:
        upload_smartrecruiters_resume(driver=driver)

        # handle ashbyhq.com
        # handle adp.com

    try:
        iframe = driver.find_elements(By.TAG_NAME, 'iframe')
        if len(iframe) > 0 or "greenhouse" in data['url']:
            handle_greenhouse(driver=driver, data=data)
        elif "smartrecruiters" in data['url']:
            handle_smartrecruiters(driver=driver, data=data)
        elif "lever" in data['url']:
            handle_lever(driver=driver, data=data)
        elif "underdog.io" in data['url']:
            handle_underdog_fields(driver=driver, data=data)
        else:
            enter_fields(driver)
    except BaseException:
        pass
