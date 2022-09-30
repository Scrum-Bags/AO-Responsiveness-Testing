import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from CommonFunctions import personal_info_update, update_address, login, signout
from TestSuiteReporter import TestSuiteReporter


class TestCases(unittest.TestCase):

    def test_000_selenium_poc_login_logout(self):
        reporter = TestSuiteReporter("SeleniumPoc", "C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/", "Kimberly Modeste")

        browser = webdriver.Chrome()
        browser.get('http://automationpractice.com/index.php')
        
        TCN = "SeleniumLoginLogout"
        reporter.addTestCase(TCN, "TC000","Users will be Logging in valid data and Logging out")

        if browser.find_element(by=By.CLASS_NAME, value="login"):
             login( browser, reporter, TCN, r)
        signout(browser)
        browser.quit()

    def test_001_selenium_poc_personal_info_pos(self):
        reporter = TestSuiteReporter("SeleniumPoc", "C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/", "Kimberly Modeste")   
      
        browser = webdriver.Chrome()
        browser.get('http://automationpractice.com/index.php')

        TCN = "SeleniumPersonalInfoPos"
        r = 2
        reporter.addTestCase(TCN, "TC001","Users will be updating Personal Information with valid data")
        if browser.find_element(by=By.CLASS_NAME, value="login-box"):
            login( browser, reporter, TCN, r)

        personal_info_update(browser, reporter, TCN, r)
        signout(browser)
        browser.quit()

    def test_002_selenium_poc_Update_Address_pos(self):
        reporter = TestSuiteReporter("SeleniumPoc", "C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/", "Kimberly Modeste")
  
        browser = webdriver.Chrome()
        browser.get('http://automationpractice.com/index.php')


        TCN = "SeleniumUpdateAddressPos"
        r = 2
        reporter.addTestCase(TCN, "TC002","Users will be updating Address with valid Information")
        if browser.find_element(by=By.CLASS_NAME, value="login-box"):
            login( browser, reporter, TCN, r)

        update_address(browser, reporter, TCN, r)
        signout(browser)
        browser.quit()

    def test_003_selenium_poc_personal_info_err(self):
        reporter = TestSuiteReporter("SeleniumPoc", "C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/", "Kimberly Modeste")   
      
        browser = webdriver.Chrome()
        browser.get('http://automationpractice.com/index.php')

        TCN = "SeleniumPersonalInfoErr"
        r = 2
        reporter.addTestCase(TCN, "TC003","Users will be updating Personal Information with invalid Email")
        if browser.find_element(by=By.CLASS_NAME, value="login-box"):
            login( browser, reporter, TCN, r)

        personal_info_update(browser, reporter, TCN, r)
        signout(browser)
        browser.quit()

    def test_002_selenium_poc_Update_Address_err(self):
        reporter = TestSuiteReporter("SeleniumPoc", "C:/Users/OWNER/OneDrive/Documents/UFTOne/reports/", "Kimberly Modeste")
  
        browser = webdriver.Chrome()
        browser.get('http://automationpractice.com/index.php')


        TCN = "SeleniumUpdateAddressErr"
        r = 2
        reporter.addTestCase(TCN, "TC002","Users will be updating address with invalid First Name")
        if browser.find_element(by=By.CLASS_NAME, value="login-box"):
            login( browser, reporter, TCN, r)

        update_address(browser, reporter, TCN, r)
        signout(browser)
        browser.quit()


unittest.main()