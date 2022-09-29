from time import sleep

from runittest.reporting_unittest import ReportingTestCase

from page_elements.advantage_online_elements import commonElementIDs
from page_elements.advantage_online_elements import mainPageWideElementIDs
from page_elements.advantage_online_elements import mainPageWaitIDs
from page_elements.advantage_online_elements import userRegisterElementIDs
from advantage_pages import AccountSummaryPage
from advantage_pages import AdvantagePage
from advantage_pages import MainPage
from advantage_pages import RegisterPage


class ResponsivenessTestCase(ReportingTestCase):

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
        # # Fill out new user info

        # # Go to account summary page
        # mainPage = MainPage(loggedIn=True)
        # mainPage.goToUserProfile()
        # self._testAccountPageResponsiveLayout()

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
            self.reportStep(
                "Relative field position check", 
                f"{orderedFields[a]} field is higher than {orderedFields[b]} field", 
                f"{orderedFields[a]} field is not higher than {orderedFields[b]} field", 
                testStatus
            )

        # Check that mobile elements are displayed
        self._mobileElementsDisplayedCheck()

        # Set window size to maximum
        self._setWindowMaxDimensions()

        # Get page object
        registerPage = RegisterPage()

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
        self.driverObj.set_window_size(**self._mainPageMobileDims)
        self.reportEvent(
            "Window sized to mobile dimensions",
            element='screen',
            data='\n'.join([f"{k}: {v}" for k, v in self._mainPageMobileDims.items()])
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
