import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


def execute(data):
    options = Options()
    user_agent = str(os.environ.get('USER_AGENT'))
    # options.add_argument("--headless")
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Firefox()

    driver.get(data['url'])

    print(data['results'])
    for el in data['results']:
        try:
            if el['field'] == 'name':
                name = driver.find_element(By.NAME, el['name'])
                name.send_keys(el['data'])
            if el['field'] == 'id':
                name = driver.find_element(By.ID, el['name'])
                name.send_keys(el['data'])
            if el['field'] == 'className':
                name = driver.find_element(By.CLASS_NAME, el['name'])
                name.send_keys(el['data'])
        except BaseException as error:
            print(f"Error: {error}. Element: {el}")
            continue
