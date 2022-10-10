from re import match as rematch
from time import sleep
from typing import Union

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from page_elements.advantage_online_elements import *
from runittest.reporting_unittest import SingletonWebDriver


class Page:
    """Base page class to handle basic object inclusion."""

    def __init__(
        self,
        idDict: dict,
        waitTimeout: int = 30
    ):
        self.elements = {}
        self.baseElementIDs = {}
        self.driverObj = SingletonWebDriver()
        self.waitForElements(idDict, waitTimeout)
        self.addElements(idDict)
        self.loaded = len(self.baseElementIDs) == len(idDict)

    def addElements(self, idDict: dict):
        self.baseElementIDs.update(idDict)
        for name, args in idDict.items():
            try:
                tempElement = self.driverObj.find_element(**args)
            except NoSuchElementException as e:
                # displayPrint("Element not found" **args)
                continue
            else:
                # displayPrint("Element found", **args)
                self.elements[name] = tempElement
    
    def refresh(self):
        self.addElements(self.baseElementIDs)
    
    def waitForElements(
        self,
        objectIDs: dict,
        timeOut: int
    ):
        conditions = [
            EC.presence_of_element_located(l.values())
            for l in
            objectIDs.values()
        ]
        WebDriverWait(
            self.driverObj,
            timeOut
        ).until(
            EC.all_of(*conditions)
        )


class AdvantagePage(Page):

    def __init__(
        self,
        loggedIn: bool,
        extraDict: Union[dict, None] = None
    ):
        self.loggedIn = loggedIn
        baseDict = commonElementIDs
        if self.loggedIn:
            baseDict.update(loggedInCommonElementIDs)
        else:
            baseDict.update(loggedOutCommonElementIDs)
        super().__init__(idDict=baseDict)
        if extraDict is not None:
            self.addElements(extraDict)
        WebDriverWait(
            self.driverObj,
            10
        ).until(
            EC.invisibility_of_element(
                commonElementIDs["loader"].values()
            )
        )
    
    def goToUserRegistration(self):
        if not self.loggedIn:
            WebDriverWait(
                self.driverObj,
                10
            ).until(
                EC.element_to_be_clickable(
                    commonElementIDs["user_icon"].values()
                )
            )
            self.elements["user_icon"].click()
            WebDriverWait(
                self.driverObj,
                5
            ).until(
                EC.element_to_be_clickable(
                    loggedOutCommonElementIDs["new_account"].values()
                )
            )
            self.elements["new_account"].click()
            WebDriverWait(
                self.driverObj,
                10
            ).until(
                EC.visibility_of_element_located(
                    userRegisterElementIDs["register_button"].values()
                )
            )
    
    def goToUserProfile(self):
        if self.loggedIn:
            WebDriverWait(
                self.driverObj,
                10
            ).until(
                EC.visibility_of_element_located(
                    loggedInCommonElementIDs["user_menu"].values()
                )
            )
            WebDriverWait(
                self.driverObj,
                10
            ).until(
                EC.element_to_be_clickable(
                    loggedInCommonElementIDs["user_menu"].values()
                )
            )
            self.elements["user_menu"].click()
            WebDriverWait(
                self.driverObj,
                10
            ).until(
                EC.visibility_of_element_located(
                    loggedInCommonElementIDs["menu_items_container"].values()
                )
            )
            WebDriverWait(
                self.driverObj,
                10
            ).until(
                EC.element_to_be_clickable(
                    loggedInCommonElementIDs["menu_items_container"].values()
                )
            )
            summaryElement = self.elements["menu_items_container"].find_elements(By.TAG_NAME, "label")[0]
            summaryElement.click()
            WebDriverWait(
                self.driverObj,
                10
            ).until(
                EC.visibility_of_element_located(
                    accountSummaryElementIDs["details_box"].values()
                )
            )
    
    def logIn(
        self, 
        username: str,
        password: str
    ):
        if not self.loggedIn:
            WebDriverWait(
                self.driverObj,
                10
            ).until(
                EC.element_to_be_clickable(
                    commonElementIDs["user_icon"].values()
                )
            )
            self.elements["user_icon"].click()
            sleep(0.5)
            self.elements['login_username'].clear()
            self.elements['login_username'].send_keys(username)
            self.elements['login_password'].clear()
            self.elements['login_password'].send_keys(password)
            self.elements['login_button'].click()
            self.waitForElements(
                loggedInCommonElementIDs,
                10
            )
    
    def logOut(self):
        if self.loggedIn:
            WebDriverWait(
                self.driverObj,
                10
            ).until(
                EC.element_to_be_clickable(
                    loggedInCommonElementIDs["user_menu"].values()
                )
            )
            self.elements["user_menu"].click()
            WebDriverWait(
                self.driverObj,
                10
            ).until(
                EC.element_to_be_clickable(
                    loggedInCommonElementIDs["menu_items_container"].values()
                )
            )
            logOutElement = self.elements["menu_items_container"].find_elements(By.TAG_NAME, "label")[2]
            logOutElement.click()
    
    def mobileElementsDisplayed(self) -> bool:
        mobileSidebar = self.driverObj.find_element(
            **commonMobileElementIDs["mobile_sidebar_button"]
        )
        if all(
            [
                EC.element_to_be_clickable(mobileSidebar),
                mobileSidebar.location['x'] >= 0,
                mobileSidebar.location['y'] >= 0,
                mobileSidebar.size['height'] > 0,
                mobileSidebar.size['width'] > 0,
            ]
        ):
            mobileSidebar.click()
            sleep(0.6)
            return all(
                [
                    EC.visibility_of(
                        commonMobileElementIDs["mobile_cart"]
                    ),
                    EC.visibility_of(
                        commonMobileElementIDs["mobile_home"]
                    ),
                    EC.visibility_of(
                        commonMobileElementIDs["mobile_user"]
                    ),
                ]
            )
        return False


