import os
from random import uniform
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def login(driver):
    # Get Input Fields
    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")

    # Enter Input
    simulate_typing(username_input, os.environ.get('EMAIL'))
    username_input.send_keys(Keys.TAB)
    sleep(1)
    simulate_typing(password_input, os.environ.get('LINKEDIN_PASSWORD'))
    sleep(1)
    password_input.send_keys(Keys.RETURN)

def simulate_typing(element, txt):
    for letter in txt:
        sleep(uniform(0.0250, 0.25))
        element.send_keys(letter)

def find_jobs_button(driver):
    try:
        filters = driver.find_elements(By.XPATH, '//*[@class="search-reusables__primary-filter"]')

        for filter in filters:
            btn = filter.find_element(By.TAG_NAME, 'button')
            if "Jobs" in btn.get_attribute('innerText'):
                btn.click()
    except BaseException:
        input("Press enter after looking up jobs: ")

def go_to_jobs_search(driver):
    try:
        search_input = driver.find_element(By.XPATH, '//input[@placeholder="Search"]')
        search_input.send_keys(os.environ.get('JOB_SEARCH'))
        search_input.send_keys(Keys.RETURN)
        sleep(4)
        find_jobs_button(driver)
    except BaseException:
        input("Press enter after looking up jobs: ")

def handle_job(driver):
    try:
        job_details = driver.find_element(By.CLASS_NAME, 'jobs-details')
        buttons = job_details.find_elements(By.TAG_NAME, 'button')
        
        for button in buttons:
            if "Apply" in button.get_attribute('innerText'):
                button.click()
        
        sleep(4)

        print('current url: ', driver.current_url)

        driver.close()
    except BaseException:
        input("Press enter after handling job: ")

def loop_linkedin():
    load_dotenv()

    options = Options()
    # options.add_argument("--headless")
    options.add_argument(f"user-agent={os.environ.get('USER_AGENT')}")
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("disable-popup-blocking")
    options.add_argument("disable-notifications")

    driver = webdriver.Firefox() 

    driver.get("https://www.linkedin.com/login?trk=guest_homepage-basic_nav-header-signin")

    # Attempt to Login
    login(driver)
    input("Press enter after logging in: ")

    # Access Job Search
    go_to_jobs_search(driver)
    
    sleep(3)
    jobs = driver.find_elements(By.XPATH, '//a[@class="disabled ember-view job-card-container__link job-card-list__title"]')
    
    for job in jobs:
        job.click()
        handle_job(driver)
        

loop_linkedin()