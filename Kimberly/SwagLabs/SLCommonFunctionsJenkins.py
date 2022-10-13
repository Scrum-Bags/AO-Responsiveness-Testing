import random
import openpyxl
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions



def mytime():
    now = datetime.now()
    current_time = now.strftime("%Y%m%d_%H%M%S")
    return current_time 

def rand ():
    random.seed()
    w = random.randint(700, 4069)
    h = random.randint(700, 2160)
    return {w, h}

def login(
    browser: webdriver
):
    username = "standard_user"
    password = "secret_sauce"


    browser.find_element(by=By.ID, value='user-name').send_keys(username)
    browser.find_element(by=By.ID, value='password').send_keys(password)
    browser.find_element(by=By.ID, value='login-button').click()


def loginHeadless(
    browser: webdriver
):
    username = "standard_user"
    password = "secret_sauce"


    print(f"Username and Password being entered...")
    browser.find_element(by=By.ID, value='user-name').send_keys(username)
    browser.find_element(by=By.ID, value='password').send_keys(password)
    browser.find_element(by=By.ID, value='login-button').click()
    print(f"Username and passsword Submitted")


    try:
        browser.find_element(by=By.CLASS_NAME, value="error-message-container.error").click()
    except:
        print(f"Username and Password entered successfully")
    else:
        print(f"Username and passsword incorrect")
        
