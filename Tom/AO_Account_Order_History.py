from tkinter import W
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, random, unittest, logging

from TestSuiteReporter import TestSuiteReporter
from AO_POMs import *
from Utilities import *

class AO_Account_Order_History(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(AO_Account_Order_History, self).__init__(*args, **kwargs)
        self.timestr = time.strftime("%Y-%m-%d--%I_%M_%S%p")
        self.reporter = TestSuiteReporter(self.timestr, "./", "Tom")
        logging.basicConfig(level=logging.INFO,
                            handlers=[
                                logging.FileHandler("AO_Browse_Store" + self.timestr + ".log"),
                                logging.StreamHandler()
                            ],
                            format= '[%(asctime)s] %(levelname)s %(message)s',
                            datefmt='%H:%M:%S'
        )

    @classmethod
    def setUpClass(cls):
        cls.edge_options = Options()
        cls.edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        cls.edge_options.headless = False
        cls.driver = webdriver.Edge(options=cls.edge_options)
        cls.driver.loggingID = "AO_Account_Order_History"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.reporter = self.reporter
        self.driver.set_window_size(945, 1012)
        log_wrapper(self.driver, "Waiting for home page to load")

    def tearDown(self):
        self.driver.reporter = None

    def test_TH_TC014(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC014 [Non-Responsive]***")
        self.driver.testID = "TC014_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC014", "TODO")
        load_excel_sheet(self.driver, 'TH_TC014', 'AOOrderHistory.xlsx', 'Sheet1')
        self.TH_TC014()

    def test_TH_TC014_responsive(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC014 [Responsive]***")
        self.driver.testID = "TC014_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC014", "TODO")
        self.driver.set_window_size(500, 900)
        load_excel_sheet(self.driver, 'TH_TC014_R', 'AOOrderHistory.xlsx', 'Sheet1')
        self.TH_TC014()

    def TH_TC014(self):
        data = self.driver.data
        log_wrapper(self.driver, 'Entered TH_TC014 main test logic')
        if self.driver.get_window_size()['width'] < 550:
            report_event_and_log(self.driver, 'Detected responisve')
            responsive = True
        else:
            report_event_and_log(self.driver, 'Responsive not detected')
            responsive = False

        page = HomePage(self.driver)
        page.login(data['DT_email'], data['DT_password'])

        time.sleep(5)

if __name__ == "__main__":
    unittest.main()