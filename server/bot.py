import os
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from utils import handle_greenhouse, handle_lever, handle_underdog_fields


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

    WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.TAG_NAME,"html"))

    for el in data['results']:
        try:
            if el['field'] == 'name':
                name = driver.find_element(By.NAME, el['name'])
                name.send_keys(get_data(el))
            if el['field'] == 'id':
                name = driver.find_element(By.ID, el['name'])
                name.send_keys(get_data(el))
            if el['field'] == 'className':
                name = driver.find_element(By.CLASS_NAME, el['name'])
                name.send_keys(get_data(el))
        except BaseException as error:
            # print(f"Error: {error}. Element: {el}")
            continue

    # handle smartrecruiters.com
    # handle workdayjobs.com
    # handle dice.com

    try:
        if "lever" in data['url']:
            handle_lever(driver=driver, data=data)
        elif "underdog.io" in data['url']:
            handle_underdog_fields(driver=driver, data=data)
        else:
            handle_greenhouse(driver=driver, data=data)
    except BaseException as error:
        # print(f"Error: {error}. Element: {el}")
        pass
