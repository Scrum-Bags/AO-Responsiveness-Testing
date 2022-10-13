import random
import openpyxl
from sys import path
import os
userStr = os.environ['USERPROFILE']
userStr = userStr.replace('\\', '/')
path.append(f"{userStr}/OWNER/OneDrive/Documents/UFTOne/tests/selenium/Test")
from Kimberly import TestSuiteReporter
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
    browser: webdriver, 
    reporter: TestSuiteReporter,
    TCRN: str
):
    username = "standard_user"
    password = "secret_sauce"

    if username == "standard_user":
        ActualBehavior = "Pass"
        TestStatus = True
    else :
        ActualBehavior="Fail"
        TestStatus = False

    browser.find_element(by=By.ID, value='user-name').send_keys(username)
    browser.find_element(by=By.ID, value='password').send_keys(password)
    browser.find_element(by=By.ID, value='login-button').click()

    reporter[TCRN].reportStep(stepDescription="User should be logged in by one of the permitted username and passwword to login", 
    expectedBehavior="Pass", actualBehavior=ActualBehavior, testStatus=TestStatus, dataString=f"Username: {username}; Password: {password}", 
    screenshotCallback=browser.find_element(by=By.TAG_NAME, value='body').screenshot, 
    imagePath=f"./Kimberly/.screenshots/{TCRN}/img{mytime()}", imageEmbed=False)

def loginHeadless(
    browser: webdriver, 
    reporter: TestSuiteReporter,
    TCRN: str
):
    username = "standard_user"
    password = "secret_sauce"

    if username == "standard_user":
        ActualBehavior = "Pass"
        TestStatus = True
    else :
        ActualBehavior="Fail"
        TestStatus = False

    print(f"Username and Password being entered...")
    browser.find_element(by=By.ID, value='user-name').send_keys(username)
    browser.find_element(by=By.ID, value='password').send_keys(password)
    browser.find_element(by=By.ID, value='login-button').click()
    print(f"Username and passsword Submitted")


    try:
        browser.find_element(by=By.CLASS_NAME, value="error-message-container.error").click()
    except:
        print(f"Username and Password entered successfully")
        ActualBehavior = "Pass"
        TestStatus = True
    else:
        print(f"Username and passsword incorrect")
        ActualBehavior="Fail"
        TestStatus = False

    reporter[TCRN].reportStep(stepDescription="User should be logged in by one of the permitted username and passwword to login", 
    expectedBehavior="Pass", actualBehavior=ActualBehavior, testStatus=TestStatus, dataString=f"Username: {username}; Password: {password}", 
    screenshotCallback=browser.find_element(by=By.TAG_NAME, value='body').screenshot, 
    imagePath=f"./Kimberly/.screenshots/{TCRN}/img{mytime()}", imageEmbed=False)



