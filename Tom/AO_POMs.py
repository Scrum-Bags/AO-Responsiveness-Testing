from selenium import webdriver
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time, random, traceback, logging

from AO_Locators import *
from TestSuiteReporter import TestSuiteReporter
from Utilities import log_wrapper, report_event_and_log

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.shopping_cart_link = self.driver.find_element(*BasePageLocators.By_shopping_cart_link)
    
    def element_is_loaded(self, locator) -> bool:
        if len(self.driver.find_elements(*locator)) > 0:
            return True
        else: 
            return False

    @staticmethod
    def wait_for_element(self, locator, timeout = 20):
        try: 
            WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except:
            return False
        else:
            return True
    
    @staticmethod
    def wait_for_element_disappear(self, locator, timeout = 20):
        try:
            WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))
        except:
            return False
        else:
            return True

    def check_responsive(self):
        log_wrapper(self.driver, 'Checking for responsive webpage')
        if self.driver.get_window_size()['width'] < 550:
            log_wrapper(self.driver, f"Responsive mobile detected, width = {self.driver.get_window_size()['width']}")
            self.driver.reporter[self.driver.testID].reportEvent("Detected responsive mobile site", False, "")
            self.driver.responsive_mobile = True
            self.driver.responsive_tablet = False
        elif self.driver.get_window_size()['width'] < 800:
            log_wrapper(self.driver, f"Responsive tablet detected, width = {self.driver.get_window_size()['width']}")
            self.driver.reporter[self.driver.testID].reportEvent("Detected responsive tablet site", False, "")
            self.driver.responsive_mobile = False
            self.driver.responsive_tablet = True
        else:
            log_wrapper(self.driver, 'Responsive not detected')
            self.driver.reporter[self.driver.testID].reportEvent("Detected desktop site", False, "")
            self.driver.responsive_mobile = False
            self.driver.responsive_tablet = False

    def click_shopping_cart(self):
        self.shopping_cart_link.click()
        self.wait_for_element(self, ShoppingCartPageLocators.By_checkout_btn)

    def click_order_history(self):
        if self.driver.responsive_mobile == True:
            time.sleep(1)
            self.driver.find_element(*HomePageLocators.By_mobile_expand).click()
            time.sleep(1)
            self.driver.find_element(*HomePageLocators.By_mobile_user).click()
            time.sleep(1)
            self.driver.find_element(*HomePageLocators.By_mobile_history).click()
        else:
            self.driver.find_element(*BasePageLocators.By_username).click()
            self.driver.find_element(*BasePageLocators.By_order_history_dropdown).click()

    def get_shopping_cart_num(self):
       return int(self.driver.find_element(*BasePageLocators.By_shopping_cart_num).get_attribute('textContent'))

    def logout(self):
        if self.driver.responsive_mobile == True:
           self.driver.find_element(*HomePageLocators.By_mobile_expand).click()
           time.sleep(1)
           self.driver.find_element(*HomePageLocators.By_mobile_user).click()
           time.sleep(1)
           self.driver.find_element(*BasePageLocators.By_mobile_signout).click()
        else:
            if self.driver.find_element(*BasePageLocators.By_username).get_attribute('textContent') != "":
                self.driver.find_element(*BasePageLocators.By_username).click()
                time.sleep(1)
                self.driver.find_element(*BasePageLocators.By_signout_dropdown).click()
            else:
                report_event_and_log(self.driver, "Attempted to logout but was already logged out")



