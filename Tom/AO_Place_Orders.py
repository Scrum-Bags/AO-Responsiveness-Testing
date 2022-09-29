from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, random
import unittest

#import sys
#sys.path.append("D:\Documents\Selenium\Shared")

from TestSuiteReporter import TestSuiteReporter
from ExcelReader import excelReader
from AO_POMs import *

class AO_Place_Orders(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(AO_Place_Orders, self).__init__(*args, **kwargs)
        self.timestr = time.strftime("%Y-%m-%d--%I_%M_%S%p")
        self.reporter = TestSuiteReporter(self.timestr, "./", "Tom")

    @classmethod
    def setUpClass(cls):
        cls.edge_options = Options()
        cls.edge_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        cls.driver = webdriver.Edge(options=cls.edge_options)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def setUp(self): 
        self.driver.get("https://www.advantageonlineshopping.com/#/")
        BasePage.wait_for_element(self, HomePageLocators.By_speakers_link) 

    def test_TH_TC012(self):
        driver = self.driver
        reporter = self.reporter
        testID = "TC012_" + str(random.getrandbits(64))
        reporter.addTestCase(testID, "TH_TC012", "Add single item to cart and checkout")
        page = HomePage(driver)
        objExcel = excelReader("D:\Documents\Selenium\Tom\AdvantageOnline\AOPlaceOrder.xlsx", 0)
        rowNum = 1
        for dataRow in objExcel:
            DT_email = dataRow["DT_email"]
            DT_password = dataRow["DT_password"]
            DT_category = dataRow["DT_category"]
            DT_item = dataRow["DT_item"]
            DT_color = dataRow["DT_color"]
            DT_quantity = dataRow["DT_quantity"]
            DT_payment_method = dataRow["DT_payment_method"]

            dataString = "Username = " + DT_email + \
                "<br>Password = " + DT_password + \
                "<br>Category = " + DT_category + \
                "<br>Item # = " + DT_item + \
                "<br>Color = " + DT_color + \
                "<br>Quantity = " + DT_quantity + \
                "<br>Payment Method = " + DT_payment_method
            rowNum += 1 #for keeping track of datarow for reporting
            reporter[testID].reportEvent("Load row #" + str(rowNum) + " values from datasheet", False, dataString, screenshotCallback=driver.save_screenshot) 
            
            page.login(DT_email, DT_password) #excel
            reporter[testID].reportEvent("Logged in", False, "User = " + DT_email + " Pass = " + DT_password, screenshotCallback=driver.save_screenshot)

            page = page.click_category_excel(DT_category) #excel
            reporter[testID].reportEvent("Clicked category", False, "Category = " + DT_category, screenshotCallback=driver.save_screenshot)

            page.click_ith_item(DT_item) #excel
            page = ItemPage(driver)
            reporter[testID].reportEvent("Clicked item", False, "Item num = " + DT_item, screenshotCallback=driver.save_screenshot)

            page.set_color(DT_color) #excel
            reporter[testID].reportEvent("Set color", False, "Color = " + DT_color, screenshotCallback=driver.save_screenshot)

            page.set_quantity(int(DT_quantity)) #excel
            reporter[testID].reportEvent("Set quantity", False, "Quantity = " + DT_quantity, screenshotCallback=driver.save_screenshot)

            #page.add_to_cart.click()
            #reporter[testID].reportEvent("Added item to cart", False, screenshotCallback=driver.save_screenshot)
            if page.click_add_cart():
                reporter[testID].reportStep("Add item to cart", "Item added to cart", "Item added to cart", True, "", screenshotCallback=driver.save_screenshot)
            else:
                reporter[testID].reportStep("Add item to cart", "Item added to cart", "Item couldn't be added to cart", False, "", screenshotCallback=driver.save_screenshot)
                continue

            page.click_shopping_cart()
            page = ShoppingCartPage(driver)
            if page.click_checkout():
                reporter[testID].reportStep("Attempt to click checkout button", "Checkout button clicked", "Checkout button clicked", True, "", screenshotCallback=driver.save_screenshot)
            else:
                reporter[testID].reportStep("Attempt to click checkout button", "Checkout button clicked", "Checkout button not clickable", False, "", screenshotCallback=driver.save_screenshot)
                driver.get('https://www.advantageonlineshopping.com/#/')
                page = HomePage(driver)
                continue
            page = OrderPaymentPage_1(driver)
            page.click_next()
            page = OrderPaymentPage_2(driver)
            reporter[testID].reportEvent("Navigated to payment method", False, screenshotCallback=driver.save_screenshot)

            time.sleep(2)
            page.choose_payment(DT_payment_method)
            page = OrderConfirmationPage(driver)
            reporter[testID].reportEvent("Selected payment method", False, "Method = " + DT_payment_method, screenshotCallback=driver.save_screenshot)

            ordernum = page.get_order_num()
            reporter[testID].reportEvent("Retrieved order number", False, "Order number = " + ordernum, screenshotCallback=driver.save_screenshot)

            page.click_order_history()
            page = OrderHistoryPage(driver)
            if page.check_order_num(ordernum):
                reporter[testID].reportStep("Check that order number is found in order history", "Order number found", "Order number found", True, screenshotCallback=driver.save_screenshot)
            else:
                reporter[testID].reportStep("Check that order number is found in order history", "Order number found", "Order number not found", False, screenshotCallback=driver.save_screenshot)

            driver.get('https://www.advantageonlineshopping.com/#/')
            page = HomePage(driver)

    def test_TH_TC013(self):
        driver = self.driver
        reporter = self.reporter
        testID = "TC013_" + str(random.getrandbits(64))
        reporter.addTestCase(testID, "TH_TC012", "Add multiple items to cart and checkout")
        page = HomePage(driver)
        objExcel = excelReader("D:\Documents\Selenium\Tom\AdvantageOnline\AOPlaceOrder.xlsx", 1)
        rowNum = 1
        for dataRow in objExcel:
            DT_email = dataRow["DT_email"]
            DT_password = dataRow["DT_password"]
            DT_category = dataRow["DT_category"]
            DT_item = dataRow["DT_item"]
            DT_color = dataRow["DT_color"]
            DT_quantity = dataRow["DT_quantity"]

            dataString = "Username = " + DT_email + \
                "<br>Password = " + DT_password + \
                "<br>Category = " + DT_category + \
                "<br>Item # = " + DT_item + \
                "<br>Color = " + DT_color + \
                "<br>Quantity = " + DT_quantity 

            rowNum += 1 #for keeping track of datarow for reporting
            reporter[testID].reportEvent("Load row #" + str(rowNum) + " values from datasheet", False, dataString, screenshotCallback=driver.save_screenshot) 
            
            page.login(DT_email, DT_password) #excel
            reporter[testID].reportEvent("Logged in", False, "User = " + DT_email + " Pass = " + DT_password, screenshotCallback=driver.save_screenshot)

            page = page.click_category_excel(DT_category) #excel
            reporter[testID].reportEvent("Clicked category", False, "Category = " + DT_category, screenshotCallback=driver.save_screenshot)

            page.click_ith_item(DT_item) #excel
            page = ItemPage(driver)
            reporter[testID].reportEvent("Clicked item", False, "Item num = " + DT_item, screenshotCallback=driver.save_screenshot)

            page.set_color(DT_color) #excel
            reporter[testID].reportEvent("Set color", False, "Color = " + DT_color, screenshotCallback=driver.save_screenshot)

            page.set_quantity(int(DT_quantity)) #excel
            reporter[testID].reportEvent("Set quantity", False, "Quantity = " + DT_quantity, screenshotCallback=driver.save_screenshot)

            if page.click_add_cart():
            #page.add_to_cart.click()
                reporter[testID].reportStep("Add item to cart", "Item added to cart", "Item added to cart", True, "", screenshotCallback=driver.save_screenshot)
            else:
                reporter[testID].reportStep("Add item to cart", "Item added to cart", "Item couldn't be added to cart", False, "", screenshotCallback=driver.save_screenshot)
            
            driver.get('https://www.advantageonlineshopping.com/#/')
            page = HomePage(driver)

        page.click_shopping_cart()
        page = ShoppingCartPage(driver)
        if page.click_checkout():
            reporter[testID].reportStep("Attempt to click checkout button", "Checkout button clicked", "Checkout button clicked", True, "", screenshotCallback=driver.save_screenshot)
        else:
            reporter[testID].reportStep("Attempt to click checkout button", "Checkout button clicked", "Checkout button not clickable", False, "", screenshotCallback=driver.save_screenshot)
        page = OrderPaymentPage_1(driver)
        page.click_next()
        page = OrderPaymentPage_2(driver)
        reporter[testID].reportEvent("Navigated to payment method", False, screenshotCallback=driver.save_screenshot)

        time.sleep(2)
        page.choose_payment("SAFEPAY")
        page = OrderConfirmationPage(driver)
        reporter[testID].reportEvent("Selected payment method", False, "Method = SAFEPAY", screenshotCallback=driver.save_screenshot)

        ordernum = page.get_order_num()
        reporter[testID].reportEvent("Retrieved order number", False, "Order number = " + ordernum, screenshotCallback=driver.save_screenshot)

        page.click_order_history()
        page = OrderHistoryPage(driver)
        if page.check_order_num(ordernum):
            reporter[testID].reportStep("Check that order number is found in order history", "Order number found", "Order number found", True, screenshotCallback=driver.save_screenshot)
        else:
            reporter[testID].reportStep("Check that order number is found in order history", "Order number found", "Order number not found", False, screenshotCallback=driver.save_screenshot)


if __name__ == "__main__":
    unittest.main()