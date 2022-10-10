from itertools import chain
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains

from runittest.reporting_unittest import ReportingTestCase
from page_elements.advantage_online_elements import *
from advantage_pages import *


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
    
    def setUp(self):
        pass

    def testUserRetrieveInfoResponsiveLayout(self):
        # Go to main page
        self.driverObj.get("http://www.advantageonlineshopping.com/#/")
        mainPage = MainPage(loggedIn=False)
        self._testMainPageResponsiveLayout()

        # Log in
        mainPage.logIn(
            self.data['username'],
            self.data['password']
        )

        # Go to account summary page
        mainPage = MainPage(loggedIn=True)

        # Go to account summary page
        mainPage.goToUserProfile()

        # get page object
        summaryPage = AccountSummaryPage()

        # go to info edit page
        summaryPage.goToProfileEditPage()

        # get edit page object
        editPage = UserInfoEditPage()

        # test edit page responsiveness
        self._testAccountInfoEditPageResponsiveLayout()

        # validate info against known

        # Return to summary page
        editPage.goToUserProfile()

        # get page object
        summaryPage = AccountSummaryPage()

        # test page responsiveness
        self._testAccountPageResponsiveLayout()

        # validate info against display

        # logout

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
        accountPage = AccountSummaryPage()

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
