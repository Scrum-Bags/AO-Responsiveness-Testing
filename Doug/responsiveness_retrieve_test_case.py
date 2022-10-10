from itertools import chain
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains

from runittest.reporting_unittest import ReportingTestCase
from page_elements.advantage_online_elements import *
from advantage_pages import *
from printlogger.printlogger import displayPrint


class RetrieveInfoResponsivenessTestCase(ReportingTestCase):

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
        displayPrint(f"case data: {self.data}")
    
    def setUp(self):
        pass

    def testUserRetrieveInfoResponsiveLayout(self):
        # Go to main page
        self.driverObj.get("http://www.advantageonlineshopping.com/#/")
        mainPage = MainPage(loggedIn=False)

        # Log in
        mainPage.logIn(
            self.data['username'],
            self.data['password']
        )

        # get main page object
        mainPage = MainPage(loggedIn=True)

        # Go to account summary page
        displayPrint("Going to account page")
        mainPage.goToUserProfile()

        # get page object
        summaryPage = AccountSummaryPage()

        # go to info edit page
        displayPrint("Going to profile edit page")
        summaryPage.goToProfileEditPage()

        # get edit page object
        editPage = UserInfoEditPage()

        # test edit page responsiveness
        displayPrint("Testing edit page responsiveness")
        self._testAccountInfoEditPageResponsiveLayout()

        # validate info against known
        editPage = UserInfoEditPage()
        # email
        testStatus = self.data['email'] == editPage.getEmail()
        self.reportStep(
            "Email field value check",
            "Email field matches expected value",
            "Email field does not match expected value",
            testStatus,
            element=editPage.elements['email'],
            imageEmbed=True,
            data=['email']
        )
        # first name
        testStatus = self.data['firstName'] == editPage.getFirstName()
        self.reportStep(
            "First name field value check",
            "First name field matches expected value",
            "First name field does not match expected value",
            testStatus,
            element=editPage.elements['first_name'],
            imageEmbed=True,
            data=['firstName']
        )
        # last name
        testStatus = self.data['lastName'] == editPage.getLastName()
        self.reportStep(
            "Last name field value check",
            "Last name field matches expected value",
            "Last name field does not match expected value",
            testStatus,
            element=editPage.elements['last_name'],
            imageEmbed=True,
            data=['lastName']
        )
        # phone number
        testStatus = self.data['phoneNumber'] == editPage.getPhoneNumber()
        self.reportStep(
            "Phone number field value check",
            "Phone number field matches expected value",
            "Phone number field does not match expected value",
            testStatus,
            element=editPage.elements['phone_number'],
            imageEmbed=True,
            data=['phoneNumber']
        )
        # address country 
        testStatus = self.data['addressCountry'] == editPage.getAddressCountry()
        self.reportStep(
            "Address country selector value check",
            "Address country selector matches expected value",
            "Address country selector does not match expected value",
            testStatus,
            element=editPage.elements['address_country'],
            imageEmbed=True,
            data=['addressCountry']
        )
        # address city 
        testStatus = self.data['addressCity'] == editPage.getAddressCity()
        self.reportStep(
            "Address city field value check",
            "Address city field matches expected value",
            "Address city field does not match expected value",
            testStatus,
            element=editPage.elements['address_city'],
            imageEmbed=True,
            data=['addressCity']
        )
        # address street 
        testStatus = self.data['addressStreet'] == editPage.getAddressStreet()
        self.reportStep(
            "Address street field value check",
            "Address street matches expected value",
            "Address street does not match expected value",
            testStatus,
            element=editPage.elements['address_street'],
            imageEmbed=True,
            data=['addressStreet']
        )
        # address postal code 
        testStatus = self.data['addressPostalCode'] == editPage.getAddressPostalCode()
        self.reportStep(
            "Address postal code field value check",
            "Address postal code matches expected value",
            "Address postal code does not match expected value",
            testStatus,
            element=editPage.elements['address_postal_code'],
            imageEmbed=True,
            data=['addressPostalCode']
        )
        # address region 
        testStatus = self.data['addressRegion'] == editPage.getAddressRegion()
        self.reportStep(
            "Address region field value check",
            "Address region matches expected value",
            "Address region does not match expected value",
            testStatus,
            element=editPage.elements['address_region'],
            imageEmbed=True,
            data=['addressRegion']
        )

        # Return to summary page
        displayPrint("Going to user profile summary")
        editPage.goToUserProfile()

        # get page object
        displayPrint("Getting summary page object")
        summaryPage = AccountSummaryPage()

        # test page responsiveness
        self._testAccountPageResponsiveLayout()

        # validate info against display
        testStatus = summaryPage.validateUserInfo(**self.data)
        self.reportStep(
            "Summary page info match check",
            "Account info matches summary info",
            "Account info does not match summary info",
            testStatus,
            element="screen",
            data=['email', 'firstName', 'lastName', 'phoneNumber', 'addressCountry', 'addressCity', 'addressStreet', 'addressPostalCode', 'addressRegion']
        )

        # logout
        summaryPage.logOut()

    def tearDown(self):
        pass
    
    def runTest(self):
        self.testUserRetrieveInfoResponsiveLayout()

    def _testAccountPageResponsiveLayout(self):
        # Set window size to mobile size (<464px?)
        self._setWindowMobileDimensions()

        # Get page object
        accountPage = AccountSummaryPage()

        # TODO Check that elements are sized to match

        # Check that mobile elements are displayed
        self._mobileElementsDisplayedCheck()

        # Set window size to maximum
        self._setWindowMaxDimensions()

        # Get page object
        accountPage = AccountSummaryPage()

        # TODO Check that elements are sized to match

        # Check that mobile elements are not displayed
        self._mobileElementsNotDisplayedCheck()
    
    def _testAccountInfoEditPageResponsiveLayout(self):
        # Set window size to mobile size (<464px?)
        self._setWindowMobileDimensions()

        # Get page object
        editPage = UserInfoEditPage()

        # TODO Check that elements are sized to match

        # Check that mobile elements are displayed
        self._mobileElementsDisplayedCheck()

        # Set window size to maximum
        self._setWindowMaxDimensions()

        # Get page object
        editPage = UserInfoEditPage()

        # TODO Check that elements are sized to match

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
