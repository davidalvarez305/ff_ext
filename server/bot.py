import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


def execute():
    options = Options()
    user_agent = str(os.environ.get('USER_AGENT'))
    options.add_experimental_option("detach", True)
    # options.add_argument("--headless")
    options.add_argument(f'user-agent={user_agent}')

    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)

    driver.get(os.environ.get('TEST_URL'))

    name = driver.find_element(By.CLASS_NAME, "_input_u5avu_30")
    name.send_keys('David')