class MainPage(AdvantagePage):
    
    def __init__(
        self,
        loggedIn: bool,
    ):
        super().__init__(
            loggedIn=loggedIn,
            extraDict=mainPageWideElementIDs
        )
        self.waitForElements(
            mainPageWaitIDs,
            10
        )
        WebDriverWait(
            self.driverObj,
            10
        ).until(
            EC.invisibility_of_element(
                commonElementIDs["loader"].values()
            )
        )
        if loggedIn:
            sleep(5.0)


class RegisterPage(AdvantagePage):

    def __init__(self):
        super().__init__(
            loggedIn=False,
            extraDict=userRegisterElementIDs
        )
        self.fieldKeys = list(self.elements.keys())
        WebDriverWait(
            self.driverObj,
            5
        ).until(
            EC.invisibility_of_element(
                loggedOutCommonElementIDs["new_account"].values()
            )
        )

    def fillUsername(
        self,
        value: str
    ):
        self.elements["username"].clear()
        self.elements["username"].send_keys(value)

    def readUsername(
        self
    ) -> str:
        return self.elements["username"].get_attribute("value")

    def testUsername(
        self,
        value: str
    ) -> bool:
        return self.readUsername().strip() == value
    
    def testUsernameError(
        self,
        value: str
    ) -> bool:
        self.elements["username"].send_keys(Keys.TAB)
        sleep(0.2)
        return self.elements["username_error"].get_attribute("innerText") == value

    def fillEmail(
        self,
        value: str
    ):
        self.elements["email"].clear()
        self.elements["email"].send_keys(value)

    def readEmail(
        self
    ) -> str:
        return self.elements["email"].get_attribute("value")

    def testEmail(
        self,
        value: str
    ) -> bool:
        return self.readEmail().strip() == value

    def testEmailError(
        self,
        value: str
    ) -> bool:
        self.elements["email"].send_keys(Keys.TAB)
        sleep(0.2)
        return self.elements["email_error"].get_attribute("innerText") == value

    def fillPassword(
        self,
        value: str
    ):
        self.elements["password"].clear()
        self.elements["password"].send_keys(value)

    def readPassword(
        self
    ) -> str:
        return self.elements["password"].get_attribute("value")

    def testPassword(
        self,
        value: str
    ) -> bool:
        return self.readPassword().strip() == value

    def testPasswordError(
        self,
        value: str
    ) -> bool:
        self.elements["password"].send_keys(Keys.TAB)
        sleep(0.2)
        return self.elements["password_error"].get_attribute("innerText") == value

    def fillPasswordConfirm(
        self,
        value: str
    ):
        self.elements["password_confirm"].clear()
        self.elements["password_confirm"].send_keys(value)

    def readPasswordConfirm(
        self
    ) -> str:
        return self.elements["password_confirm"].get_attribute("value")

    def testPasswordConfirm(
        self,
        value: str
    ) -> bool:
        return self.readPasswordConfirm().strip() == value

    def testPasswordConfirmError(
        self,
        value: str
    ) -> bool:
        self.elements["password_confirm"].send_keys(Keys.TAB)
        sleep(0.2)
        return self.elements["password_confirm_error"].get_attribute("innerText") == value

    def fillFirstName(
        self,
        value: str
    ):
        self.elements["first_name"].clear()
        self.elements["first_name"].send_keys(value)

    def readFirstName(
        self
    ) -> str:
        return self.elements["first_name"].get_attribute("value")

    def testFirstName(
        self,
        value: str
    ) -> bool:
        return self.readFirstName().strip() == value

    def testFirstNameError(
        self,
        value: str
    ) -> bool:
        self.elements["first_name"].send_keys(Keys.TAB)
        sleep(0.2)
        return self.elements["first_name_error"].get_attribute("innerText") == value

    def fillLastName(
        self,
        value: str
    ):
        self.elements["last_name"].clear()
        self.elements["last_name"].send_keys(value)

    def readLastName(
        self
    ) -> str:
        return self.elements["last_name"].get_attribute("value")

    def testLastName(
        self,
        value: str
    ) -> bool:
        return self.readLastName().strip() == value

    def testLastNameError(
        self,
        value: str
    ) -> bool:
        self.elements["last_name"].send_keys(Keys.TAB)
        sleep(0.2)
        return self.elements["last_name_error"].get_attribute("innerText") == value

    def fillPhoneNumber(
        self,
        value: str
    ):
        self.elements["phone_number"].clear()
        self.elements["phone_number"].send_keys(value)

    def readPhoneNumber(
        self
    ) -> str:
        return self.elements["phone_number"].get_attribute("value")

    def testPhoneNumber(
        self,
        value: str
    ) -> bool:
        return self.readPhoneNumber().strip() == value

    def testPhoneNumberError(
        self,
        value: str
    ) -> bool:
        self.elements["phone_number"].send_keys(Keys.TAB)
        sleep(0.2)
        return self.elements["phone_number_error"].get_attribute("innerText") == value

    def fillAddressCountry(
        self,
        value: str
    ):
        selector = Select(self.elements["address_country"])
        try:
            selector.select_by_visible_text(value)
        except NoSuchElementException as nsee:
            pass

    def readAddressCountry(
        self
    ) -> str:
        selector = Select(self.elements["address_country"])
        return selector.first_selected_option.get_attribute("innerText")

    def testAddressCountry(
        self,
        value: str
    ) -> bool:
        return self.readAddressCountry().strip() == value

    def fillAddressCity(
        self,
        value: str
    ):
        self.elements["address_city"].clear()
        self.elements["address_city"].send_keys(value)

    def readAddressCity(
        self
    ) -> str:
        return self.elements["address_city"].get_attribute("value")

    def testAddressCity(
        self,
        value: str
    ) -> bool:
        return self.readAddressCity().strip() == value

    def testAddressCityError(
        self,
        value: str
    ) -> bool:
        self.elements["address_city"].send_keys(Keys.TAB)
        sleep(0.2)
        return self.elements["address_city_error"].get_attribute("innerText") == value

    def fillAddressStreet(
        self,
        value: str
    ):
        self.elements["address_street"].clear()
        self.elements["address_street"].send_keys(value)

    def readAddressStreet(
        self
    ) -> str:
        return self.elements["address_street"].get_attribute("value")

    def testAddressStreet(
        self,
        value: str
    ) -> bool:
        return self.readAddressStreet().strip() == value

    def testAddressStreetError(
        self,
        value: str
    ) -> bool:
        self.elements["address_street"].send_keys(Keys.TAB)
        sleep(0.2)
        return self.elements["address_street_error"].get_attribute("innerText") == value

    def fillAddressRegion(
        self,
        value: str
    ):
        self.elements["address_region"].clear()
        self.elements["address_region"].send_keys(value)

    def readAddressRegion(
        self
    ) -> str:
        return self.elements["address_region"].get_attribute("value")

    def testAddressRegion(
        self,
        value: str
    ) -> bool:
        return self.readAddressRegion().strip() == value

    def testAddressRegionError(
        self,
        value: str
    ) -> bool:
        self.elements["address_region"].send_keys(Keys.TAB)
        sleep(0.2)
        return self.elements["address_region_error"].get_attribute("innerText") == value

    def fillAddressPostalCode(
        self,
        value: str
    ):
        self.elements["address_postal_code"].clear()
        self.elements["address_postal_code"].send_keys(value)

    def readAddressPostalCode(
        self
    ) -> str:
        return self.elements["address_postal_code"].get_attribute("value")

    def testAddressPostalCode(
        self,
        value: str
    ) -> bool:
        return self.readAddressPostalCode().strip() == value
    
    def testAddressPostalCodeError(
        self,
        value: str
    ) -> bool:
        self.elements["address_postal_code"].send_keys(Keys.TAB)
        sleep(0.2)
        return self.elements["address_postal_code_error"].get_attribute("innerText") == value

    def setOfferOptin(
        self,
        value: bool
    ):
        clickIf = (
            (value and not self.readOfferOptin())
            or (not value and self.readOfferOptin())
        )
        if clickIf:
            self.elements["offers_opt_in"].click()

    def readOfferOptin(
        self
    ) -> bool:
        return self.elements["offers_opt_in"].is_selected()

    def setTermsAndConditionsOptIn(
        self,
        value: bool
    ):
        clickIf = (
            (value and not self.readTermsAndConditionsOptIn())
            or (not value and self.readTermsAndConditionsOptIn())
        )
        if clickIf:
            self.elements["terms_and_conditions_opt_in"].click()

    def readTermsAndConditionsOptIn(
        self
    ) -> bool:
        return self.elements["terms_and_conditions_opt_in"].is_selected()
    
    def testTermsAndConditionsOptInError(self) -> bool:
        return not self.elements["register_button"].get_dom_attribute("disabled") is None

    def submitInfo(self):
        self.elements["register_button"].click()
        WebDriverWait(
            self.driverObj, 
            10
        ).until(
            EC.element_to_be_clickable(
                mainPageWideElementIDs["offer_button"].values()
            )
        )


