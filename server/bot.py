import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from handle_fields import enter_fields
from server.helpers.sheets import get_values
from sites.bamboo import handle_bamboo
from sites.underdog import handle_underdog_fields
from sites.lever import handle_lever
from sites.smartrecruiters import handle_smartrecruiters, upload_smartrecruiters_resume
from sites.greenhouse import handle_greenhouse
from sites.workdayjobs import handle_workdayjobs
from utils import click_preapplication_button

def execute(data):
    rows = get_values(os.environ.get('SHEETS_ID'), f"{os.environ.get('TAB_NAME')}!A2:E")
    values = []

    for row in rows:
        values.append({ "data": row[0], "question": row[1:] })

    options = Options()
    user_agent = str(os.environ.get('USER_AGENT'))
    # options.add_argument("--headless")
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Firefox()

    driver.get(data['url'])

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
        if "greenhouse" in data['url']:
            handle_greenhouse(driver=driver, data=data, values=values)
        elif "smartrecruiters" in data['url']:
            handle_smartrecruiters(driver=driver, data=data, values=values)
        elif "lever" in data['url']:
            handle_lever(driver=driver, data=data, values=values)
        elif "underdog.io" in data['url']:
            handle_underdog_fields(driver=driver, data=data, values=values)
        else:
            enter_fields(driver, values)
    except BaseException:
        pass
