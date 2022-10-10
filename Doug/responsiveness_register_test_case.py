from itertools import chain
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains

from runittest.reporting_unittest import ReportingTestCase
from page_elements.advantage_online_elements import *
from advantage_pages import *


class RegisterResponsivenessTestCase(ReportingTestCase):

    _mainPageMobileDims = {
        "width": 463,
        "height": 720
    }

    _registerPageMobileDims = {
        "width": 751,
        "height": 720
    }

    _accountPageMobileDims = {
        "width": 460,
        "height": 720
    }

    def __init__(
        self,
        testCaseID,
        testCaseDescription,
        **kwargs
    ):
        super().__init__(
            testCaseID,
            testCaseDescription,
            **kwargs
        )
    
    def setUp(self):
        pass

    def testUserRegisterResponsiveLayout(self):
        # Go to main page
        self.driverObj.get("http://www.advantageonlineshopping.com/#/")
        mainPage = MainPage(loggedIn=False)
        self._testMainPageResponsiveLayout()

        # # Go to register page
        mainPage.goToUserRegistration()
        self._testRegisterPageResponsiveLayout()

        # Fill out new user info
        # Get the page object
        registerPage = RegisterPage()

        # Report that page loaded
        self.reportEvent(
            "User Registration Page Loaded",
            element="screen"
        )

        # Put data into fields
        # Input Username
        if self.data["expectedErrorField"] in ["", "username", "termsAndConditionsOptIn"]:
            registerPage.fillUsername(self.data["username"])
            self.reportEvent(
                "Username field filled",
                data=["username"],
                element=registerPage.elements["username"],
                imageEmbed=True
            )
            # Check for input errors
            if self.data["expectedErrorField"] == "username":
                sleep(0.3)
                testStatus = registerPage.testUsernameError(self.data["expectedError"])
                self.reportStep(
                    "Username input field check",
                    f"Error message '{self.data['expectedError']}' is displayed",
                    f"Error message not displayed",
                    testStatus,
                    imageEmbed=True,
                    element=registerPage.elements["username_error"]
                )
                return
            
        # Input Email
        if self.data["expectedErrorField"] in ["", "email", "termsAndConditionsOptIn"]:
            registerPage.fillEmail(self.data["email"])
            self.reportEvent(
                "Email field filled",
                data=["email"],
                element=registerPage.elements["email"],
                imageEmbed=True
            )
            # Check for input errors
            if self.data["expectedErrorField"] == "email":
                sleep(0.3)
                testStatus = registerPage.testEmailError(self.data["expectedError"])
                self.reportStep(
                    "Email input field check",
                    f"Error message '{self.data['expectedError']}' is displayed",
                    f"Error message not displayed",
                    testStatus,
                    imageEmbed=True,
                    element=registerPage.elements["email_error"]
                )
                return

        # Input Password
        if self.data["expectedErrorField"] in ["", "password", "passwordConfirm", "termsAndConditionsOptIn"]:
            registerPage.fillPassword(self.data["password"])
            self.reportEvent(
                "Pasword field filled",
                data=["password"],
                element=registerPage.elements["password"],
                imageEmbed=True
            )
            # Check for input errors
            if self.data["expectedErrorField"] == "password":
                sleep(0.3)
                testStatus = registerPage.testPasswordError(self.data["expectedError"])
                self.reportStep(
                    "Password input field check",
                    f"Error message '{self.data['expectedError']}' is displayed",
                    f"Error message not displayed",
                    testStatus,
                    imageEmbed=True,
                    element=registerPage.elements["password_error"]
                )
                return

        # Input Password Confirmation
        if self.data["expectedErrorField"] in ["", "passwordConfirm", "termsAndConditionsOptIn"]:
            registerPage.fillPasswordConfirm(self.data["passwordConfirm"])
            self.reportEvent(
                "Confirm Password field filled",
                data=["passwordConfirm"],
                element=registerPage.elements["password_confirm"],
                imageEmbed=True
            )
            # Check for input errors
            if self.data["expectedErrorField"] == "passwordConfirm":
                sleep(0.3)
                testStatus = registerPage.testPasswordConfirmError(self.data["expectedError"])
                self.reportStep(
                    "Confirm Password input field check",
                    f"Error message '{self.data['expectedError']}' is displayed",
                    f"Error message not displayed",
                    testStatus,
                    imageEmbed=True,
                    element=registerPage.elements["password_confirm_error"]
                )
                return

        # Input First Name
        if self.data["expectedErrorField"] in ["", "firstName"]:
            registerPage.fillFirstName(self.data["firstName"])
            self.reportEvent(
                "First Name field filled",
                data=["firstName"],
                element=registerPage.elements["first_name"],
                imageEmbed=True
            )
            # Check for input errors
            if self.data["expectedErrorField"] == "firstName":
                sleep(0.3)
                testStatus = registerPage.testFirstNameError(self.data["expectedError"])
                self.reportStep(
                    "First Name input field check",
                    f"Error message '{self.data['expectedError']}' is displayed",
                    f"Error message not displayed",
                    testStatus,
                    imageEmbed=True,
                    element=registerPage.elements["first_name_error"]
                )
                return

        # Input Last Name
        if self.data["expectedErrorField"] in ["", "lastName"]:
            registerPage.fillLastName(self.data["lastName"])
            self.reportEvent(
                "Last Name field filled",
                data=["lastName"],
                element=registerPage.elements["last_name"],
                imageEmbed=True
            )
            # Check for input errors
            if self.data["expectedErrorField"] == "lastName":
                sleep(0.3)
                testStatus = registerPage.testLastNameError(self.data["expectedError"])
                self.reportStep(
                    "Last Name input field check",
                    f"Error message '{self.data['expectedError']}' is displayed",
                    f"Error message not displayed",
                    testStatus,
                    imageEmbed=True,
                    element=registerPage.elements["last_name_error"]
                )
                return

        # Input Phone Number
        if self.data["expectedErrorField"] in ["", "phoneNumber"]:
            registerPage.fillPhoneNumber(self.data["phoneNumber"])
            self.reportEvent(
                "Phone Number field filled",
                data=["phoneNumber"],
                element=registerPage.elements["phone_number"],
                imageEmbed=True
            )
            # Check for input errors
            if self.data["expectedErrorField"] == 'phoneNumber':
                sleep(0.3)
                testStatus = registerPage.testPhoneNumberError(self.data["expectedError"])
                self.reportStep(
                    "PhoneNumber input field check",
                    f"Error message '{self.data['expectedError']}' is displayed",
                    f"Error message not displayed",
                    testStatus,
                    imageEmbed=True,
                    element=registerPage.elements["phone_number_error"]
                )
                return

        # Input Address Country
        if self.data["expectedErrorField"] == '':
            registerPage.fillAddressCountry(self.data["addressCountry"])
            self.reportEvent(
                "Address Country field filled",
                data=["addressCountry"],
                element=registerPage.elements["address_country"],
                imageEmbed=True
            )

        # Input Address City
        if self.data["expectedErrorField"] in ["", "addressCity"]:
            registerPage.fillAddressCity(self.data["addressCity"])
            self.reportEvent(
                "Address City field filled",
                data=["addressCity"],
                element=registerPage.elements["address_city"],
                imageEmbed=True
            )
            # Check for input errors
            if self.data["expectedErrorField"] == "addressCity":
                sleep(0.3)
                testStatus = registerPage.testAddressCityError(self.data["expectedError"])
                self.reportStep(
                    "Address City input field check",
                    f"Error message '{self.data['expectedError']}' is displayed",
                    f"Error message not displayed",
                    testStatus,
                    imageEmbed=True,
                    element=registerPage.elements["address_city_error"]
                )
                return

        # Input Address Street
        if self.data["expectedErrorField"] in ["", "addressStreet"]:
            registerPage.fillAddressStreet(self.data["addressStreet"])
            self.reportEvent(
                "Address Street field filled",
                data=["addressStreet"],
                element=registerPage.elements["address_street"],
                imageEmbed=True
            )
            # Check for input errors
            if self.data["expectedErrorField"] == "addressStreet":
                sleep(0.3)
                testStatus = registerPage.testAddressStreetError(self.data["expectedError"])
                self.reportStep(
                    "Address Street input field check",
                    f"Error message '{self.data['expectedError']}' is displayed",
                    f"Error message not displayed",
                    testStatus,
                    imageEmbed=True,
                    element=registerPage.elements["address_street_error"]
                )
                return

        # Input Address Region
        if self.data["expectedErrorField"] in ["", "addressRegion"]:
            registerPage.fillAddressRegion(self.data["addressRegion"])
            self.reportEvent(
                "Address Region field filled",
                data=["addressRegion"],
                element=registerPage.elements["address_region"],
                imageEmbed=True
            )
            # Check for input errors
            if self.data["expectedErrorField"] == "addressRegion":
                sleep(0.3)
                testStatus = registerPage.testAddressRegionError(self.data["expectedError"])
                self.reportStep(
                    "Address Region input field check",
                    f"Error message '{self.data['expectedError']}' is displayed",
                    f"Error message not displayed",
                    testStatus,
                    imageEmbed=True,
                    element=registerPage.elements["address_region_error"]
                )
                return

        # Input Address Postal Code
        if self.data["expectedErrorField"] in ["", "addressPostalCode"]:
            registerPage.fillAddressPostalCode(self.data["addressPostalCode"])
            self.reportEvent(
                "Address Postal Code field filled",
                data=["addressPostalCode"],
                element=registerPage.elements["address_postal_code"],
                imageEmbed=True
            )
            # Check for input errors
            if self.data["expectedErrorField"] == "addressPostalCode":
                sleep(0.3)
                testStatus = registerPage.testAddressPostalCodeError(self.data["expectedError"])
                self.reportStep(
                    "Address Postal Code input field check",
                    f"Error message '{self.data['expectedError']}' is displayed",
                    f"Error message not displayed",
                    testStatus,
                    imageEmbed=True,
                    element=registerPage.elements["address_postal_code_error"]
                )
                return

        # Input Offers Opt In selection
        if self.data["expectedErrorField"] == '':
            registerPage.setOfferOptin(self.data["offersOptIn"])
            self.reportEvent(
                "Offers Opt In selected",
                data=["offersOptIn"],
                element=registerPage.elements["offers_opt_in"],
                imageEmbed=True
            )

        # Input Terms And Conditions selection
        if self.data["expectedErrorField"] in ["", "termsAndConditionsOptIn"]:
            registerPage.setTermsAndConditionsOptIn(self.data["termsAndConditionsOptIn"])
            self.reportEvent(
                "Terms And Conditions Opt In selected",
                data=["termsAndConditionsOptIn"],
                element=registerPage.elements["terms_and_conditions_opt_in"],
                imageEmbed=True
            )
            # Check for register button being active
            if self.data["expectedErrorField"] == "termsAndConditionsOptIn":
                sleep(0.3)
                testStatus = registerPage.testTermsAndConditionsOptInError()
                self.reportStep(
                    "Terms And Conditions Opt In check box check",
                    f"Register button is not active",
                    f"Register button is active",
                    testStatus,
                    element=registerPage.elements["register_button"],
                    imageEmbed=True
                )
                return

        # Click register button
        registerPage.submitInfo()  # Waits for the main page to load

    def tearDown(self):
        mainPage = MainPage(loggedIn=True)
        mainPage.logOut()
    
    def runTest(self):
        self.testUserRegisterResponsiveLayout()

    def _testMainPageResponsiveLayout(self):
        # Set window size to mobile size (<464px?)
        self._setWindowMobileDimensions()

        # Get a page object
        mainPage = MainPage(loggedIn=False)

        # Check that elements are sized to match
        for ID in mainPageWaitIDs.keys():
            element = self.driverObj.find_element(**mainPageWaitIDs[ID])
            targetWidth = self.driverObj.find_element(**commonElementIDs['body']).size['width']
            testStatus = element.size['width'] == targetWidth
            self.reportStep(
                f"'{ID}' element width check, page is {targetWidth}px wide",
                f"'{ID}' element is {element.size['width']}px wide",
                f"Failure! '{ID}' element is {element.size['width']}px wide",
                testStatus,
                element=element
            )
        
        # Check that offer is not displayed
        offerElementIDs = mainPageWideElementIDs["offer_button"]
        offerElement = self.driverObj.find_element(
            **offerElementIDs
        )
        self.reportStep(
            "Offer not displayed check", 
            "Offer is not displayed", 
            "Offer is displayed", 
            not offerElement.is_displayed(),
        )

        # Check that mobile elements are displayed
        self._mobileElementsDisplayedCheck()

        # Set window size to maximum
        self._setWindowMaxDimensions()

        # Get a page object
        mainPage = MainPage(loggedIn=False)

        # Check that elements are sized to match
        imageWidths = {
            n: self.driverObj.find_element(**mainPageWaitIDs[n]).size['width'] for n in [
                'speakers_image',
                'tablets_image',
                'laptops_image',
                'mice_image',
                'headphones_image'
            ]
        }
        bodyWidth = self.driverObj.find_element(**commonElementIDs['body']).size['width']

        # Get row width sums
        topRowWidth = imageWidths['speakers_image'] + imageWidths['tablets_image'] + imageWidths['headphones_image']
        bottomRowWidth = imageWidths['laptops_image'] + imageWidths['mice_image'] + imageWidths['headphones_image']
        # Check that top row and headphones sum to window width
        testStatus = abs(topRowWidth - bodyWidth) < 2.0
        self.reportStep(
            "Top images row width check",
            f"Sum of row widths {topRowWidth} is the same as the window width: {bodyWidth}",
            f"Sum of row widths {topRowWidth} is not quite the same as the window width: {bodyWidth}",
            testStatus
        )
        # Check that bottom row and headphone sum to window width
        testStatus = abs(bottomRowWidth - bodyWidth) < 2.0
        self.reportStep(
            "Bottom images row width check",
            f"Sum of row widths {bottomRowWidth} is the same as the window width: {bodyWidth}",
            f"Sum of row widths {bottomRowWidth} is not quite the same as the window width: {bodyWidth}",
            testStatus
        )
        # Check that ratio between others and headphones is ~ 1.0625
        for otherName, other, headphones in [
            (w, float(imageWidths[w]), float(imageWidths['headphones_image'])) 
            for w in [
                'speakers_image', 
                'tablets_image',
                'laptops_image',
                'mice_image'
            ]
        ]:
            ratio = other / headphones
            testStatus = abs(ratio) - 1.0625 < 0.05
            self.reportStep(
                "Images width ratio check",
                f"Ratio {ratio} between {otherName} ({other}px) and headphones image ({headphones}px) is ~1.0625",
                f"Ratio {ratio} between {otherName} ({other}px) and headphones image ({headphones}px) is not ~1.0625",
                testStatus
            )

        # Check that mobile elements are not displayed
        self._mobileElementsNotDisplayedCheck()
        
        # Check that offer is displayed
        offerElement = self.driverObj.find_element(
            **mainPageWideElementIDs["offer_button"]
        )
        self.reportStep(
            "Offer displayed check", 
            "Offer is displayed", 
            "Offer is not displayed", 
            offerElement.is_displayed(),
            element='screen'
        )

    def _testRegisterPageResponsiveLayout(self):
        # Set window size to mobile size (<464px?)
        self._setWindowMobileDimensions()

        # Get page object
        registerPage = RegisterPage()

        # Check that vertical positions are distinct and in expected order
        orderedFields = [
            'username',
            'email',
            'password',
            'password_confirm',
            'first_name',
            'last_name',
            'phone_number',
            'address_country',
            'address_city',
            'address_street',
            'address_region',
            'address_postal_code'
        ]
        fieldVerticalPositions = {
            i: self.driverObj.find_element(**userRegisterElementIDs[n]).location['y']
            for i, n in enumerate(orderedFields)
        }
        for a, b in zip(
            range(0, len(orderedFields) - 1),
            range(1, len(orderedFields))
        ):
            testStatus = fieldVerticalPositions[a] < fieldVerticalPositions[b]  # NB top of page y = 0, so smaller is higher
            element = self.driverObj.find_element(**userRegisterElementIDs[orderedFields[b]])
            self.driverObj.execute_script('arguments[0].scrollIntoView(false);', element)
            self.reportStep(
                "Relative field position check", 
                f"{orderedFields[a]} field is higher (y={fieldVerticalPositions[a]}) than {orderedFields[b]} field (y={fieldVerticalPositions[b]})", 
                f"{orderedFields[a]} field is not higher (y={fieldVerticalPositions[a]}) than {orderedFields[b]} field (y={fieldVerticalPositions[b]})", 
                testStatus,
                element='screen'
            )

        # Check that mobile elements are displayed
        self._mobileElementsDisplayedCheck()

        # Set window size to maximum
        self._setWindowMaxDimensions()

        # Get page object
        registerPage = RegisterPage()

        # Check that vertical positions are now similar for pairs
        fieldParallels = [
            ('username', 'email'),
            ('password', 'password_confirm'),
            ('first_name', 'last_name'),
            ('address_country', 'address_city'),
            ('address_street', 'address_region')
        ]
        fieldVerticalPositions = {
            n: self.driverObj.find_element(**userRegisterElementIDs[n]).location['y']
            for n in chain(orderedFields)
        }
        for a, b in fieldParallels:
            testStatus = fieldVerticalPositions[a] == fieldVerticalPositions[b]
            element = self.driverObj.find_element(**userRegisterElementIDs[a])
            self.driverObj.execute_script('arguments[0].scrollIntoView(false);', element)
            self.reportStep(
                "Parallel field position check", 
                f"{a} field (y={fieldVerticalPositions[a]}) is parallel to field {b} (y={fieldVerticalPositions[b]})", 
                f"{a} field (y={fieldVerticalPositions[a]}) is not parallel to field {b} (y={fieldVerticalPositions[b]})", 
                testStatus,
                element='screen'
            )

        # Check that mobile elements are not displayed
        self._mobileElementsNotDisplayedCheck()

    def _setWindowMobileDimensions(self):
        self.driverObj.set_window_size(**self._mainPageMobileDims)
        self.reportEvent(
            "Window sized to mobile dimensions",
            element='screen',
            data='<br>'.join([f"{k}: {v}" for k, v in self._mainPageMobileDims.items()])
        )

    def _setWindowMaxDimensions(self):
        self.driverObj.maximize_window()
        self.reportEvent(
            "Window maximized",
            element='screen'
        )

    def _mobileElementsDisplayedCheck(self):
        page = AdvantagePage(loggedIn=False)
        testStatus = page.mobileElementsDisplayed()
        self.reportStep(
            "Mobile elements displayed check",
            "Mobile elements are displayed",
            "Mobile elements are not displayed",
            testStatus,
            element='screen'
        )

    def _mobileElementsNotDisplayedCheck(self):
        page = AdvantagePage(loggedIn=False)
        testStatus = not page.mobileElementsDisplayed()
        self.reportStep(
            "Mobile elements not displayed check",
            "Mobile elements are not displayed",
            "Mobile elements are displayed",
            testStatus,
            element='screen'
        )
