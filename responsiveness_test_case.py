from time import sleep

from runittest.reporting_unittest import ReportingTestCase

from advantage_pages import AdvantagePage
from advantage_pages import MainPage
from advantage_pages import RegisterPage
from advantage_pages import AccountSummaryPage

class ResponsivenessTestCase(ReportingTestCase):

    _mobileDims = {
        "width": 463,
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
        mainPage.goToUserRegistration()
        self._testMainPageResponsiveLayout()

        # Go to register page
        registerPage = RegisterPage()
        self._testRegisterPageResponsiveLayout()
        # Fill out new user info

        # Go to account summary page
        mainPage = MainPage(loggedIn=True)
        mainPage.goToUserProfile()
        self._testAccountPageResponsiveLayout()

    def tearDown(self):
        pass
    
    def runTest(self):
        self.testUserRegisterResponsiveLayout()

    def _testMainPageResponsiveLayout(self):
        # Set window size to mobile size (<464px?)
        self._setWindowMobileDimensions()

        # Get a page object
        mainPage = MainPage(loggedIn=False)

        # TODO Check that elements are sized to match

        # Check that mobile elements are displayed
        self._mobileElementsDisplayedCheck()

        # Set window size to maximum
        self._setWindowMaxDimensions()

        # Get a page object
        mainPage = MainPage(loggedIn=False)

        # TODO Check that elements are sized to match

        # Check that mobile elements are not displayed
        self._mobileElementsNotDisplayedCheck()

    def _testRegisterPageResponsiveLayout(self):
        # Set window size to mobile size (<464px?)
        self._setWindowMobileDimensions()

        # Get page object
        registerPage = RegisterPage()

        # TODO Check that elements are sized to match

        # Check that mobile elements are displayed
        self._mobileElementsDisplayedCheck()

        # Set window size to maximum
        self._setWindowMaxDimensions()

        # Get page object
        registerPage = RegisterPage()

        # TODO Check that elements are sized to match

        # Check that mobile elements are not displayed
        self._mobileElementsNotDisplayedCheck()

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

    def _setWindowMobileDimensions(self):
        self.driverObj.set_window_size(**self._mobileDims)
        self.reportEvent(
            "Window sized to mobile dimensions",
            element='screen',
            data='\n'.join([f"{k}: {v}" for k, v in self._mobileDims.items()])
        )

    def _setWindowMaxDimensions(self):
        self.driverObj.maximize_window()
        self.reportEvent(
            "Window maximized",
            element='screen'
        )

    def _mobileElementsDisplayedCheck(self):
        self.reportStep(
            "Mobile elements displayed check",
            "Mobile elements are displayed",
            "Mobile elements are not displayed",
            mainPage.mobileElementsDisplayed(),
            element='screen'
        )

    def _mobileElementsNotDisplayedCheck(self):
        self.reportStep(
            "Mobile elements not displayed check",
            "Mobile elements are not displayed",
            "Mobile elements are displayed",
            not mainPage.mobileElementsDisplayed(),
            element='screen'
        )