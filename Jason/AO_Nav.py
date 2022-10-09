from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from AO_Locators import AO_Nav_Objects
from AO_Locators import AO_Login_Objects
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import random
import string
import time

#https://selenium-python.readthedocs.io/getting-started.html#simple-usage

class AO_Nav():


    def __init__(self, driver = "default"):

        if(driver=="default"):
            self.driver = webdriver.Chrome()
        else:
            self.driver = driver

    def MobileCheck(self):
        #print(self.driver.find_element(*AO_Login_Objects.By_login_menu).size["height"])
        return not self.driver.find_element(*AO_Login_Objects.By_login_menu).size["height"] > 0

    def GoTo_Account(self, reporter, ssPath):
        driver = self.driver
        mobile = self.MobileCheck()
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((AO_Login_Objects.By_login_field)))
        if mobile:
            #print(len(driver.find_elements(*AO_Login_Objects.By_mobile_dropdown)))
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((AO_Nav_Objects.By_mobile_dropdown)))
            driver.find_element(*AO_Login_Objects.By_mobile_dropdown).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Nav_Objects.By_user_menu_m)))
            driver.find_element(*AO_Nav_Objects.By_user_menu_m).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Nav_Objects.By_account_link_m)))
            driver.find_element(*AO_Nav_Objects.By_account_link_m).click()
        else:
            driver.find_element(*AO_Nav_Objects.By_user_menu).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Nav_Objects.By_account_link)))
            driver.find_element(*AO_Nav_Objects.By_account_link).click()
        #wait for load, replace with a find_elements check later
        WebDriverWait(driver, 60).until(EC.url_matches("https://www.advantageonlineshopping.com/#/myAccount"))
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((AO_Nav_Objects.By_account_indicator)))

        #confirm url
        if driver.current_url == "https://www.advantageonlineshopping.com/#/myAccount":
            reporter.reportStep("Click on account link","Driver should navigate to account page","Navigation successful",True,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Navigated to account page")
        else:
            reporter.reportStep("Click on account link","Driver should navigate to account page","Navigation failed",False,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Unable to navigate to account page")
    def GoTo_Orders(self, reporter, ssPath):
        driver = self.driver
        mobile = self.MobileCheck()
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((AO_Login_Objects.By_login_field)))
        if mobile:
            #print(len(driver.find_elements(*AO_Login_Objects.By_mobile_dropdown)))
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((AO_Nav_Objects.By_mobile_dropdown)))
            driver.find_element(*AO_Login_Objects.By_mobile_dropdown).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Nav_Objects.By_user_menu_m)))
            driver.find_element(*AO_Nav_Objects.By_user_menu_m).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Nav_Objects.By_orders_link_m)))
            driver.find_element(*AO_Nav_Objects.By_orders_link_m).click()
        else:
            driver.find_element(*AO_Nav_Objects.By_user_menu).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Nav_Objects.By_orders_link)))
            driver.find_element(*AO_Nav_Objects.By_orders_link).click()
        #wait for load, replace with a find_elements check later
        #time.sleep(5)
        WebDriverWait(driver, 60).until(EC.url_matches("https://www.advantageonlineshopping.com/#/MyOrders"))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((AO_Nav_Objects.By_orders_indicator)))
        #confirm url
        if driver.current_url == "https://www.advantageonlineshopping.com/#/MyOrders":
            reporter.reportStep("Click on order history link","Driver should navigate to order page","Navigation successful",True,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Navigated to orders page")
        else:
            reporter.reportStep("Click on order history link","Driver should navigate to order page","Navigation failed",False,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Unable to navigate to orders page")
    def GoTo_ShoppingCart(self, reporter, ssPath):
        driver = self.driver
        mobile = self.MobileCheck()
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((AO_Login_Objects.By_login_field)))
        if mobile:
            #print(len(driver.find_elements(*AO_Login_Objects.By_mobile_dropdown)))
            WebDriverWait(driver, 2).until(EC.element_to_be_clickable((AO_Nav_Objects.By_mobile_dropdown)))
            driver.find_element(*AO_Login_Objects.By_mobile_dropdown).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Nav_Objects.By_shopping_cart_link_m)))
            driver.find_element(*AO_Nav_Objects.By_shopping_cart_link_m).click()
        else:
            driver.find_element(*AO_Nav_Objects.By_shopping_cart_link).click()
        WebDriverWait(driver, 60).until(EC.url_matches("https://www.advantageonlineshopping.com/#/shoppingCart"))
        WebDriverWait(driver, 30).until(EC.presence_of_element_located((AO_Nav_Objects.By_shopping_cart_indicator)))
        #confirm url
        if driver.current_url == "https://www.advantageonlineshopping.com/#/shoppingCart":
            reporter.reportStep("Click on shopping cart link","Driver should navigate to shopping cart page","Navigation successful",True,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Navigated to shopping cart page")
        else:
            reporter.reportStep("Click on shopping cart link","Driver should navigate to shopping cart page","Navigation failed",False,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Unable to navigate to shopping cart page")
    def GoTo_About(self, reporter, ssPath):
        driver = self.driver
        mobile = self.MobileCheck()
        #try non-mobile clicks
        if not mobile:
            WebDriverWait(driver, 60).until(EC.invisibility_of_element((AO_Login_Objects.By_login_field)))
            driver.find_element(*AO_Nav_Objects.By_about_dropdown).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Nav_Objects.By_about_link)))
            driver.find_element(*AO_Nav_Objects.By_about_link).click()
        else:
            reporter.reportStep("Click on About link","Driver should navigate to About page","Unable to locate About link, forcing navigation",False,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Unable to locate About link, forcing navigation")
            driver.get("https://www.advantageonlineshopping.com/#/about")
            WebDriverWait(driver, 20).until(EC.url_matches("https://www.advantageonlineshopping.com/#/about"))
            WebDriverWait(driver, 20).until(EC.visibility_of_element_located((AO_Nav_Objects.By_about_indicator)))
            return
        #wait for load, replace with a find_elements check later
        WebDriverWait(driver, 20).until(EC.url_matches("https://www.advantageonlineshopping.com/#/about"))
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((AO_Nav_Objects.By_about_indicator)))
        #confirm url
        if driver.current_url == "https://www.advantageonlineshopping.com/#/about":
            reporter.reportStep("Click on About link","Driver should navigate to About page","Navigation successful",True,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Navigated to about page")
        else:
            reporter.reportStep("Click on About link","Driver should navigate to About page","Navigation failed",False,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Unable to navigate to about page")
    def GoTo_AOS(self, reporter, ssPath):
        driver = self.driver
        mobile = self.MobileCheck()
        #try non-mobile clicks
        if not mobile:
            WebDriverWait(driver, 60).until(EC.invisibility_of_element((AO_Login_Objects.By_login_field)))
            driver.find_element(*AO_Nav_Objects.By_about_dropdown).click()
            WebDriverWait(driver, 60).until(EC.element_to_be_clickable((AO_Nav_Objects.By_aos_link)))
            driver.find_element(*AO_Nav_Objects.By_aos_link).click()
        else:
            reporter.reportStep("Click on About link","Driver should navigate to About page","Unable to locate About link, forcing navigation",False,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Unable to locate About link, forcing navigation")
            driver.get("https://www.advantageonlineshopping.com/#/version")
            WebDriverWait(driver, 60).until(EC.url_matches("https://www.advantageonlineshopping.com/#/version"))
            WebDriverWait(driver, 20).until(EC.presence_of_element_located((AO_Nav_Objects.By_aos_indicator)))
            return
        #wait for load, replace with a find_elements check later
        WebDriverWait(driver, 60).until(EC.url_matches("https://www.advantageonlineshopping.com/#/version"))
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((AO_Nav_Objects.By_aos_indicator)))
        #confirm url
        if driver.current_url == "https://www.advantageonlineshopping.com/#/version":
            reporter.reportStep("Click on AOS link","Driver should navigate to AOS page","Navigation successful",True,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Navigated to aos page")
        else:
            reporter.reportStep("Click on AOS link","Driver should navigate to AOS page","Navigation failed",False,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Unable to navigate to aos page")
    def GoTo_Speakers(self, reporter, ssPath):
        driver = self.driver
        WebDriverWait(driver, 60).until(EC.invisibility_of_element((AO_Login_Objects.By_login_field)))
        driver.find_element(*AO_Nav_Objects.By_speakers_link).click()
        WebDriverWait(driver, 60).until(EC.url_matches("https://www.advantageonlineshopping.com/#/category/Speakers/4"))
        #WebDriverWait(driver, 20).until(EC.visibility_of_element_located((AO_Nav_Objects.By_speakers_indicator)))
        #confirm url
        if driver.current_url == "https://www.advantageonlineshopping.com/#/category/Speakers/4":
            reporter.reportStep("Click on Speakers link","Driver should navigate to Speakers page","Navigation successful",True,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Navigated to speakers page")
        else:
            reporter.reportStep("Click on Speakers link","Driver should navigate to Speakers page","Navigation failed",False,"", driver.find_element(By.TAG_NAME, "body").screenshot, ssPath + ''.join(random.choices(string.ascii_lowercase, k=20)))
            print("Unable to navigate to speakers page")
