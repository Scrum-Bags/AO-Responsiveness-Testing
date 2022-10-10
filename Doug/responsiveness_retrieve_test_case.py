from itertools import chain
from time import sleep

from selenium.webdriver.common.action_chains import ActionChains

from runittest.reporting_unittest import ReportingTestCase
from page_elements.advantage_online_elements import *
from advantage_pages import *
from printlogger.printlogger import displayPrint


class RetrieveInfoResponsivenessTestCase(ReportingTestCase):

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
        self._setWindowMaxDimensions()
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
        displayPrint("Account page loaded")
        self.reportEvent(
            "Account page loaded",
            element="screen"
        )

        # go to info edit page
        displayPrint("Going to profile edit page")
        summaryPage.goToProfileEditPage()

        # get edit page object
        editPage = UserInfoEditPage()
        displayPrint("Profile edit page loaded")
        self.reportEvent(
            "Profile edit page loaded",
            element="screen"
        )

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
            data=[
                'firstName',
                'lastName',
                'phoneNumber',
                'addressCountry',
                'addressCity',
                'addressStreet',
                'addressPostalCode',
                'addressRegion'
            ]
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

        # check that all fields are vertically parallel
        xPositions = {
            f: editPage.elements[f].location['x']
            for f in 
            [
                'email',
                'first_name',
                'last_name',
                'phone_number',
                'address_country',
                'address_city',
                'address_street',
                'address_postal_code',
                'address_region'
            ]
        }
        testStatus = len(xPosition.values()) == 1
        displayPrint("Mobile format vertical field alignment check")
        self.reportStep(
            "Mobile format vertical field alignment check",
            "Input fields are vertically aligned",
            "Input fields are not vertically aligned",
            testStatus,
            element='screen',
            data='<br>'.join(
                [
                    f"{a}: {ax}" 
                    for a, ax 
                    in xPositions.items()
                ]
            )
        )

        # Check that mobile elements are displayed
        self._mobileElementsDisplayedCheck()

        # Set window size to maximum
        self._setWindowMaxDimensions()

        # Get page object
        editPage = UserInfoEditPage()

        # Test for field parallels
        parallelPairKeys = [
            ('first_name', 'last_name'),
            ('address_country', 'address_city'),
            ('address_street', 'address_postal_code')
        ]
        for pair in parallelPairKeys:
            a, b = pair
            ay, by = editPage.elements[a].location['y'], editPage.elements[b].location['y']
            testStatus = ay == by
            displayPrint(f"Checking vertical positions of {a} and {b}")
            self.reportStep(
                f"Testing horizontal positions of {a} and {b}",
                f"{a} is parallel to {b}",
                f"{a} is not parallel to {b}",
                testStatus,
                element="screen",
                data=f"{a}'s y: {ay}<br>{b}'s y: {by}"
            )

        # Check that mobile elements are not displayed
        self._mobileElementsNotDisplayedCheck()

    def _setWindowMobileDimensions(self):
        self.driverObj.set_window_size(**self._accountPageMobileDims)
        displayPrint("Window sized to mobile dimensions")
        self.reportEvent(
            "Window sized to mobile dimensions",
            element='screen',
            data='<br>'.join([f"{k}: {v}" for k, v in self._accountPageMobileDims.items()])
        )

    def _setWindowMaxDimensions(self):
        self.driverObj.maximize_window()
        displayPrint("Window sized to max dimensions")
        self.reportEvent(
            "Window sized to max dimensions",
            element='screen'
        )

    def _mobileElementsDisplayedCheck(self):
        page = AdvantagePage(loggedIn=False)
        testStatus = page.mobileElementsDisplayed()
        displayPrint("Mobile elements displayed check")
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
        displayPrint("Mobile elements not displayed check")
        self.reportStep(
            "Mobile elements not displayed check",
            "Mobile elements are not displayed",
            "Mobile elements are displayed",
            testStatus,
            element='screen'
        )