class HomePage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.wait_for_page_load()
        super().__init__(driver)
        self.speakers_link = driver.find_element(*HomePageLocators.By_speakers_link)
        self.laptops_link = driver.find_element(*HomePageLocators.By_laptops_link)
        self.tablets_link = driver.find_element(*HomePageLocators.By_tablets_link)
        self.mice_link = driver.find_element(*HomePageLocators.By_mice_link)
        self.headphones_link = driver.find_element(*HomePageLocators.By_headphones_link)
        self.user_btn = driver.find_element(*HomePageLocators.By_user_btn)
        report_event_and_log(self.driver, "Loaded HomePage")

    def wait_for_page_load(self):
        timer = 0
        log_wrapper(self.driver, "Waiting for home page to load...")
        while len(self.driver.find_elements(*HomePageLocators.By_headphones_link)) == 0 and timer < 10:
            log_wrapper(self.driver, "Still waiting, refresh in " + str(10 - timer) + "s")
            time.sleep(1)
            timer += 1
        if len(self.driver.find_elements(*HomePageLocators.By_headphones_link)) == 0:
            log_wrapper(self.driver, "Refreshing page")
            self.driver.refresh()
            self = HomePage(self.driver)

    def click_speakers(self):
        self.speakers_link.click()
        self.wait_for_element(self, SpeakersPageLocators.By_price_expander)
        report_event_and_log(self.driver, "Clicked speakers link")

    def click_laptops(self):
        self.laptops_link.click()
        self.wait_for_element(self, SpeakersPageLocators.By_price_expander)
        report_event_and_log(self.driver, "Clicked laptops link")

    def click_tablets(self):
        self.tablets_link.click()
        self.wait_for_element(self, SpeakersPageLocators.By_price_expander)
        report_event_and_log(self.driver, "Clicked tablets link")

    def click_mice(self):
        self.mice_link.click()
        self.wait_for_element(self, SpeakersPageLocators.By_price_expander)
        report_event_and_log(self.driver, "Clicked mice link")

    def click_headphones(self):
        self.headphones_link.click()
        self.wait_for_element(self, SpeakersPageLocators.By_price_expander)
        report_event_and_log(self.driver, "Clicked mice link")

    def click_category_excel(self, value):
        report_event_and_log(self.driver, "Clicking category page from excel")
        value = value.upper()
        if value == "SPEAKERS":
            self.click_speakers()
            return SpeakersPage(self.driver)
        elif value == "LAPTOPS":
            self.click_laptops()
            return LaptopsPage(self.driver)
        elif value == "TABLETS":
            self.click_tablets()
            return TabletsPage(self.driver)
        elif value == "MICE":
            self.click_mice()
            return MicePage(self.driver)
        elif value == "HEADPHONES":
            self.click_headphones()
            return HeadphonesPage(self.driver)

    def login(self, user, password):
        if self.driver.find_element(*BasePageLocators.By_username).get_attribute('textContent') == "":
            if self.driver.responsive_mobile == True:
                self.driver.find_element(*HomePageLocators.By_mobile_expand).click()
                time.sleep(0.3)
                self.driver.find_element(*HomePageLocators.By_mobile_user).click()
            else:
                self.user_btn.click()
            time.sleep(1)
            self.driver.find_element(*HomePageLocators.By_username_field).send_keys(user)
            self.driver.find_element(*HomePageLocators.By_password_field).send_keys(password)
            self.driver.find_element(*HomePageLocators.By_signin_btn).click()
            self.wait_for_element_disappear(self, HomePageLocators.By_signin_btn)
            report_event_and_log(self.driver, "Logged in")
        else:
            report_event_and_log(self.driver, "Attempted to login but was already logged in")

    

class StorePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.price_expander = driver.find_element(*StorePageLocators.By_price_expander)
        self.price_left_handle = driver.find_element(*StorePageLocators.By_price_left_handle)
        self.price_right_handle = driver.find_element(*StorePageLocators.By_price_right_handle)

    def expand_expander(self, element):
        if "arrowUp" not in element.get_attribute("class"):
            element.click()
            time.sleep(0.3)
            report_event_and_log(self.driver, "Expanded expander with label " + element.text)

    def close_expander(self, element):
        if "arrowUp" in element.get_attribute('class'):
            element.click()
            time.sleep(0.3)
            report_event_and_log(self.driver, "Closed expander with label " + element.text)

    def get_left_price(self) -> int:
        left_price = self.driver.find_element(*StorePageLocators.By_price_left_val).get_attribute('textContent')
        left_price = left_price.replace(',', '')
        return int(left_price[1:])

    def get_right_price(self) -> int:
        right_price = self.driver.find_element(*StorePageLocators.By_price_right_val).get_attribute('textContent')
        right_price = right_price.replace(',', '')
        return int(right_price[1:])

    def set_left_price(self, value):
        pixel_length = self.driver.find_element(*StorePageLocators.By_price_slider).size['width']
        converted_val = (value - self.get_left_price()) * (pixel_length/((self.get_right_price() - self.get_left_price()))) 
        action = ActionChains(self.driver)
        action.drag_and_drop_by_offset(self.price_left_handle, converted_val, 0).perform()
        report_event_and_log(self.driver, "Set left price slider to value " + str(value))

    def set_right_price(self, value):
        if self.get_right_price() - value < 2:
            return
        else:
            pixel_length = self.driver.find_element(*StorePageLocators.By_price_slider).size['width']
            converted_val = (value - self.get_left_price()) * (pixel_length/((self.get_right_price() - self.get_left_price()))) 
            action = ActionChains(self.driver)
            action.drag_and_drop_by_offset(self.price_right_handle, converted_val - pixel_length, 0).perform()
        report_event_and_log(self.driver, "Set right price slider to value " + str(value))

    def set_price(self, value):
        if value - 5 > self.get_left_price():
            self.set_left_price(value - 1)
        if value + 5 < self.get_right_price(): 
            self.set_right_price(value)

    def get_num_items(self) -> int:
        return int(self.driver.find_element(*StorePageLocators.By_num_items).get_attribute('textContent').strip().split()[0])

    def get_displayed_num_items(self) -> int:
        return int(len(self.driver.find_elements(*StorePageLocators.By_item_area)))

    def wait_for_item_display_update(self, timeout=3.0):
        timer = 0.0
        while (self.get_displayed_num_items() != self.get_num_items()) and timer < timeout:
            time.sleep(0.5)
            timer += 0.5
        if timer < timeout:
            self.driver.reporter[self.driver.testID].reportStep(
                "Waited for displayed items to update after filters set",
                "Displayed items updated to correct amount shown",
                "Displayed items updated to correct amount shown",
                True,
                "",
                screenshotCallback=self.driver.save_screenshot
            )
        else:
            self.driver.reporter[self.driver.testID].reportStep(
                "Waited for displayed items to update after filters set",
                "Displayed items updated to correct amount shown",
                "Displayed items updated to incorrect amount shown",
                False,
                "",
                screenshotCallback=self.driver.save_screenshot
            )

    def click_ith_item(self, value):
        xpath = StorePageLocators.By_item_area[1] + '[' + str(value) + ']'
        try:
            self.driver.find_element(By.XPATH, xpath).click()
            self.wait_for_element(self, ItemPageLocators.By_add_to_cart_btn)
            report_event_and_log(self.driver, "Clicked item #" + str(value))
        except:
            report_event_and_log(self.driver, "click_ith_item() - Element does not exist")

    def clear_selection(self):
        self.driver.execute_script("window.scrollTo(0,0)")
        self.driver.find_element(*StorePageLocators.By_clear_selection).click()
        time.sleep(0.5)
        report_event_and_log(self.driver, "Cleared all filter options")

    def get_prod_name(self, value) -> str:
        xpath = StorePageLocators.By_item_area[1] + '[' + str(value) + ']/p[1]/a'
        try:
            return self.driver.find_element(By.XPATH, xpath).get_attribute('textContent').strip().upper()
        except:
            report_event_and_log(self.driver, "get_prod_name() - Element does not exist")
            return "N/A"

    def get_prod_price(self, value) -> str:
        xpath = StorePageLocators.By_item_area[1] + '[' + str(value) + ']/p[2]/a'
        try:
            return self.driver.find_element(By.XPATH, xpath).get_attribute('textContent').strip().upper()
        except:
            report_event_and_log(self.driver, "get_prod_price() - Element does not exist")
            return "N/A"

    def open_responsive_filter(self):
        if 'display: block;' not in self.driver.find_element(*StorePageLocators.By_mobile_slider).get_attribute('style'):
            self.driver.find_element(*StorePageLocators.By_responsive_filter).click()
            time.sleep(0.3)
            report_event_and_log(self.driver, "Opened responsive filter")

    def scroll_to_bottom(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

class SpeakersPage(StorePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.price_expander = driver.find_element(*SpeakersPageLocators.By_price_expander)
        self.price_left_handle = driver.find_element(*SpeakersPageLocators.By_price_left_handle)
        self.price_right_handle = driver.find_element(*SpeakersPageLocators.By_price_right_handle)
        self.compat_expander = driver.find_element(*SpeakersPageLocators.By_compatibility_expander)
        self.manufacturer_expander = driver.find_element(*SpeakersPageLocators.By_manufacturer_expander)
        self.weight_expander = driver.find_element(*SpeakersPageLocators.By_weight_expander)
        self.wireless_expander = driver.find_element(*SpeakersPageLocators.By_wireless_expander)
        self.color_expander = driver.find_element(*SpeakersPageLocators.By_color_expander)
        report_event_and_log(self.driver, "Loaded Speakers Page")

    def expand_all(self):
        self.price_expander.click()
        self.compat_expander.click()
        self.manufacturer_expander.click()
        self.weight_expander.click()
        self.wireless_expander.click()
        self.color_expander.click()

    def set_compat(self, value):
        if value == "0":
                self.driver.find_element(*SpeakersPageLocators.By_compat_0).click()
        elif value == "1":
            self.driver.find_element(*SpeakersPageLocators.By_compat_1).click()
        report_event_and_log(self.driver, "Set compatability option to " + str(value))

    def set_manufacturer(self, value):
        if value == "Bose":
            self.driver.find_element(*SpeakersPageLocators.By_manufacturer_0).click()
        elif value == "HP":
            self.driver.find_element(*SpeakersPageLocators.By_manufacturer_1).click()
        elif value == "Logitech":
            self.driver.find_element(*SpeakersPageLocators.By_manufacturer_2).click()
        report_event_and_log(self.driver, "Set manufacturer option to " + str(value))

    def set_weight(self, value):
        if value == "0.55 lb":
            self.driver.find_element(*SpeakersPageLocators.By_weight_0).click()
        elif value == "1.0 lb":
            self.driver.find_element(*SpeakersPageLocators.By_weight_1).click()
        elif value == "1.1 lb":
            self.driver.find_element(*SpeakersPageLocators.By_weight_2).click()
        elif value == "1.25 lb":
            self.driver.find_element(*SpeakersPageLocators.By_weight_3).click()
        elif value == "1.26 lb":
            self.driver.find_element(*SpeakersPageLocators.By_weight_4).click()
        elif value == "1.95 lb":
            self.driver.find_element(*SpeakersPageLocators.By_weight_5).click()
        elif value == "3.03 lb":
            self.driver.find_element(*SpeakersPageLocators.By_weight_6).click()
        report_event_and_log(self.driver, "Set weight option to " + str(value))

    def set_wireless(self, value):
        if value == "0":
            self.driver.find_element(*SpeakersPageLocators.By_wireless_0).click()
        elif value == "1": 
            self.driver.find_element(*SpeakersPageLocators.By_wireless_1).click()
        report_event_and_log(self.driver, "Set wireless option to " + str(value))
                
    def set_color(self, value):
        if value == "BLACK":
            self.driver.find_element(*SpeakersPageLocators.By_color_BLACK).click()
        elif value == "BLUE":
            self.driver.find_element(*SpeakersPageLocators.By_color_BLUE).click()
        elif value == "GRAY":
            self.driver.find_element(*SpeakersPageLocators.By_color_GRAY).click()
        elif value == "PURPLE":
            self.driver.find_element(*SpeakersPageLocators.By_color_PURPLE).click()
        elif value == "RED":
            self.driver.find_element(*SpeakersPageLocators.By_color_RED).click()
        elif value == "TURQUOISE":
            self.driver.find_element(*SpeakersPageLocators.By_color_TURQUOISE).click()
        elif value == "WHITE":
            self.driver.find_element(*SpeakersPageLocators.By_color_WHITE).click()
        elif value == "YELLOW":
            self.driver.find_element(*SpeakersPageLocators.By_color_YELLOW).click()
        report_event_and_log(self.driver, "Set color option to " + str(value))

class LaptopsPage(StorePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.price_expander = driver.find_element(*LaptopsPageLocators.By_price_expander)
        self.price_left_handle = driver.find_element(*LaptopsPageLocators.By_price_left_handle)
        self.price_right_handle = driver.find_element(*LaptopsPageLocators.By_price_right_handle)
        self.display_expander = driver.find_element(*LaptopsPageLocators.By_display_expander)
        self.os_expander = driver.find_element(*LaptopsPageLocators.By_os_expander)
        self.processor_expander = driver.find_element(*LaptopsPageLocators.By_processor_expander)
        self.weight_expander = driver.find_element(*LaptopsPageLocators.By_weight_expander)
        self.color_expander = driver.find_element(*LaptopsPageLocators.By_color_expander)
        report_event_and_log(self.driver, "Loaded Laptops Page")

    def set_display(self, value):
        if value ==  "0":
            self.driver.find_element(*LaptopsPageLocators.By_display_0).click()
        elif value ==  "1":
            self.driver.find_element(*LaptopsPageLocators.By_display_1).click()
        elif value ==  "2":
            self.driver.find_element(*LaptopsPageLocators.By_display_2).click()               
        elif value ==  "3":
            self.driver.find_element(*LaptopsPageLocators.By_display_3).click()
        elif value ==  "4":
            self.driver.find_element(*LaptopsPageLocators.By_display_4).click()
        elif value ==  "5":
            self.driver.find_element(*LaptopsPageLocators.By_display_5).click()
        elif value ==  "6":
            self.driver.find_element(*LaptopsPageLocators.By_display_6).click()
        elif value ==  "7":
            self.driver.find_element(*LaptopsPageLocators.By_display_7).click()
        elif value ==  "8":
            self.driver.find_element(*LaptopsPageLocators.By_display_8).click()
        elif value ==  "9":
            self.driver.find_element(*LaptopsPageLocators.By_display_9).click()
        elif value ==  "10":
            self.driver.find_element(*LaptopsPageLocators.By_display_10).click()
        report_event_and_log(self.driver, "Set display option to " + str(value))

    def set_os(self, value):
        if value ==  "Chrome OS":
            self.driver.find_element(*LaptopsPageLocators.By_os_0).click()
        elif value ==  "Windows 10":
            self.driver.find_element(*LaptopsPageLocators.By_os_1).click()
        elif value ==  "Windows 7 Professional 64":
            self.driver.find_element(*LaptopsPageLocators.By_os_2).click()
        elif value ==  "Windows 8.1":
            self.driver.find_element(*LaptopsPageLocators.By_os_3).click()
        report_event_and_log(self.driver, "Set operating system option to " + str(value))

    def set_processor(self, value):
        if value ==  "0":
            self.driver.find_element(*LaptopsPageLocators.By_processor_0).click()
        elif value ==  "1":
            self.driver.find_element(*LaptopsPageLocators.By_processor_1).click()
        elif value ==  "2":
            self.driver.find_element(*LaptopsPageLocators.By_processor_2).click()
        elif value ==  "3":
            self.driver.find_element(*LaptopsPageLocators.By_processor_3).click()
        elif value ==  "4":
            self.driver.find_element(*LaptopsPageLocators.By_processor_4).click()
        elif value ==  "5":
            self.driver.find_element(*LaptopsPageLocators.By_processor_5).click()
        elif value ==  "6":
            self.driver.find_element(*LaptopsPageLocators.By_processor_6).click()
        elif value ==  "7":
            self.driver.find_element(*LaptopsPageLocators.By_processor_7).click()
        elif value ==  "8":
            self.driver.find_element(*LaptopsPageLocators.By_processor_8).click()
        elif value ==  "9":
            self.driver.find_element(*LaptopsPageLocators.By_processor_9).click()
        report_event_and_log(self.driver, "Set processor option to " + str(value))

    def set_weight(self, value):
        if value ==  "2.3 lb":
            self.driver.find_element(*LaptopsPageLocators.By_weight_0).click()
        elif value ==  "2.6 lb":
            self.driver.find_element(*LaptopsPageLocators.By_weight_1).click()
        elif value ==  "3.17 lb":
            self.driver.find_element(*LaptopsPageLocators.By_weight_2).click()
        elif value ==  "3.2 lb": 
            self.driver.find_element(*LaptopsPageLocators.By_weight_3).click()
        elif value ==  "3.21 lb":
            self.driver.find_element(*LaptopsPageLocators.By_weight_4).click()
        elif value ==  "3.4 lb":
            self.driver.find_element(*LaptopsPageLocators.By_weight_5).click()
        elif value ==  "4 lb":
            self.driver.find_element(*LaptopsPageLocators.By_weight_6).click()
        elif value ==  "4.96 lb":
            self.driver.find_element(*LaptopsPageLocators.By_weight_7).click()
        elif value ==  "5.51 lb":
            self.driver.find_element(*LaptopsPageLocators.By_weight_8).click()
        elif value ==  "7.25 lb":
            self.driver.find_element(*LaptopsPageLocators.By_weight_9).click()
        elif value ==  "7.42 lb":
            self.driver.find_element(*LaptopsPageLocators.By_weight_10).click()
        report_event_and_log(self.driver, "Set weight option to " + str(value))

    def set_color(self, value):
        if value ==  "BLACK":
            self.driver.find_element(*LaptopsPageLocators.By_color_BLACK).click()
        elif value ==  "BLUE":
            self.driver.find_element(*LaptopsPageLocators.By_color_BLUE).click()
        elif value ==  "GRAY":
            self.driver.find_element(*LaptopsPageLocators.By_color_GRAY).click()
        elif value ==  "PURPLE":
            self.driver.find_element(*LaptopsPageLocators.By_color_PURPLE).click()
        elif value ==  "RED":
            self.driver.find_element(*LaptopsPageLocators.By_color_RED).click()
        elif value ==  "TURQUOISE":
            self.driver.find_element(*LaptopsPageLocators.By_color_TURQUOISE).click()
        elif value ==  "WHITE":
            self.driver.find_element(*LaptopsPageLocators.By_color_WHITE).click()
        elif value ==  "YELLOW":
            self.driver.find_element(*LaptopsPageLocators.By_color_YELLOW).click()
        report_event_and_log(self.driver, "Set weight option to " + str(value))

class TabletsPage(StorePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.price_expander = driver.find_element(*TabletsPageLocators.By_price_expander)
        self.price_left_handle = driver.find_element(*TabletsPageLocators.By_price_left_handle)
        self.price_right_handle = driver.find_element(*TabletsPageLocators.By_price_right_handle)
        self.display_expander = driver.find_element(*TabletsPageLocators.By_display_expander)
        self.processor_expander = driver.find_element(*TabletsPageLocators.By_processor_expander)
        self.color_expander = driver.find_element(*TabletsPageLocators.By_color_expander)
        report_event_and_log(self.driver, "Loaded Tablets Page")

    def set_display(self, value):
        if value ==  "0":
            self.driver.find_element(*TabletsPageLocators.By_display_0).click()
        elif value ==  "1":
            self.driver.find_element(*TabletsPageLocators.By_display_1).click()
        elif value ==  "2":
            self.driver.find_element(*TabletsPageLocators.By_display_2).click()
        report_event_and_log(self.driver, "Set display option to " + str(value))

    def set_processor(self, value):
        if value ==  "0":
            self.driver.find_element(*TabletsPageLocators.By_processor_0).click()
        elif value ==  "1":
            self.driver.find_element(*TabletsPageLocators.By_processor_1).click()
        elif value ==  "2":
            self.driver.find_element(*TabletsPageLocators.By_processor_2).click()
        report_event_and_log(self.driver, "Set processor option to " + str(value))

    def set_color(self, value):
        if value ==  "BLACK":
            self.driver.find_element(*TabletsPageLocators.By_color_BLACK).click()
        elif value ==  "GRAY":
            self.driver.find_element(*TabletsPageLocators.By_color_GRAY).click()
        report_event_and_log(self.driver, "Set color option to " + str(value))
    
class MicePage(StorePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.price_expander = driver.find_element(*MicePageLocators.By_price_expander)
        self.price_left_handle = driver.find_element(*MicePageLocators.By_price_left_handle)
        self.price_right_handle = driver.find_element(*MicePageLocators.By_price_right_handle)
        self.scroller_expander = driver.find_element(*MicePageLocators.By_scroller_expander)
        self.color_expander = driver.find_element(*MicePageLocators.By_color_expander)
        report_event_and_log(self.driver, "Loaded Mice Page")

    def set_scroller(self, value):
        if value ==  "0":
            self.driver.find_element(*MicePageLocators.By_scroller_0).click()
        elif value ==  "1":
            self.driver.find_element(*MicePageLocators.By_scroller_1).click()
        elif value ==  "2":
            self.driver.find_element(*MicePageLocators.By_scroller_2).click()
        elif value ==  "3":
            self.driver.find_element(*MicePageLocators.By_scroller_3).click()
        elif value ==  "4":
            self.driver.find_element(*MicePageLocators.By_scroller_4).click()
        report_event_and_log(self.driver, "Set scroller option to " + str(value))

    def set_color(self, value):
        if value ==  "BLACK":
            self.driver.find_element(*MicePageLocators.By_color_BLACK).click()
        elif value ==  "BLUE":
            self.driver.find_element(*MicePageLocators.By_color_BLUE).click()
        elif value ==  "GRAY":
            self.driver.find_element(*MicePageLocators.By_color_GRAY).click()
        elif value ==  "PURPLE":
            self.driver.find_element(*MicePageLocators.By_color_PURPLE).click()
        elif value ==  "RED":
            self.driver.find_element(*MicePageLocators.By_color_RED).click()
        elif value ==  "WHITE":
            self.driver.find_element(*MicePageLocators.By_color_WHITE).click()
        report_event_and_log(self.driver, "Set color option to " + str(value))

class HeadphonesPage(StorePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.price_expander = driver.find_element(*HeadphonesPageLocators.By_price_expander)
        self.price_left_handle = driver.find_element(*HeadphonesPageLocators.By_price_left_handle)
        self.price_right_handle = driver.find_element(*HeadphonesPageLocators.By_price_right_handle)
        self.compatibility_expander = driver.find_element(*HeadphonesPageLocators.By_compatibility_expander)
        self.connector_expander = driver.find_element(*HeadphonesPageLocators.By_connector_expander)
        self.weight_expander = driver.find_element(*HeadphonesPageLocators.By_weight_expander)
        self.color_expander = driver.find_element(*HeadphonesPageLocators.By_color_expander)
        report_event_and_log(self.driver, "Loaded Headphones Page")

    def set_compat(self, value):
        if value ==  "0":
            self.driver.find_element(*HeadphonesPageLocators.By_compat_0).click()
        elif value ==  "1":
            self.driver.find_element(*HeadphonesPageLocators.By_compat_1).click()
        elif value ==  "2":
            self.driver.find_element(*HeadphonesPageLocators.By_compat_2).click()
        report_event_and_log(self.driver, "Set compatability option to " + str(value))

    def set_connector(self, value):
        if value ==  "0":
            self.driver.find_element(*HeadphonesPageLocators.By_connector_0).click()
        elif value ==  "1":
            self.driver.find_element(*HeadphonesPageLocators.By_connector_1).click()
        report_event_and_log(self.driver, "Set connector option to " + str(value))

    def set_weight(self, value):
        if value ==  "0.03 lb":
            self.driver.find_element(*HeadphonesPageLocators.By_weight_0).click()
        elif value ==  "0.07 lb":
            self.driver.find_element(*HeadphonesPageLocators.By_weight_1).click()
        elif value ==  "0.15 lb":
            self.driver.find_element(*HeadphonesPageLocators.By_weight_2).click()
        elif value ==  "0.57 lb":
            self.driver.find_element(*HeadphonesPageLocators.By_weight_3).click()
        report_event_and_log(self.driver, "Set weight option to " + str(value))

    def set_color(self, value):
        if value ==  "BLACK":
            self.driver.find_element(*LaptopsPageLocators.By_color_BLACK).click()
        elif value ==  "BLUE":
            self.driver.find_element(*LaptopsPageLocators.By_color_BLUE).click()
        elif value ==  "GRAY":
            self.driver.find_element(*LaptopsPageLocators.By_color_GRAY).click()
        elif value ==  "PURPLE":
            self.driver.find_element(*LaptopsPageLocators.By_color_PURPLE).click()
        elif value ==  "RED":
            self.driver.find_element(*LaptopsPageLocators.By_color_RED).click()
        elif value ==  "TURQUOISE":
            self.driver.find_element(*LaptopsPageLocators.By_color_TURQUOISE).click()
        elif value ==  "WHITE":
            self.driver.find_element(*LaptopsPageLocators.By_color_WHITE).click()
        elif value ==  "YELLOW":
            self.driver.find_element(*LaptopsPageLocators.By_color_YELLOW).click()
        report_event_and_log(self.driver, "Set color option to " + str(value))

class ItemPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.minus = self.driver.find_element(*ItemPageLocators.By_minus_btn)
        self.plus = self.driver.find_element(*ItemPageLocators.By_plus_btn)
        self.add_to_cart = self.driver.find_element(*ItemPageLocators.By_add_to_cart_btn)
        report_event_and_log(self.driver, 'Loaded individual item page')

    def set_quantity(self, value):
        if value == 1:
            report_event_and_log(self.driver, 'Set quantity to ' + str(value))
            return
        else:
            for i in range(1, value):
                self.plus.click()
            report_event_and_log(self.driver, 'Set quantity to ' + str(value))

    def set_color(self, value):
        value = int(value)
        if value == 1:
            report_event_and_log(self.driver, 'Set color to ' + str(value))
            return
        else:
            try:
                xpath = ItemPageLocators.By_color_select[1] + '[' + str(value) + ']'
                self.driver.find_element(By.XPATH, xpath).click()
                report_event_and_log(self.driver, 'Set color to ' + str(value))
            except:
                traceback.print_exc()
                print("Color selection error - value probably out of range")

    def get_prod_name(self) -> str:
        return self.driver.find_element(*ItemPageLocators.By_item_name).get_attribute('textContent').strip().upper()

    def get_prod_price(self) -> str:
        return self.driver.find_element(*ItemPageLocators.By_item_price).get_attribute('textContent').split(' ')[1].strip().upper()
    
    def click_add_cart(self, timeout = 15):
        timeCounter = 0
        prevNum = self.get_shopping_cart_num()
        self.add_to_cart.click()
        while self.get_shopping_cart_num() == prevNum:
            time.sleep(1)
            timeCounter += 1 
            if timeCounter == timeout:
                return False
        return True

class ShoppingCartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.checkout_btn = self.driver.find_element(*ShoppingCartPageLocators.By_checkout_btn)

    def click_checkout(self):
        try: 
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.checkout_btn)
            )
        except:
            return False
        else:
            self.checkout_btn.click()
            if self.wait_for_element(self, OrderPaymentPageLocators.By_next_btn) == False:
                print("Failed to add item to cart")
                return False
            return True

class OrderPaymentPage_1(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.edit_shipping = self.driver.find_element(*OrderPaymentPageLocators.By_edit_shipping_link)
        self.next_btn = self.driver.find_element(*OrderPaymentPageLocators.By_next_btn)
    
    def click_next(self):
        self.next_btn.click()
        self.wait_for_element(self, OrderPaymentPageLocators.By_safepay_user)

class OrderPaymentPage_2(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.safepay_user = self.driver.find_element(*OrderPaymentPageLocators.By_safepay_user)
        self.safepay_pass = self.driver.find_element(*OrderPaymentPageLocators.By_safepay_password)
        self.mastercredit_op = self.driver.find_element(*OrderPaymentPageLocators.By_mastercredit_method)
        self.paynow = self.driver.find_element(*OrderPaymentPageLocators.By_safepay_paynow)

    def safepay_checkout(self):
        #self.safepay_user.send_keys(username)
        #self.safepay_pass.send_keys(password)
        self.driver.find_element(*OrderPaymentPageLocators.By_safepay_method).click()
        self.paynow.click()
        self.wait_for_element(self, OrderConfirmationPageLocators.By_tracking_num)

    def mastercredit_checkout(self):
        self.mastercredit_op.click()
        self.driver.find_element(*OrderPaymentPageLocators.By_creditcard_paynow).click()

    def choose_payment(self, value):
        if value ==  "SAFEPAY":
            self.safepay_checkout()
        elif value ==  "MASTERCREDIT":
            self.mastercredit_checkout()

class OrderConfirmationPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.tracking_num = self.driver.find_element(*OrderConfirmationPageLocators.By_tracking_num)
        self.order_num = self.driver.find_element(*OrderConfirmationPageLocators.By_order_num)
        self.order_total = self.driver.find_element(*OrderConfirmationPageLocators.By_order_total)

    def get_order_num(self):
        while self.order_num.get_attribute('textContent') == "":
            time.sleep(.1)
        return self.order_num.get_attribute('textContent')

    def get_tracking_num(self):
        while self.tracking_num.get_attribute('textContent') == "":
            time.sleep(.1)
        return self.tracking_num.get_attribute('textContent')

    def click_order_history(self):
        self.driver.get('https://www.advantageonlineshopping.com/#/MyOrders')
        self.wait_for_element(self, OrderHistoryPageLocators.By_order_num)
        while self.driver.find_element(*OrderHistoryPageLocators.By_order_num).get_attribute('textContent') == "":
            time.sleep(.1)

class OrderHistoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        time.sleep(2)
        if self.element_is_loaded(OrderHistoryPageLocators.By_no_orders):
            self.no_orders = self.driver.find_element(*OrderHistoryPageLocators.By_no_orders)
        else:
            self.wait_for_element(self, OrderHistoryPageLocators.By_order_num)
        #self.most_recent_order_num = self.driver.find_element(*OrderHistoryPageLocators.By_order_num)
        #self.most_recent_total_price = self.driver.find_element(*OrderHistoryPageLocators.By_total_price)

    def check_order_num(self, value):
        time.sleep(3)
        elements = self.driver.find_elements(By.TAG_NAME, 'tr')
        for element in elements:
            if value == element.find_elements(By.XPATH, './/*')[1].get_attribute('textContent'):
                return True
        return False

    def get_row_count(self) -> int:
        #subtract one from the end to remove header
        return len(self.driver.find_elements(By.XPATH, '//*[@id="myAccountContainer"]/div/table/tbody/tr')) - 1

    #returns a hash table of all values of a particular row
    def get_row_information(self, rowNum):
        output = {}
        #variable gets inserted inbetween xpath and xpath_end of the column we want
        xpath = '//*[@id="myAccountContainer"]/div/table/tbody/tr[' + str(rowNum + 1) + ']/td['
        xpath_end = ']/label'
        if self.element_is_loaded((By.XPATH, xpath + '1' + xpath_end)):
            output['order_num'] = self.driver.find_element(By.XPATH, xpath + '1' + xpath_end).get_attribute('textContent')
            output['order_date'] = self.driver.find_element(By.XPATH, xpath + '2' + xpath_end).get_attribute('textContent')
            output['order_time'] = self.driver.find_element(By.XPATH, xpath + '3' + xpath_end).get_attribute('textContent')
            output['product_name'] = self.driver.find_element(By.XPATH, xpath + '4' + ']/span').get_attribute('textContent')
            output['quantity'] = self.driver.find_element(By.XPATH, xpath + '6' + xpath_end).get_attribute('textContent')
            output['total_price'] = self.driver.find_element(By.XPATH, xpath + '7' + xpath_end).get_attribute('textContent')
        else:
            output['order_num'] = None
        return output

    def get_row_by_confirmation_num(self, confirmationNum):
        #find the row num assocaited with confirmationNum, then 
        #return that row with get_row_information()
        for i in range(1, self.get_row_count() + 1):
            data = self.get_row_information(i)
            if data['order_num'] == confirmationNum:
                return data
        
    def get_total_price(self):
        elements = self.driver.find_elements(By.TAG_NAME, 'tr')
        return elements[-1].find_elements(By.XPATH, './/*')[14].get_attribute('textContent')