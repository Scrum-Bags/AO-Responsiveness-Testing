import string
from time import sleep
import unittest
import openpyxl
import random
import os
import zipfile
from S3_Tool import upload_file
userStr = ".."
import TestSuiteReporter
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from SLCommonFunctionsJenkins import loginHeadless, mytime, rand
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestCases(unittest.TestCase):
    
    # @classmethod
    def __init__(self, *args, **kwargs):
        super(TestCases, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        cls.imageFolders = []
        cls.timestr = "SwagLabsHeadless"+mytime()
        cls.reporter = TestSuiteReporter.TestSuiteReporter(cls.timestr, "../Reports/", "Kimberly Modeste")
        cls.screenshotPath = "../.screenshots/"
        cls.path = "../TestCasesExcel.xlsx"


    def test_001_login_logout(self):
        print(f"#########################################")
       
        wb = openpyxl.load_workbook(self.path)  
      
        option = Options()
        option.headless = True
        browser = webdriver.Chrome(options=option)
        browser.get('https://www.saucedemo.com/')
        print(f"Browser Opened: {browser.title}")
        
        TCN = self.timestr
        self.imageFolders.append(TCN)
        r = 2
        self.reporter.addTestCase(TCN, "TC001", "User will be loging in and out of the SwagLabs Website")

        print(f"Starting to Login...")
        if browser.find_element(by=By.CLASS_NAME, value="login-box"):
            loginHeadless(browser, self.reporter,TCN)
        print(f"Login completed")

        # Logout
        WebDriverWait(browser, 5).until(expected_conditions.element_to_be_clickable(browser.find_element(by=By.ID, value="react-burger-menu-btn")))
        browser.find_element(by=By.ID, value="react-burger-menu-btn").click()
        buttonList = browser.find_element(by=By.CLASS_NAME, value="bm-item-list").find_elements(by=By.TAG_NAME, value="a")
        WebDriverWait(browser, 60).until(expected_conditions.element_to_be_clickable(buttonList[2]))
        buttonList[2].click()

        self.reporter[TCN].reportStep(stepDescription="User should click the hamburger and logout", 
        expectedBehavior="Pass", actualBehavior="Pass", testStatus=True, dataString="", 
        screenshotCallback=browser.find_element(by=By.TAG_NAME, value='body').screenshot, 
        imagePath=''+'img'+mytime(), imageEmbed=False)
        print(f"Logged out")
        print(f"#########################################")
        browser.close()


    @classmethod
    def tearDownClass(cls):
        del cls.reporter
        zipObj = zipfile.ZipFile(cls.timestr+".zip", 'w')
        zipObj.write("../Reports/"+cls.timestr + ".html")
        for folder in cls.imageFolders:
            print(folder)
            for image in os.listdir("./.screenshots/"+folder+"/"):
                print(image)
                zipObj.write("../.screenshots/"+folder+"/"+image)
        zipObj.close()
        upload_file(cls.timestr+".zip","scrumbags-reports")


unittest.main()
