from selenium import webdriver
from selenium.webdriver.chrome import Options
from selenium.webdriver.common.by import By
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
                                logging.FileHandler("AO_Account_Order_History" + self.timestr + ".log"),
                                logging.StreamHandler()
                            ],
                            format= '[%(asctime)s] %(levelname)s %(message)s',
                            datefmt='%H:%M:%S'
        )

    @classmethod
    def setUpClass(cls):
        cls.options = Options()
        cls.options.headless = True
        cls.driver = webdriver.Chrome(options=cls.options)
        cls.driver.loggingID = "AO_Account_Order_History"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        self.driver.reporter = self.reporter
        self.driver.set_window_size(1920, 1012)
        log_wrapper(self.driver, "Waiting for home page to load")

    def tearDown(self):
        self.driver.reporter = None

    def test_TH_TC014(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC014 [Non-Responsive]***")
        self.driver.testID = "TC014_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC014", "Check orders against excel sheet values [Non-responsive]")
        self.TH_TC014()

    def test_TH_TC014_responsive_mobile(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC014 [Responsive-mobile]***")
        self.driver.testID = "TC014_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC014_RM", "Check orders against excel sheet values [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC014()

    def test_TH_TC014_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC014 [Responsive-tablet]***")
        self.driver.testID = "TC014_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC014_RM", "Check orders against excel sheet values [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC014()

    def TH_TC014(self):
        log_wrapper(self.driver, 'Entered TH_TC014 main test logic')
       
        load_excel_sheet(self.driver, f'TH_TC014_1', 'AOOrderHistory.xlsx', 'TH_TC014')
        page = HomePage(self.driver)

        page.check_responsive()
        page.login(self.driver.data['DT_email'], self.driver.data['DT_password'])
        page.click_order_history()
            
        page = OrderHistoryPage(self.driver)

        for i in range(2, excel_get_rows('AOOrderHistory.xlsx', 'TH_TC014')):
            load_excel_sheet(self.driver, f'TH_TC014_{i}', 'AOOrderHistory.xlsx', 'TH_TC014')
            
            data = self.driver.data

            values = page.get_row_by_confirmation_num(self.driver.data['DT_order_number'])
            if self.driver.data['DT_order_number'] == values['order_num']:
                log_wrapper(self.driver, "Order numbers match: " + values['order_num'])
                self.reporter[self.driver.testID].reportStep(
                    "Check that order numbers match", 
                    "Order numbers match",
                    "Order numbers match: ",
                    True, 
                    f"Value is {values['order_num']}",
                    screenshotCallback=self.driver.save_screenshot
                    )
            else:
                log_wrapper(self.driver, "Order numbers don't match")
                self.reporter[self.driver.testID].reportStep(
                    "Check that order numbers match", 
                    "Order numbers match",
                    f"Order numbers don't match:  {values['order_num']}",
                    False, 
                    f"DB value: {data['DT_order_number']} Website value: {values['order_num']}",
                    screenshotCallback=self.driver.save_screenshot
                    )

            if self.driver.data['DT_order_date'] == values['order_date']:
                log_wrapper(self.driver, "Order dates match: " + values['order_date'])
                self.reporter[self.driver.testID].reportStep(
                    "Check that order dates match", 
                    "Order dates match",
                    "Order dates match: ",
                    True, 
                    f"Value is {values['order_date']}",
                    screenshotCallback=self.driver.save_screenshot
                    )
            else:
                log_wrapper(self.driver, "Order dates don't match")
                self.reporter[self.driver.testID].reportStep(
                    "Check that order dates match", 
                    "Order dates match",
                    "Order dates don't match: ",
                    False, 
                    f"DB value: {data['DT_order_date']} Website value: {values['order_date']}",
                    screenshotCallback=self.driver.save_screenshot
                    )
    

            if self.driver.data['DT_order_time'] == values['order_time']:
                log_wrapper(self.driver, "Order times match: " + values['order_time'])
                self.reporter[self.driver.testID].reportStep(
                    "Check that order times match", 
                    "Order times match",
                    "Order times match: ",
                    True, 
                    f"Value is {values['order_time']}",
                    screenshotCallback=self.driver.save_screenshot
                    )
            else:
                log_wrapper(self.driver, "Order times don't match")
                self.reporter[self.driver.testID].reportStep(
                    "Check that order times match", 
                    "Order times match",
                    "Order times don't match: ",
                    False, 
                    f"DB value: {data['DT_order_time']} Website value: {values['order_time']}",
                    screenshotCallback=self.driver.save_screenshot
                    )
    

            if self.driver.data['DT_product_name'] == values['product_name']:
                log_wrapper(self.driver, "Product names match: " + values['product_name'])
                self.reporter[self.driver.testID].reportStep(
                    "Check that product names match", 
                    "Product names match",
                    "Product names match: ",
                    True, 
                    f"Value is {values['product_name']}",
                    screenshotCallback=self.driver.save_screenshot
                    )
            else:
                log_wrapper(self.driver, "Product names don't match")
                self.reporter[self.driver.testID].reportStep(
                    "Check that product names match", 
                    "Product names match",
                    "Product names don't match: ",
                    False, 
                    f"DB value {data['DT_product_name']} Website value: {values['product_name']}",
                    screenshotCallback=self.driver.save_screenshot
                    )
    

            if self.driver.data['DT_quantity'] == values['quantity']:
                log_wrapper(self.driver, "Quantities match: " + values['quantity'])
                self.reporter[self.driver.testID].reportStep(
                    "Check that item quantities match", 
                    "Quantities match",
                    "Quantities match: ",
                    True, 
                    f"Value is {values['quantity']}",
                    screenshotCallback=self.driver.save_screenshot
                    )
            else:
                log_wrapper(self.driver, "Quantities don't match")
                self.reporter[self.driver.testID].reportStep(
                    "Check that item quantities match", 
                    "Quantities match",
                    "Quantities don't match: ",
                    False, 
                    f"DB value {data['DT_quantity']} Website value: {values['quantity']}",
                    screenshotCallback=self.driver.save_screenshot
                    )
    

            if self.driver.data['DT_total_price'] == values['total_price']:
                log_wrapper(self.driver, "Total prices match: " + values['total_price'])
                self.reporter[self.driver.testID].reportStep(
                    "Check that total prices match", 
                    "Prices match",
                    "Prices match: ",
                    True, 
                    f"Value is {values['total_price']}",
                    screenshotCallback=self.driver.save_screenshot
                    )
            else:
                log_wrapper(self.driver, "Total prices don't match")
                self.reporter[self.driver.testID].reportStep(
                    "Check that total prices match", 
                    "Prices match",
                    "Prices don't match: ",
                    False, 
                    f"DB value {data['DT_total_price']} Website value: {values['total_price']}",
                    screenshotCallback=self.driver.save_screenshot
                    )

        page.logout()        
    


    def test_TH_TC015(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC015 [Non-Responsive]***")
        self.driver.testID = "TC015_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC015", "Test that 'No Orders' message appears on account with no orders [Non-responsive]")
        self.TH_TC015()

    def test_TH_TC015_responsive_mobile(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC015 [Responsive-mobile]***")
        self.driver.testID = "TC015_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC015_RM", "Test that 'No Orders' message appears on account with no orders [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC015()

    def test_TH_TC015_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC015 [Responsive-tablet]***")
        self.driver.testID = "TC015_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC015_RM", "Test that 'No Orders' message appears on account with no orders [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC015()

    def TH_TC015(self):
        log_wrapper(self.driver, 'Entered TH_TC015 main test logic')
       
        load_excel_sheet(self.driver, f'TH_TC015_1', 'AOOrderHistory.xlsx', 'TH_TC015')
        page = HomePage(self.driver)
        page.check_responsive()
        page.login(self.driver.data['DT_email'], self.driver.data['DT_password'])
        page.click_order_history()
            
        page = OrderHistoryPage(self.driver)
        if page.element_is_loaded(OrderHistoryPageLocators.By_no_orders):
            self.driver.reporter[self.driver.testID].reportStep(
                "Checking for 'No Orders' text", 
                "Found 'No Orders' text", 
                "Found 'No Orders' text",
                True,
                "",
                screenshotCallback=self.driver.save_screenshot
            )
        else:
            self.driver.reporter[self.driver.testID].reportStep(
                "Checking for 'No Orders' text", 
                "Found 'No Orders' text", 
                "Didn't find 'No Orders' text",
                False,
                "",
                screenshotCallback=self.driver.save_screenshot
            )

if __name__ == "__main__":
    unittest.main()