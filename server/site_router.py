from selenium.webdriver.common.by import By
from handle_fields import enter_fields
from sites.bamboo import handle_bamboo
from sites.underdog import handle_underdog_fields
from sites.lever import handle_lever
from sites.smartrecruiters import handle_smartrecruiters, upload_smartrecruiters_resume
from sites.greenhouse import handle_greenhouse
from sites.workdayjobs import handle_workdayjobs
from utils import click_preapplication_button

def site_router(driver, data, values):
    if "workdayjobs" in data['url']:
        handle_workdayjobs(driver, data)
        return

    if "bamboohr" in data['url']:
        click_preapplication_button(driver)
        handle_bamboo(driver=driver, data=data)

    if "smartrecruiters" in data['url']:
        upload_smartrecruiters_resume(driver=driver)

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
            enter_fields(driver, values, data)
    except BaseException as err:
        print("Error in site router: ", err)