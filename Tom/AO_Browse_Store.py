from selenium import webdriver
from selenium.webdriver.common.by import By 
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, random, unittest, logging

#import sys
#sys.path.append("D:\Documents\Selenium\Shared")

from TestSuiteReporter import TestSuiteReporter
from ExcelReader import excelReader
from AO_POMs import *

from Utilities import log_wrapper

class AO_Browse_Store(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(AO_Browse_Store, self).__init__(*args, **kwargs)
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
        cls.options = Options()
        cls.options.headless = True
        cls.driver = webdriver.Firefox(options=cls.options)
        cls.driver.loggingID = "AO_Browse_Store"

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self):
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        log_wrapper(self.driver, "Waiting for home page to load")
        self.driver.reporter = self.reporter
        self.driver.set_window_size(1920, 1012)

    def tearDown(self):
        self.driver.reporter = None

    #test single items
    def test_TH_TC001(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC001 [Non-responsive]***")
        self.driver.testID = "TC001_" + str(random.getrandbits(64)) 
        self.reporter.addTestCase(self.driver.testID, "TH_TC001", "Test speakers page options using excel data [Non-Responsive]")
        self.TH_TC001()

    def test_TH_TC001_responsive_mobile(self):
        log_wrapper(self.driver, '***BEGINNING TH_TC001 [Responsive-mobile]***')
        self.driver.testID = "TC001_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC001_RM", "Test Speakers page options using excel data [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC001()

    def test_TH_TC001_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC001 [Responsive-tablet]***")
        self.driver.testID = "TC001_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC001_RT", "Test Speakers page options using excel data [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC001()

    def TH_TC001(self):
        driver = self.driver
        reporter = self.reporter
        testID = self.driver.testID
        log_wrapper(self.driver, 'Entered TH_TC001 main test logic')
        log_wrapper(self.driver, 'Checking for responsive webpage')

        page = HomePage(driver)
        page.check_responsive()

        page.click_speakers()
        page = SpeakersPage(driver)
        objExcel = excelReader("./AOBrowseStore.xlsx", 0)
        rowNum = 1 #for keeping track of datarow for reporting

        for dataRow in objExcel:
            rowNum += 1
            DT_price = float(dataRow["DT_price"])
            DT_compat = dataRow["DT_compat"]
            DT_manufacturer = dataRow["DT_manufacturer"]
            DT_weight =dataRow["DT_weight"]
            DT_wireless = dataRow["DT_wireless"]
            DT_color = dataRow["DT_color"]
            DT_expected_items = int(dataRow["DT_expected_items"])

            dataString = "Price = " + str(DT_price) + \
                "<br>Compatability option = " + DT_compat + \
                "<br>Manufacturer option = " + DT_manufacturer + \
                "<br>Weight option = " + DT_weight + \
                "<br>Wireless option = " + DT_wireless + \
                "<br>Color option = " + DT_color
            log_wrapper(self.driver, "Loaded test values from excel")

            reporter[testID].reportEvent("Load row #" + str(rowNum) + " values from datasheet", False, dataString)

            if self.driver.responsive_mobile:
                page.open_responsive_filter()

            page.expand_expander(page.price_expander)
            page.set_price(DT_price)
            page.expand_expander(page.compat_expander)
            page.set_compat(DT_compat)
            page.expand_expander(page.manufacturer_expander)
            page.set_manufacturer(DT_manufacturer)
            page.expand_expander(page.weight_expander)
            page.set_weight(DT_weight)
            page.expand_expander(page.wireless_expander)
            page.set_wireless(DT_wireless)
            page.expand_expander(page.color_expander)
            page.set_color(DT_color)
            if self.driver.responsive_mobile:
                page.scroll_to_bottom()
            reporter[testID].reportEvent("Entered selection options", False)
            page.wait_for_item_display_update()
            if DT_expected_items == page.get_num_items():
                reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Correct number of items shown", True, "Items found: " + str(DT_expected_items), screenshotCallback=driver.save_screenshot)
            else:
                reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Incorrect number of items shown", False, "Items found: " + str(page.get_num_items()),screenshotCallback=driver.save_screenshot)
            page.clear_selection()

    def test_TH_TC002(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC002 [Non-responsive]***")
        self.driver.testID = "TC002_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC002", "Test Laptops page options using excel data [Non-responsive]")
        self.TH_TC002()

    def test_TH_TC002_responsive_mobile(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC002 [Responsive-mobile]***")
        self.driver.testID = "TC002_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC002_RM", "Test Laptops page options using excel data [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC002()
    
    def test_TH_TC002_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC002 [Responsive-tablet]***")
        self.driver.testID = "TC002_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC002_RT", "Test Laptops page options using excel data [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC002()

    def TH_TC002(self):
        driver = self.driver
        reporter = self.reporter
        testID = self.driver.testID
        log_wrapper(self.driver, 'Entered TH_TC002 main test logic')
        page = HomePage(driver)
        page.check_responsive()
        page.click_laptops()
        page = LaptopsPage(driver)
        objExcel = excelReader("./AOBrowseStore.xlsx", 1)
        rowNum = 1 #for keeping track of datarow for reporting
        for dataRow in objExcel:
            rowNum += 1
            DT_price = float(dataRow["DT_price"])
            DT_display = dataRow["DT_display"]
            DT_os = dataRow["DT_os"]
            DT_processor = dataRow["DT_processor"]
            DT_weight = dataRow["DT_weight"]
            DT_color = dataRow["DT_color"]
            DT_expected_items = int(dataRow["DT_expected_items"])

            dataString = "Price = " + str(DT_price) + \
                "<br>Display option = " + DT_display + \
                "<br>OS option = " + DT_os + \
                "<br>Processor option = " + DT_processor + \
                "<br>Weight option = " + DT_weight + \
                "<br>Color option = " + DT_color
            log_wrapper(self.driver, "Loaded test values from excel")

            reporter[testID].reportEvent("Load row #" + str(rowNum) + " values from datasheet", False, dataString)

            if self.driver.responsive_mobile:
                page.open_responsive_filter()

            page.expand_expander(page.price_expander)
            page.set_price(DT_price)
            page.expand_expander(page.display_expander)
            page.set_display(DT_display)
            page.expand_expander(page.os_expander)
            page.set_os(DT_os)
            page.expand_expander(page.processor_expander)
            page.set_processor(DT_processor)
            page.expand_expander(page.weight_expander)
            page.set_weight(DT_weight)
            page.expand_expander(page.color_expander)
            page.set_color(DT_color)
            if self.driver.responsive_mobile:
                page.scroll_to_bottom()
            reporter[testID].reportEvent("Entered selection options", False)
            page.wait_for_item_display_update()
            if DT_expected_items == page.get_num_items():
                reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Correct number of items shown", True, "Items found: " + str(DT_expected_items), screenshotCallback=driver.save_screenshot)
                log_wrapper(self.driver, 'STEP SUCCESS')
            else:
                reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Incorrect number of items shown", False, "Items found: " + str(page.get_num_items()),screenshotCallback=driver.save_screenshot)
                log_wrapper(self.driver, 'STEP FAILURE')
            page.clear_selection()

    def test_TH_TC003(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC003 [Non-responsive]***")
        self.driver.testID = "TC003_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC003", "Test Tablets page options using excel data [Non-responsive]")
        self.TH_TC003()

    def test_TH_TC003_responsive_mobile(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC003 [Responsive-mobile]***")
        self.driver.testID = "TC003_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC003_RM", "Test Tablets page options using excel data [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC003()

    def test_TH_TC003_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC003 [Responsive-tablet]***")
        self.driver.testID = "TC003_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC003_RT", "Test Tablets page options using excel data [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC003()

    def TH_TC003(self):
        driver = self.driver
        reporter = self.reporter
        testID = self.driver.testID
        log_wrapper(self.driver, 'Entered TH_TC003 main test logic')

        page = HomePage(driver)
        page.check_responsive()
        page.click_tablets()
        page = TabletsPage(driver)
        objExcel = excelReader("./AOBrowseStore.xlsx", 2)
        rowNum = 1 #for keeping track of datarow for reporting
        for dataRow in objExcel:
            rowNum += 1
            DT_price = float(dataRow["DT_price"])
            DT_display = str(dataRow["DT_display"])
            DT_processor = str(dataRow["DT_processor"])
            DT_color = dataRow["DT_color"]
            DT_expected_items = int(dataRow["DT_expected_items"])

            dataString = "Price = " + str(DT_price) + \
                "<br>Display option = " + DT_display + \
                "<br>Manufacturer option = " + DT_processor + \
                "<br>Color option = " + DT_color 
            log_wrapper(self.driver, "Loaded test values form excel sheet")
            reporter[testID].reportEvent("Load row #" + str(rowNum) + " values from datasheet", False, dataString)

            if self.driver.responsive_mobile:
                page.open_responsive_filter()

            page.expand_expander(page.price_expander)
            page.set_price(DT_price)
            page.expand_expander(page.display_expander)
            page.set_display(DT_display)
            page.expand_expander(page.processor_expander)
            page.set_processor(DT_processor)
            page.expand_expander(page.color_expander)
            page.set_color(DT_color)
            if self.driver.responsive_mobile:
                page.scroll_to_bottom()
            reporter[testID].reportEvent("Entered selection options", False)
            page.wait_for_item_display_update()
            if DT_expected_items == page.get_num_items():
                reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Correct number of items shown", True, "Items found: " + str(DT_expected_items), screenshotCallback=driver.save_screenshot)
                log_wrapper(self.driver, "STEP SUCCESS")
            else:
                reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Incorrect number of items shown", False, "Items found: " + str(page.get_num_items()),screenshotCallback=driver.save_screenshot)
                log_wrapper(self.driver, "STEP FAILURE")
            page.clear_selection()

    def test_TH_TC004(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC004 [Non-responsive]***")
        self.driver.testID = "TC004_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC004", "Test Mice page options using excel data [Non-responsive]")
        self.TH_TC004()

    def test_TH_TC004_responsive_mobile(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC004 [Responsive-mobile]***")
        self.driver.testID = "TC004_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC004_RM", "Test Mice page options using excel data [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC004()

    def test_TH_TC004_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC004 [Responsive-tablet]***")
        self.driver.testID = "TC004_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC004_RT", "Test Mice page options using excel data [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC004()

    def TH_TC004(self):
        driver = self.driver
        reporter = self.reporter
        testID = self.driver.testID
        log_wrapper(self.driver, 'Entered TH_TC004 main test logic')
        page = HomePage(driver)
        page.check_responsive()
        page.click_mice()
        page = MicePage(driver)
        objExcel = excelReader("./AOBrowseStore.xlsx", 3)
        rowNum = 1 #for keeping track of datarow for reporting
        for dataRow in objExcel:
            rowNum += 1
            DT_price = float(dataRow["DT_price"])
            DT_scroller = str(dataRow["DT_scroller"])
            DT_color = dataRow["DT_color"]
            DT_expected_items = int(dataRow["DT_expected_items"])

            dataString = "Price = " + str(DT_price) + \
                "<br>Scroller option = " + DT_scroller + \
                "<br>Color option = " + DT_color 

            log_wrapper(self.driver, "Loaded test values from excel")
            reporter[testID].reportEvent("Load row #" + str(rowNum) + " values from datasheet", False, dataString)

            if self.driver.responsive_mobile:
                page.open_responsive_filter()

            page.expand_expander(page.price_expander)
            page.set_price(DT_price)
            page.expand_expander(page.scroller_expander)
            page.set_scroller(DT_scroller)
            page.expand_expander(page.color_expander)
            page.set_color(DT_color)
            if self.driver.responsive_mobile:
                page.scroll_to_bottom()
            reporter[testID].reportEvent("Entered selection options", False)
            page.wait_for_item_display_update()
            if DT_expected_items == page.get_num_items():
                reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Correct number of items shown", True, "Items found: " + str(DT_expected_items), screenshotCallback=driver.save_screenshot)
                log_wrapper(self.driver, "STEP SUCCESS")
            else:
                reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Incorrect number of items shown", False, "Items found: " + str(page.get_num_items()),screenshotCallback=driver.save_screenshot)
                log_wrapper(self.driver, "STEP FAILURE")
            page.clear_selection()

    def test_TH_TC005(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC005 [Non-responsive]***")
        self.driver.testID = "TC005_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC005", "Test Headphones page options using excel data [Non-responsive]")
        self.TH_TC005()

    def test_TH_TC005_responsive_mobile(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC005 [Responsive-mobile]***")
        self.driver.testID = "TC005_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC005_RM", "Test Headphones page options using excel data [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC005()

    def test_TH_TC005_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC005 [Responsive-tablet]***")
        self.driver.testID = "TC005_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC005_RT", "Test Headphones page options using excel data [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC005()

    def TH_TC005(self):
        driver = self.driver
        reporter = self.reporter
        testID = self.driver.testID
        log_wrapper(self.driver, 'Entered TH_TC005 main test logic')
        page = HomePage(driver)
        page.check_responsive()
        page.click_headphones()
        page = HeadphonesPage(driver)
        objExcel = excelReader("./AOBrowseStore.xlsx", 4)
        rowNum = 1 #for keeping track of datarow for reporting

        for dataRow in objExcel:
            rowNum += 1
            DT_price = float(dataRow["DT_price"])
            DT_compat = dataRow["DT_compat"]
            DT_connector = dataRow["DT_connector"]
            DT_weight =dataRow["DT_weight"]
            DT_color = dataRow["DT_color"]
            DT_expected_items = int(dataRow["DT_expected_items"])

            dataString = "Price = " + str(DT_price) + \
                "<br>Compatability option = " + DT_compat + \
                "<br>Conector option = " + DT_connector + \
                "<br>Weight option = " + DT_weight + \
                "<br>Color option = " + DT_color
            log_wrapper(self.driver, "Loaded test values from excel")
            
            reporter[testID].reportEvent("Load row #" + str(rowNum) + " values from datasheet", False, dataString)


            if self.driver.responsive_mobile:
                page.open_responsive_filter()
            page.expand_expander(page.price_expander)
            page.set_price(DT_price)
            page.expand_expander(page.compatibility_expander)
            page.set_compat(DT_compat)
            page.expand_expander(page.connector_expander)
            page.set_connector(DT_connector)
            page.expand_expander(page.weight_expander)
            page.set_weight(DT_weight)
            page.expand_expander(page.color_expander)
            page.set_color(DT_color)
            if self.driver.responsive_mobile:
                page.scroll_to_bottom()
            reporter[testID].reportEvent("Entered selection options", False)
            page.wait_for_item_display_update()
            if DT_expected_items == page.get_num_items():
                reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Correct number of items shown", True, "Items found: " + str(DT_expected_items), screenshotCallback=driver.save_screenshot)
                log_wrapper(self.driver, "STEP SUCCESS")
            else:
                reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Incorrect number of items shown", False, "Items found: " + str(page.get_num_items()),screenshotCallback=driver.save_screenshot)
                log_wrapper(self.driver, "STEP FAILURE")
            page.clear_selection()

    #test multiple items
    def test_TH_TC006(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC006 [Non-responsive]***")
        self.driver.testID = "TC006_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC006", "Test Speakers page options using excel data with multiple selections [Non-responsive]")
        self.TH_TC006()

    def test_TH_TC006_responsive_mobile(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC006 [Responsive-mobile]***")
        self.driver.testID = "TC006_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC006_RM", "Test Speakers page options using excel data with multiple selections [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC006()

    def test_TH_TC006_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC006 [Responsive-tablet]***")
        self.driver.testID = "TC006_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC006_RT", "Test Speakers page options using excel data with multiple selections [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC006()

    def TH_TC006(self):
        driver = self.driver
        reporter = self.reporter
        testID = self.driver.testID

        log_wrapper(self.driver, 'Entered TH_TC006 main test logic')
           
        page = HomePage(driver)
        page.check_responsive()
        page.click_speakers()
        page = SpeakersPage(driver)
        objExcel = excelReader("./AOBrowseStore.xlsx", 5)
        rowNum = 1 #for keeping track of datarow for reporting
        expected_items = 0

        for dataRow in objExcel:
            rowNum += 1
            DT_compat = dataRow["DT_compat"]
            DT_manufacturer = dataRow["DT_manufacturer"]
            DT_weight =dataRow["DT_weight"]
            DT_wireless = dataRow["DT_wireless"]
            DT_color = dataRow["DT_color"]
            expected_items += int(dataRow["DT_expected_items"])

            dataString = "Compatability option = " + DT_compat + \
                "<br>Manufacturer option = " + DT_manufacturer + \
                "<br>Weight option = " + DT_weight + \
                "<br>Wireless option = " + DT_wireless + \
                "<br>Color option = " + DT_color

            log_wrapper(self.driver, 'Loaded test values from excel')
            reporter[testID].reportEvent("Load row #" + str(rowNum) + " values from datasheet", False, dataString)

            if self.driver.responsive_mobile:
                page.open_responsive_filter()

            page.expand_expander(page.compat_expander)
            page.set_compat(DT_compat)
            page.close_expander(page.compat_expander)

            page.expand_expander(page.manufacturer_expander)
            page.set_manufacturer(DT_manufacturer)
            page.close_expander(page.manufacturer_expander)

            page.expand_expander(page.weight_expander)
            page.set_weight(DT_weight)
            page.close_expander(page.weight_expander)

            page.expand_expander(page.wireless_expander)
            page.set_wireless(DT_wireless)
            page.close_expander(page.wireless_expander)

            page.expand_expander(page.color_expander)
            page.set_color(DT_color)
            page.close_expander(page.color_expander)

            if self.driver.responsive_mobile:
                page.scroll_to_bottom()
            reporter[testID].reportEvent("Entered selection options", False)
            page.wait_for_item_display_update()
            self.driver.execute_script("window.scrollTo(0,0)")
        if expected_items == page.get_num_items():
            reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Correct number of items shown", True, "Items found: " + str(expected_items), screenshotCallback=driver.save_screenshot)
            log_wrapper(self.driver, "STEP SUCCESS")
        else:
            reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Incorrect number of items shown", False, "Items found: " + str(page.get_num_items()),screenshotCallback=driver.save_screenshot)
            log_wrapper(self.driver, "STEP FAILURE")

    def test_TH_TC007(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC007 [Non-responsive]***")
        self.driver.testID = "TC007_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC007", "Test Laptops page options using excel data with multiple selections [Non-responsive]")
        self.TH_TC007()

    def test_TH_TC007_responsive_mobile(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC007 [Responsive-mobile]***")
        self.driver.testID = "TC007_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC007_RM", "Test Laptops page options using excel data with multiple selections [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC007()

    def test_TH_TC007_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC007 [Responsive-tablet]***")
        self.driver.testID = "TC007_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC007_RT", "Test Laptops page options using excel data with multiple selections [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC007()
  
    def TH_TC007(self):
        driver = self.driver
        reporter = self.reporter
        testID = self.driver.testID
        log_wrapper(self.driver, 'Entered TH_TC007 main test logic')
        page = HomePage(driver)

        page.check_responsive()

        page.click_laptops()
        page = LaptopsPage(driver)
        objExcel = excelReader("./AOBrowseStore.xlsx", 6)
        rowNum = 1 #for keeping track of datarow for reporting
        expected_items = 0
        for dataRow in objExcel:
            rowNum += 1
            DT_display = dataRow["DT_display"]
            DT_os = dataRow["DT_os"]
            DT_processor = dataRow["DT_processor"]
            DT_weight = str(dataRow["DT_weight"])
            DT_color = dataRow["DT_color"]
            expected_items += int(dataRow["DT_expected_items"])

            dataString = "Display option = " + DT_display + \
                "<br>OS option = " + DT_os + \
                "<br>Processor option = " + DT_processor + \
                "<br>Weight option = " + DT_weight + \
                "<br>Color option = " + DT_color

            log_wrapper(self.driver, 'Loaded test values from excel')
            reporter[testID].reportEvent("Load row #" + str(rowNum) + " values from datasheet", False, dataString)

            if self.driver.responsive_mobile:
                page.open_responsive_filter()
                
            page.expand_expander(page.display_expander)
            page.set_display(DT_display)
            page.close_expander(page.display_expander)

            page.expand_expander(page.os_expander)
            page.set_os(DT_os)
            page.close_expander(page.os_expander)

            page.expand_expander(page.processor_expander)
            page.set_processor(DT_processor)
            page.close_expander(page.processor_expander)

            page.expand_expander(page.weight_expander)
            page.set_weight(DT_weight)
            page.close_expander(page.weight_expander)

            page.expand_expander(page.color_expander)
            page.set_color(DT_color)
            page.close_expander(page.color_expander)

            if self.driver.responsive_mobile:
                page.scroll_to_bottom()
            reporter[testID].reportEvent("Entered selection options", False)
            page.wait_for_item_display_update()
            self.driver.execute_script("window.scrollTo(0,0)")
        if expected_items == page.get_num_items():
            reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Correct number of items shown", True, "Items found: " + str(expected_items), screenshotCallback=driver.save_screenshot)
            log_wrapper(self.driver, 'STEP SUCCESS')
        else:
            reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Incorrect number of items shown", False, "Items found: " + str(page.get_num_items()),screenshotCallback=driver.save_screenshot)
            log_wrapper(self.driver, 'STEP FAILURE')


    def test_TH_TC008(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC008 [Non-responsive]***")
        self.driver.testID = "TC008_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC008", "Test Tablets page options using excel data with multiple selections [Non-responsive]")
        self.TH_TC008()

    def test_TH_TC008_responsive_mobile(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC008 [Responsive-mobile]***")
        self.driver.testID = "TC008_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC008_RM", "Test Tablets page options using excel data with multiple selections [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC008()

    def test_TH_TC008_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC008 [Responsive-tablet]***")
        self.driver.testID = "TC008_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC008_RT", "Test Tablets page options using excel data with multiple selections [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC008()

    def TH_TC008(self):
        driver = self.driver
        reporter = self.reporter
        testID = self.driver.testID
        log_wrapper(self.driver, 'Entered TH_TC008 main logic')

        page = HomePage(driver)

        page.check_responsive()

        page.click_tablets()
        page = TabletsPage(driver)
        objExcel = excelReader("./AOBrowseStore.xlsx", 7)
        rowNum = 1 #for keeping track of datarow for reporting
        expected_items = 0
        for dataRow in objExcel:
            rowNum += 1
            DT_display = str(dataRow["DT_display"]).strip()
            DT_processor = str(dataRow["DT_processor"])
            DT_color = dataRow["DT_color"].strip()
            expected_items += int(dataRow["DT_expected_items"])

            dataString = "Display option = " + DT_display + \
                "<br>Manufacturer option = " + DT_processor + \
                "<br>Color option = " + DT_color 
            
            log_wrapper(self.driver, 'Loaded test values from excel')
            reporter[testID].reportEvent("Load row #" + str(rowNum) + " values from datasheet", False, dataString)
            if self.driver.responsive_mobile:
                page.open_responsive_filter()
            page.expand_expander(page.display_expander)
            page.set_display(DT_display)
            page.close_expander(page.display_expander)

            page.expand_expander(page.processor_expander)
            page.set_processor(DT_processor)
            page.close_expander(page.processor_expander)

            page.expand_expander(page.color_expander)
            page.set_color(DT_color)
            page.close_expander(page.color_expander)

            if self.driver.responsive_mobile:
                page.scroll_to_bottom()
            reporter[testID].reportEvent("Entered selection options", False)
            page.wait_for_item_display_update()
            self.driver.execute_script("window.scrollTo(0,0)")
        if expected_items == page.get_num_items():
            reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Correct number of items shown", True, "Items found: " + str(expected_items), screenshotCallback=driver.save_screenshot)
            log_wrapper(self.driver, "STEP SUCCESS")
        else:
            reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Incorrect number of items shown", False, "Items found: " + str(page.get_num_items()),screenshotCallback=driver.save_screenshot)
            log_wrapper(self.driver, "STEP FAILURE")

        
    def test_TH_TC009(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC009 [Non-responsive]***")
        self.driver.testID = "TC009_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC009", "Test Mice page options using excel data with multiple selections [Non-responsive]")
        self.TH_TC009()

    def test_TH_TC009_responsive_mobile(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC009 [Responsive-mobile]***")
        self.driver.testID = "TC009_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC009_RM", "Test Mice page options using excel data with multiple selections [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC009()

    def test_TH_TC009_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC009 [Responsive-tablet]***")
        self.driver.testID = "TC009_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC009_RT", "Test Mice page options using excel data with multiple selections [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC009()

    def TH_TC009(self):
        driver = self.driver
        reporter = self.reporter
        testID = self.driver.testID
        log_wrapper(self.driver, 'Entered TH_TC009 main test logic')

        page = HomePage(driver)

        page.check_responsive()

        page.click_mice()
        page = MicePage(driver)
        objExcel = excelReader("./AOBrowseStore.xlsx", 8)
        rowNum = 1 #for keeping track of datarow for reporting
        expected_items = 0
        for dataRow in objExcel:
            rowNum += 1
            DT_scroller = str(dataRow["DT_scroller"])
            DT_color = dataRow["DT_color"]
            expected_items += int(dataRow["DT_expected_items"])

            dataString = "Scroller option = " + DT_scroller + \
                "<br>Color option = " + DT_color 
            reporter[testID].reportEvent("Load row #" + str(rowNum) + " values from datasheet", False, dataString)
            log_wrapper(self.driver, 'Loaded test values from excel')

            if self.driver.responsive_mobile:
                page.open_responsive_filter()

            page.expand_expander(page.scroller_expander)
            page.set_scroller(DT_scroller)
            page.close_expander(page.scroller_expander)

            page.expand_expander(page.color_expander)
            page.set_color(DT_color)
            page.close_expander(page.color_expander)

            if self.driver.responsive_mobile:
                page.scroll_to_bottom()
            reporter[testID].reportEvent("Entered selection options", False)
            page.wait_for_item_display_update()
            self.driver.execute_script("window.scrollTo(0,0)")
        if expected_items == page.get_num_items():
            reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Correct number of items shown", True, "Items found: " + str(expected_items), screenshotCallback=driver.save_screenshot)
            log_wrapper(self.driver, "STEP SUCCESS")
        else:
            reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Incorrect number of items shown", False, "Items found: " + str(page.get_num_items()),screenshotCallback=driver.save_screenshot)
            logging.getLogger(driver.logginID).info("STEP FAILURE")

    def test_TH_TC010(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC010 [Non-responsive]***")
        self.driver.testID = "TC010_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC010", "Test Headphones page options using excel data with multiple selections [Non-responsive]")
        self.TH_TC010()

    def test_TH_TC010_responsive_mobile(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC010 [Responsive-mobile]***")
        self.driver.testID = "TC010_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC010_RM", "Test Headphones page options using excel data with multiple selections [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC010()

    def test_TH_TC010_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC010 [Responsive-tablet]***")
        self.driver.testID = "TC010_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC010_RT", "Test Headphones page options using excel data with multiple selections [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC010()

    def TH_TC010(self):
        driver = self.driver
        reporter = self.reporter
        testID = self.driver.testID
        log_wrapper(self.driver, 'Entered TH_TC010 main test logic')

        page = HomePage(driver)

        page.check_responsive()

        page.click_headphones()
        page = HeadphonesPage(driver)
        objExcel = excelReader("./AOBrowseStore.xlsx", 9)
        rowNum = 1 #for keeping track of datarow for reporting
        expected_items = 0
        for dataRow in objExcel:
            rowNum += 1
            DT_compat = dataRow["DT_compat"]
            DT_connector = dataRow["DT_connector"]
            DT_weight =dataRow["DT_weight"]
            DT_color = dataRow["DT_color"]
            expected_items += int(dataRow["DT_expected_items"])

            dataString = "Compatability option = " + DT_compat + \
                "<br>Conector option = " + DT_connector + \
                "<br>Weight option = " + DT_weight + \
                "<br>Color option = " + DT_color
            log_wrapper(self.driver, 'Loaded test values from excel')
            reporter[testID].reportEvent("Load row #" + str(rowNum) + " values from datasheet", False, dataString)

            if self.driver.responsive_mobile:
                page.open_responsive_filter()

            page.expand_expander(page.compatibility_expander)
            page.set_compat(DT_compat)
            page.close_expander(page.compatibility_expander)

            page.expand_expander(page.connector_expander)
            page.set_connector(DT_connector)
            page.close_expander(page.connector_expander)

            page.expand_expander(page.weight_expander)
            page.set_weight(DT_weight)
            page.close_expander(page.weight_expander)

            page.expand_expander(page.color_expander)
            page.set_color(DT_color)
            page.close_expander(page.color_expander)

            if self.driver.responsive_mobile:
                page.scroll_to_bottom()
            reporter[testID].reportEvent("Entered selection options", False)
            page.wait_for_item_display_update()
            self.driver.execute_script("window.scrollTo(0,0)")
        if expected_items == page.get_num_items():
            reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Correct number of items shown", True, "Items found: " + str(expected_items), screenshotCallback=driver.save_screenshot)
            log_wrapper(self.driver, 'STEP SUCCESS')
        else:
            reporter[testID].reportStep("Check that results return expected number of items", "Correct number of items shown", "Incorrect number of items shown", False, "Items found: " + str(page.get_num_items()),screenshotCallback=driver.save_screenshot)
            log_wrapper(self.driver, 'STEP FAILURE')

    #test item pages
    def test_TH_TC011(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC011 [Non-responsive]***")
        self.driver.testID = "TC011_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC011", "Test viewing items based on excel input [Non-responsive]")
        self.TH_TC011()

    def test_TH_TC011_responsive_mobile(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC011 [Responsive-mobile]***")
        self.driver.testID = "TC011_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC011_RM", "Test viewing items based on excel input [Responsive-mobile]")
        self.driver.set_window_size(360, 900)
        self.TH_TC011()

    def test_TH_TC011_responsive_tablet(self):
        log_wrapper(self.driver, "***BEGINNING TH_TC011 [Responsive-tablet]***")
        self.driver.testID = "TC011_" + str(random.getrandbits(64))
        self.reporter.addTestCase(self.driver.testID, "TH_TC011_RT", "Test viewing items based on excel input [Responsive-tablet]")
        self.driver.set_window_size(768, 900)
        self.TH_TC011()

    def TH_TC011(self):
        driver = self.driver
        reporter = self.reporter
        testID = self.driver.testID
        log_wrapper(self.driver, 'Entered TH_TC011 main test logic')

        page = HomePage(driver)

        page.check_responsive()
           
        objExcel = excelReader("./AOBrowseStore.xlsx", 10)
        rowNum = 1 #for keeping track of datarow for reporting
        for dataRow in objExcel:
            rowNum += 1
            DT_category = dataRow["DT_category"]
            DT_item = dataRow["DT_item"]

            dataString = "Category option = " + DT_category + \
                "<br>Item option (#) = " + DT_item

            log_wrapper(self.driver, 'Loaded values form excel')
            reporter[testID].reportEvent("Loaded row #" + str(rowNum) + " values from datasheet", False, dataString)
            page = page.click_category_excel(DT_category)
            itemName = page.get_prod_name(DT_item)
            itemPrice = page.get_prod_price(DT_item)
            page.click_ith_item(DT_item)
            page = ItemPage(driver)
            dataString = "Item # = " + str(DT_item) + \
                "<br>Displayed item name = " + itemName + \
                "<br>Displayed item price = " + itemPrice
            reporter[testID].reportEvent("Clicked item", False, dataString)

            if itemName == page.get_prod_name():
                reporter[testID].reportStep("Check that item page descriptin matches store page description", "Description matches", "Description matches", True, "", screenshotCallback=driver.save_screenshot)
                log_wrapper(self.driver, 'STEP SUCCESS')
            else:
                dataString = "Store page description = " + itemName + \
                    "<br>Item page description = " + page.get_prod_name() 
                reporter[testID].reportStep("Check that item page description matches store page description", "Description matches", "Description doesn't match", False, dataString, screenshotCallback=driver.save_screenshot)
                log_wrapper(self.driver, 'STEP FAILURE')
            if itemPrice == page.get_prod_price():
                reporter[testID].reportStep("Check that item page price matches store page price", "Price matches", "Price matches", True, "", screenshotCallback=driver.save_screenshot)
                log_wrapper(self.driver, 'STEP SUCCESS')
            else:
                dataString = "Store page price = " + itemPrice + \
                    "<br>Item page description = " + page.get_prod_price()
                reporter[testID].reportStep("Check that item page price matches store page price", "Price matches", "Price doesn't match", False, dataString, screenshotCallback=driver.save_screenshot)
                log_wrapper(self.driver, 'STEP FAILURE')
            driver.get('https://www.advantageonlineshopping.com/#/')
            page = HomePage(driver)

                
if __name__ == "__main__":
    unittest.main()