class AccountSummaryPage(AdvantagePage):

    def __init__(self):
        super().__init__(
            loggedIn=True,
            extraDict=accountSummaryElementIDs
        )
        self.fieldKeys = list(self.elements.keys())
    
    def validateUserInfo(
        self,
        **kwargs
    ):
        summaryBlock = self.driverObj.find_elements(**accountSummaryElementIDs["details_box"])[0]
        dataItems = summaryBlock.find_elements(by=By.CLASS_NAME, value="ng-binding")
        for item in dataItems:
            innerText = item.get_attribute("innerText").strip()
            match item.get_dom_attribute("data-ng-hide"):
                case "accountDetails.homeAddress == ''":
                    compareStr = kwargs["addressStreet"]
                case "accountDetails.cityName == ''":
                    compareStr = kwargs["addressCity"]
                case "accountDetails.countryName == ''":
                    compareStr = kwargs["addressCountry"] 
                case "accountDetails.stateProvince == ''":
                    compareStr = kwargs["addressRegion"]
                case "accountDetails.zipcode == ''":
                    compareStr = kwargs["addressPostalCode"]
                case None:
                    isPhoneNumber = rematch(r'^[0-9\-]{10,20}$', innerText) is not None
                    # print(f"isPhoneNumber: {isPhoneNumber}")
                    if isPhoneNumber:
                        compareStr = kwargs["phoneNumber"]
                    else:
                        compareStr = " ".join([kwargs["firstName"], kwargs["lastName"]])
            # print(f"compareStr: '{compareStr}' innerText: '{innerText}'")
            if compareStr != innerText:
                # print(f"{'phoneNumber' if isPhoneNumber else 'fullName'} doesn't match!\n")
                return False
        return True

    def goToProfileEditPage(self):
        self.elements['account_details_link'].click()
        self.waitForElements(
            accountInfoEditPageElementIDs, 
            20
        )


