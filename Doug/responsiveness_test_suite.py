from os import path

from excel.excelreader import excelReader
from responsiveness_register_test_case import RegisterResponsivenessTestCase
from responsiveness_retrieve_test_case import RetrieveInfoResponsivenessTestCase
from runittest.reporting_unittest import ReportingTestCase
from runittest.reporting_unittest import ReportingTestResult
from runittest.reporting_unittest import ReportingTestSuite
from runittest.reporting_unittest import SingletonWebDriver

# Set up a web driver object
driver = SingletonWebDriver()

# Set up a test suite object
reportPath = path.join(
    "C:\\",
    "Users",
    "matrixrunner",
    "Desktop",
    "Selenium Sprints",
    "9-27",
    "AO-Responsiveness-Testing",
    "Doug"
)

AO_Suite = ReportingTestSuite(
    "Advantage Online - Responsiveness Testing",
    "Doug Walter",
    driver,
    outPath=reportPath
)

# Get the test data from the spreadsheet
dataPath = path.join(
    reportPath,
    "AdvantageData.xlsm"
)

# Add the test cases from the test data
testList = []
for dataRow in excelReader(
    dataPath,
    0,
    varModFunc=lambda a: a[3:]
):
    testList.append(
        RegisterResponsivenessTestCase(**dataRow)
    )
    dataRow['testCaseID'] = "DW_TC002"
    dataRow['testCaseDescription'] = "Logged-in user can retrieve their profile information"
    testList.append(
        RetrieveInfoResponsivenessTestCase(**dataRow)
    )

AO_Suite.addTests(testList)

# Get a results object ready
results = ReportingTestResult()

# Run the test suite
AO_Suite.run(results)

# Stop driving
driver.quit()
