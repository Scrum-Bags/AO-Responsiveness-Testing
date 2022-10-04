from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from runittest.reporting_unittest import SingletonWebDriver

_DEFAULT_TIMEOUT = 12


def waitForSpecificElement(
    idDict: dict,
    timeout: int = _DEFAULT_TIMEOUT
):
    waitElement = idDict.values()
    WebDriverWait(
        SingletonWebDriver(),
        timeout
    ).until(
        EC.presence_of_element_located(
            waitElement
        )
    )
