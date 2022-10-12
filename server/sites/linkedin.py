import os
from random import uniform
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from site_router import site_router

def login(driver):
    # Get Input Fields
    username_input = driver.find_element(By.ID, "session_key")
    password_input = driver.find_element(By.ID, "session_password")

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

def handle_job(driver, data, values):
    job_details = driver.find_element(By.CLASS_NAME, 'jobs-details')
    buttons = job_details.find_elements(By.TAG_NAME, 'button')
    
    for button in buttons:
        if "Apply" in button.get_attribute('innerText'):
            button.click()
    
    sleep(5)

    # Switch Tab & Fill Fields
    driver.switch_to.window(driver.window_handles[1])
    data['url'] = driver.current_url

    site_router(driver=driver, data=data, values=values)

    driver.close()

def handle_linkedin(driver, data, values):

    # Attempt to Login
    # login(driver)
    input("Press enter after logging in: ")

    # Access Job Search
    go_to_jobs_search(driver)
    
    sleep(5)
    jobs = driver.find_elements(By.XPATH, '//a[@class="disabled ember-view job-card-container__link job-card-list__title"]')
    
    for job in jobs:
        try:
            job.click()
            handle_job(driver=driver, data=data, values=values)
        except BaseException as err:
            print(err)
            continue