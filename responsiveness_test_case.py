from time import sleep

from runittest.reporting_unittest import ReportingTestCase

from advantage_pages import AdvantagePage
from advantage_pages import MainPage
from advantage_pages import RegisterPage
from advantage_pages import AccountSummaryPage

class ResponsivenessTestCase(ReportingTestCase):

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
    
    def registerUser(self):
        pass
            
    def tearDown(self):
        pass
    
    def runTest(self):
        pass
