from re import match as rematch
from time import sleep
from typing import Union

from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

from page_elements.advantage_online_elements import accountSummaryElementIDs
from page_elements.advantage_online_elements import commonElementIDs
from page_elements.advantage_online_elements import commonMobileElementIDs
from page_elements.advantage_online_elements import loggedOutCommonElementIDs
from page_elements.advantage_online_elements import loggedInCommonElementIDs
from page_elements.advantage_online_elements import mainPageWaitIDs
from page_elements.advantage_online_elements import mainPageWideElementIDs
from page_elements.advantage_online_elements import userRegisterElementIDs
from runittest.reporting_unittest import SingletonWebDriver


class Page:
    """Base page class to handle basic object inclusion."""

    def __init__(
        self,
        idDict: dict,
        extraDict: Union[dict, None] = None
    ):
        self.elements = {}
        tempDict = idDict
        if extraDict is not None:
            tempDict.update(extraDict)
        self.driverObj = SingletonWebDriver()
        # print(f"Getting wait key from idDict: {idDict}")
        waitObjectID = idDict[list(idDict.keys())[0]]
        # print(f"Have key: {waitObjectID}")
        # print("Waiting for page to load")
        WebDriverWait(
            self.driverObj,
            10
        ).until(
            EC.presence_of_element_located((waitObjectID.values()))
        )
        # print("Page has loaded!")
        self.addElements(tempDict)

    def addElements(self, idDict: dict):
        # print("Adding Elements")
        for name, args in idDict.items():
            # temp_element = None
            try:
                # print(f"trying to find: {name}: {args}")
                # temp_element = self.driverObj.find_element(**args)
                self.elements[name] = self.driverObj.find_element(**args)
                # setattr(self, name, temp_element)
            except NoSuchElementException as e:
                # print(f"error!: element not found: {e}")
                continue
        # print("Elements Added")


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
        super().__init__(
            idDict=baseDict,
            extraDict=extraDict
        )
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
        if EC.visibility_of(
            commonMobileElementIDs["mobile_sidebar_button"]
        ):
            self.driverObj.find_element(
                commonMobileElementIDs["mobile_sidebar_button"]
            ).click()
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
            extraDict=mainPageWaitIDs
        )
        WebDriverWait(
            self.driverObj,
            10
        ).until(
            EC.all_of(
                EC.visibility_of_element_located(
                    mainPageWaitIDs["headphones_image"].values()
                ),
                EC.visibility_of_element_located(
                    mainPageWaitIDs["laptops_image"].values()
                ),
                EC.visibility_of_element_located(
                    mainPageWaitIDs["mice_image"].values()
                ),
                EC.visibility_of_element_located(
                    mainPageWaitIDs["speakers_image"].values()
                ),
                EC.visibility_of_element_located(
                    mainPageWaitIDs["tablets_image"].values()
                )
            )
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
        selector.select_by_visible_text(value)

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
                mainPageElementIDs["offer_button"].values()
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
