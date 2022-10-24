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
        self.timestr = "SwagLabsHeadless"+mytime()
        self.reporter = TestSuiteReporter.TestSuiteReporter(self.timestr, "../Reports", "Kimberly Modeste")
        self.screenshotPath = "../.screenshots/"
        self.path = "../TestCasesExcel.xlsx"

    @classmethod
    def setUp(self):
        self.imageFolders = []
        options = Options()
        options.headless = True
        self.browser = webdriver.Chrome(options=options)
        self.browser.get('https://www.saucedemo.com/')


    def test_001_login_logout(self):
        print(f"#########################################")     
        wb = openpyxl.load_workbook(self.path)  

        print(f"Browser Opened: {self.browser.title}")
        
        TCN = self.timestr
        self.imageFolders.append(TCN)
        r = 2
        self.reporter.addTestCase(TCN, "TC001", "User will be loging in and out of the SwagLabs Website")

        print(f"Starting to Login...")
        if self.browser.find_element(by=By.CLASS_NAME, value="login-box"):
            loginHeadless(self.browser, self.reporter,TCN)
        print(f"Login completed")

        # Logout
        WebDriverWait(self.browser, 5).until(expected_conditions.element_to_be_clickable(self.browser.find_element(by=By.ID, value="react-burger-menu-btn")))
        self.browser.find_element(by=By.ID, value="react-burger-menu-btn").click()
        buttonList = self.browser.find_element(by=By.CLASS_NAME, value="bm-item-list").find_elements(by=By.TAG_NAME, value="a")
        WebDriverWait(self.browser, 60).until(expected_conditions.element_to_be_clickable(buttonList[2]))
        buttonList[2].click()

        self.reporter[TCN].reportStep(stepDescription="User should click the hamburger and logout", 
        expectedBehavior="Pass", actualBehavior="Pass", testStatus=True, dataString="", 
        screenshotCallback=self.browser.find_element(by=By.TAG_NAME, value='body').screenshot, 
        imagePath=self.screenshotPath)
        print(f"Logged out")
        print(f"#########################################")


    def tearDown(self):
        self.browser.close()

    @classmethod
    def tearDownClass(self):
        del self.reporter
        zipObj = zipfile.ZipFile(self.timestr+".zip", 'w')
        zipObj.write("../Reports/"+self.timestr + ".html")
        for folder in self.imageFolders:
            for image in os.listdir("../.screenshots/"+folder+"/"):
                zipObj.write("../.screenshots/"+folder+"/"+image)
        zipObj.close()
        upload_file(self.timestr+".zip","scrumbags-reports")
            


unittest.main()
