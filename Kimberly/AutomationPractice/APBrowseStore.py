import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from APCommonFunctions import selectCategories, login
from TestSuiteReporter import TestSuiteReporter
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class TestCases(unittest.TestCase):

    def test_001_browse_store_pos(self):
        browser = webdriver.Chrome()
        browser.get('http://automationpractice.com/index.php')

        reporter = TestSuiteReporter("AutomationPractice", "C:/Users/OWNER/OneDrive/Documents/UFTOne/tests/selenium/Test/Kimberly/Reports/", "Kimberly Modeste")
        reporter.addTestCase("Browse Store Reg", "TC001", "User will be browsing the AutomationPractice Website")
       
        if browser.find_element(by=By.CLASS_NAME, value="login"):
            login(browser, reporter, "Browse Store Reg", 2)
        browser.find_element(by=By.XPATH, value="//a[@title='My Store']").click()
        WebDriverWait(browser, 60).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "sf-menu.clearfix.menu-content")))
        
        selectCategories(browser, reporter, "Browse Store Reg", 2)
        browser.find_element(by=By.CLASS_NAME, value="logout").click() 

        
    def test_002_browse_store_pos(self):
        browser = webdriver.Chrome()
        browser.get('http://automationpractice.com/index.php')

        reporter = TestSuiteReporter("AutomationPractice", "C:/Users/OWNER/OneDrive/Documents/UFTOne/tests/selenium/Test/Kimberly/Reports/", "Kimberly Modeste")
        reporter.addTestCase("Browse Store All", "TC002", "User will be browsing the AutomationPractice Website clicking everything")
       
        if browser.find_element(by=By.CLASS_NAME, value="login"):
            login(browser, reporter, "Browse Store All", 2)
        browser.find_element(by=By.XPATH, value="//a[@title='My Store']").click()
        WebDriverWait(browser, 60).until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "sf-menu.clearfix.menu-content")))
        
        selectCategories( browser, reporter, "Browse Store All", 4)
        browser.find_element(by=By.CLASS_NAME, value="logout").click() 

unittest.main()