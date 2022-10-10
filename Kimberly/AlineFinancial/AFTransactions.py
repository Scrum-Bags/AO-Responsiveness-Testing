from pydoc import cli
import time
import unittest
import openpyxl
from sys import path
path.append("C:/Users/OWNER/OneDrive/Documents/UFTOne/tests/selenium/Test")
from Kimberly import TestSuiteReporter
from selenium import webdriver
from CommonFunctions import login, transactionChecker, loginHeadless, transactionCheckerHeadless
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options


class TestCases(unittest.TestCase):

    # def test_001_view_transactions(self):
    #     reporter = TestSuiteReporter.TestSuiteReporter("AlineFinancial", "C:/Users/OWNER/OneDrive/Documents/UFTOne/tests/selenium/Test/Kimberly/Reports", "Kimberly Modeste") 

    #     browser = webdriver.Chrome()
    #     browser.get('http://uftcapstone-dev-landing.s3-website-us-east-1.amazonaws.com/')

    #     TCN = "AlineFinancialSearchTrans"
    #     r = 2
    #     reporter.addTestCase(TCN, "TC001", "Users will be using the search bar to search for results")

    #     login(browser, reporter, TCN, r)

    #     #By date
    #     WebDriverWait(browser, 120).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 0, r, 1)

    #     #By Account
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 1, r, 3)

    #     #By Description
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 2, r, 5)

    #     #By Amount
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 3, r, 7)

    #     #By Balance
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 4, r, 9)

    # def test_002_view_transactions(self):
    #     reporter = TestSuiteReporter.TestSuiteReporter("AlineFinancial", "C:/Users/OWNER/OneDrive/Documents/UFTOne/tests/selenium/Test/Kimberly/Reports", "Kimberly Modeste") 

    #     browser = webdriver.Chrome()
    #     browser.get('http://uftcapstone-dev-landing.s3-website-us-east-1.amazonaws.com/')

    #     TCN = "AlineFinancialSearchTransf"
    #     r = 4
    #     reporter.addTestCase(TCN, "TC002", "Users will be using the search bar to search for results that don't exist")

    #     login(browser, reporter, TCN, r)

    #     #By date
    #     WebDriverWait(browser, 120).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 0, r, 1)

    #     #By Account
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 1, r, 3)

    #     #By Description
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 2, r, 5)

    #     #By Amount
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 3, r, 7)

    #     #By Balance
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 4, r, 9)

    # def test_003_view_transactions(self):
    #     reporter = TestSuiteReporter.TestSuiteReporter("AlineFinancial", "C:/Users/OWNER/OneDrive/Documents/UFTOne/tests/selenium/Test/Kimberly/Reports", "Kimberly Modeste") 

    #     options = Options()
    #     options.headless = True
    #     browser = webdriver.Chrome(options=options)
    #     browser.get('http://uftcapstone-dev-landing.s3-website-us-east-1.amazonaws.com/')

    #     TCN = "AlineFinancialSearchTransHp"
    #     r = 2
    #     reporter.addTestCase(TCN, "TC003", "Users will be using the search bar to search for results in headless mode")

    #     print("Starting up headless login")
    #     loginHeadless(browser, reporter, TCN, r)
    #     print("Finished headless login")

    #     #By date
    #     WebDriverWait(browser, 120).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     print("Starting up Transaction checker in headless mode")
    #     print("Searching by: Date")
    #     transactionCheckerHeadless(browser, reporter, TCN, 0, r, 1)
    #     print("Finished Transaction in Headless mode: Date")

    #     #By Account
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     print("Starting up Transaction checker in headless mode")
    #     print("Searching by: Account")
    #     transactionCheckerHeadless(browser, reporter, TCN, 1, r, 3)
    #     print("Finished Transaction in Headless mode: Account")


    #     #By Description
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     print("Starting up Transaction checker in headless mode")
    #     print("Searching by: Description")
    #     transactionCheckerHeadless(browser, reporter, TCN, 2, r, 5)
    #     print("Finished Transaction in Headless mode: Date")


    #     #By Amount
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     print("Starting up Transaction checker in headless mode")
    #     print("Searching by: Amount")
    #     transactionCheckerHeadless(browser, reporter, TCN, 3, r, 7)
    #     print("Finished Transaction in Headless mode: Date")

    #     #By Balance
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     print("Starting up Transaction checker in headless mode")
    #     print("Searching by: Balance")
    #     transactionCheckerHeadless(browser, reporter, TCN, 4, r, 9)
    #     print("Finished Transaction in Headless mode: Date")

    # def test_004_view_transactions(self):
    #     reporter = TestSuiteReporter.TestSuiteReporter("AlineFinancial", "C:/Users/OWNER/OneDrive/Documents/UFTOne/tests/selenium/Test/Kimberly/Reports", "Kimberly Modeste") 

    #     browser = webdriver.Chrome()
    #     browser.get('http://uftcapstone-dev-landing.s3-website-us-east-1.amazonaws.com/')

    #     TCN = "AlineFinancialSearchTransHf"
    #     r = 4
    #     reporter.addTestCase(TCN, "TC004", "Users will be using the search bar to search for results that don't exist in headless mode")

    #     print("Starting up headless login")
    #     loginHeadless(browser, reporter, TCN, r)
    #     print("Finished headless login")

    #     #By date
    #     WebDriverWait(browser, 120).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     print("Starting up Transaction checker in headless mode")
    #     print("Searching by: Date")
    #     transactionCheckerHeadless(browser, reporter, TCN, 0, r, 1)
    #     print("Finished Transaction in Headless mode: Date")

    #     #By Account
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     print("Starting up Transaction checker in headless mode")
    #     print("Searching by: Account")
    #     transactionCheckerHeadless(browser, reporter, TCN, 1, r, 3)
    #     print("Finished Transaction in Headless mode: Account")


    #     #By Description
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     print("Starting up Transaction checker in headless mode")
    #     print("Searching by: Description")
    #     transactionCheckerHeadless(browser, reporter, TCN, 2, r, 5)
    #     print("Finished Transaction in Headless mode: Date")


    #     #By Amount
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     print("Starting up Transaction checker in headless mode")
    #     print("Searching by: Amount")
    #     transactionCheckerHeadless(browser, reporter, TCN, 3, r, 7)
    #     print("Finished Transaction in Headless mode: Date")

    #     #By Balance
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     print("Starting up Transaction checker in headless mode")
    #     print("Searching by: Balance")
    #     transactionCheckerHeadless(browser, reporter, TCN, 4, r, 9)
    #     print("Finished Transaction in Headless mode: Date")

    def test_005_view_transactions(self):
        reporter = TestSuiteReporter.TestSuiteReporter("AlineFinancial", "C:/Users/OWNER/OneDrive/Documents/UFTOne/tests/selenium/Test/Kimberly/Reports", "Kimberly Modeste") 

        browser = webdriver.Chrome()
        browser.get('http://uftcapstone-dev-landing.s3-website-us-east-1.amazonaws.com/')

        TCN = "AlineFinancialSearchTransR"
        r = 2
        reporter.addTestCase(TCN, "TC005", "Users will be using the search bar to search for results changing the page window every few steps")

        
        browser.set_window_size(700, 700)

        loginHeadless(browser, reporter, TCN, r)

        #By date
        WebDriverWait(browser, 120).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
        transactionCheckerHeadless(browser, reporter, TCN, 0, r, 1)

        # #By Account
        # WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
        # transactionChecker(browser, reporter, TCN, 1, r, 3)

        # #By Description
        # WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
        # transactionChecker(browser, reporter, TCN, 2, r, 5)

        # #By Amount
        # WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
        # transactionChecker(browser, reporter, TCN, 3, r, 7)

        # #By Balance
        # WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
        # transactionChecker(browser, reporter, TCN, 4, r, 9)

    # def test_006_view_transactions(self):
    #     reporter = TestSuiteReporter.TestSuiteReporter("AlineFinancial", "C:/Users/OWNER/OneDrive/Documents/UFTOne/tests/selenium/Test/Kimberly/Reports", "Kimberly Modeste") 

    #     browser = webdriver.Chrome()
    #     browser.get('http://uftcapstone-dev-landing.s3-website-us-east-1.amazonaws.com/')

    #     TCN = "AlineFinancialSearchTransfR"
    #     r = 4
    #     reporter.addTestCase(TCN, "TC006", "Users will be using the search bar to search for results that don't exist while changing the window every few steps")

    #     login(browser, reporter, TCN, r)

    #     #By date
    #     WebDriverWait(browser, 120).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 0, r, 1)

    #     #By Account
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 1, r, 3)

    #     #By Description
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 2, r, 5)

    #     #By Amount
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 3, r, 7)

    #     #By Balance
    #     WebDriverWait(browser, 60).until( expected_conditions.presence_of_element_located((By.XPATH, "//input[@name='searchTerm']")))
    #     transactionChecker(browser, reporter, TCN, 4, r, 9)

   

unittest.main()