class UserInfoEditPage(AdvantagePage):
    
    def __init__(
        self,
        loggedIn=True,
        extraDict=accountInfoEditPageElementIDs
    ):
        super().__init__(loggedIn=True)

    def getEmail(self) -> str:
        return self.elements['email'].get_attribute('value')

    def setEmail(self, value: str):
        self.elements['email'].clear()
        self.elements['email'].send_keys(value)

    def getFirstName(self) -> str:
        return self.elements['first_name'].get_attribute('value')

    def setFirstName(self, value: str):
        self.elements['first_name'].clear()
        self.elements['first_name'].send_keys(value)

    def getLastName(self) -> str:
        return self.elements['last_name'].get_attribute('value')

    def setLastName(self, value: str):
        self.elements['last_name'].clear()
        self.elements['last_name'].send_keys(value)

    def getPhoneNumber(self) -> str:
        return self.elements['phone_number'].get_attribute('value')

    def setPhoneNumber(self, value: str):
        self.elements['phone_number'].clear()
        self.elements['phone_number'].send_keys(value)

    def getAddressCountry(self) -> str:
        tempSelect = Select(self.elements['address_country'])
        return tempSelect.first_selected_option

    def setAddressCountry(self, value: str):
        self.elements['address_country'].clear()
        self.elements['address_country'].send_keys(value)

    def getAddressCity(self) -> str:
        return self.elements['address_city'].get_attribute('value')

    def setAddressCity(self, value: str):
        self.elements['address_city'].clear()
        self.elements['address_city'].send_keys(value)

    def getAddressStreet(self) -> str:
        return self.elements['address_street'].get_attribute('value')

    def setAddressStreet(self, value: str):
        self.elements['address_street'].clear()
        self.elements['address_street'].send_keys(value)

    def getAddressPostalCode(self) -> str:
        return self.elements['address_postal_code'].get_attribute('value')

    def setAddressPostalCode(self, value: str):
        self.elements['address_postal_code'].clear()
        self.elements['address_postal_code'].send_keys(value)

    def getAddressRegion(self) -> str:
        return self.elements['address_region'].get_attribute('value')

    def setAddressRegion(self, value: str):
        self.elements['address_region'].clear()
        self.elements['address_region'].send_keys(value)

    def saveInfo(self):
        self.elements['save_button'].click()
        self.waitForElements(
            accountSummaryElementIDs,
            20
        )