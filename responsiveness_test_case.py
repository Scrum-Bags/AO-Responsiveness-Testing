from time import sleep

from runittest.reporting_unittest import ReportingTestCase

from page_elements.advantage_online_elements import mainPageWideElementIDs
from page_elements.advantage_online_elements import mainPageWaitIDs
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
        self._testMainPageResponsiveLayout()
        mainPage.goToUserRegistration()

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

        # Check that elements are sized to match
        for ID in mainPageWaitIDs.keys():
            element = self.driverObj.find_element(mainPageIDs[ID])
            testStatus = element.size()['width'] == self._mobileDims['width'] 
            targetWidth = self._mobileDims["width"]
            self.reportStep(
                f"'{ID}' element width check",
                f"'{ID}' element is {targetWidth}px wide",
                f"Failure! '{ID}' element is {targetWidth}px wide",
                testStatus,
                element=element
            )
        
        # Check that offer is not displayed
        offerElement = self.driverObj.find_element(
            **mainPageWideElementIDs["offer_button"]
        )
        self.reportStep(
            "Offer not displayed check", 
            "Offer is not displayed", 
            "Offer is displayed", 
            not offerElement.is_displayed(),
            element=offerElement
        )

        # Check that mobile elements are displayed
        self._mobileElementsDisplayedCheck()

        # Set window size to maximum
        self._setWindowMaxDimensions()

        # Get a page object
        mainPage = MainPage(loggedIn=False)

        # Check that elements are sized to match
        speakersWidth = self.driverObj.find_element(mainPageWaitIDs["speakers_image"])
        tabletsWidth = self.driverObj.find_element(mainPageWaitIDs["tablets_image"])
        laptopsWidth = self.driverObj.find_element(mainPageWaitIDs["laptops_image"])
        miceWidth = self.driverObj.find_element(mainPageWaitIDs["mice_image"])
        headphonesWidth = self.driverObj.find_element(mainPageWaitIDs["headphones_image"])
        windowWidth = self.driverObj.size()['width'] 

        # Check that top row and headphones sum to window width
        topRowWidth = speakersWidth + tabletsWidth + headphonesWidth
        bottomRowWidth = laptopsWidth + miceWidth + headphonesWidth
        testStatus = abs(topRowWidth - windowWidth) < 2.0
        self.reportStep(
            "Top images row width check",
            f"Sum of row widths {topRowWidth} is the same as the window width: {windowWidth}",
            f"Sum of row widths {topRowWidth} is not quite the same as the window width: {windowWidth}",
            testStatus
        )
        # Check that bottom row and headphone sum to window width
        testStatus = abs(bottomRowWidth - windowWidth) < 2.0
        self.reportStep(
            "Bottom images row width check",
            f"Sum of row widths {bottomRowWidth} is the same as the window width: {windowWidth}",
            f"Sum of row widths {bottomRowWidth} is not quite the same as the window width: {windowWidth}",
            testStatus
        )
        # Check that ratio between others and headphones is ~ 1.0625
        for other, headphones in [
            (float(w), float(headphonesWidth)) 
            for w in [
                speakersWidth, 
                tabletsWidth, 
                laptopsWidth, 
                headphonesWidth
                ]
        ]:
            ratio = other / headphones
            testStatus = abs(ratio) - 1.0625 < 0.2
            self.reportStep(
                "Images width ratio check",
                f"Ratio {ratio} between other image {other} and headphones image {headphones} is ~1.0625",
                f"Ratio {ratio} between other image {other} and headphones image {headphones} is not ~1.0625",
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
            element=offerElement
        )

    def _testRegisterPageResponsiveLayout(self):
        # Set window size to mobile size (<464px?)
        self._setWindowMobileDimensions()

        # Get page object
        registerPage = RegisterPage()

        # TODO Check that elements are reordered

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
        testStatus = mainPage.mobileElementsDisplayed()
        self.reportStep(
            "Mobile elements displayed check",
            "Mobile elements are displayed",
            "Mobile elements are not displayed",
            testStatus,
            element='screen'
        )

    def _mobileElementsNotDisplayedCheck(self):
        testStatus = not mainPage.mobileElementsDisplayed()
        self.reportStep(
            "Mobile elements not displayed check",
            "Mobile elements are not displayed",
            "Mobile elements are displayed",
            testStatus,
            element='screen'
        )
