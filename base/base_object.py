from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from support.logger import log_func
from selenium.common import TimeoutException

class BaseObject:

    LOG = log_func()

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def _is_visible(self, locator: tuple) -> WebElement:
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            self.LOG.info(f"element {locator} is visible")
            return element
        except TimeoutException:
            self.LOG.error(f"element {locator} is INvisible")
            raise TimeoutException(f"element {locator} is not visible during specified time")

    def _is_clickable(self, locator: tuple) -> WebElement:
        try:
            x = self.wait.until(ec.element_to_be_clickable(locator))
            self.LOG.info(f"element {locator} is clickable")
            return x
        except:
            self.LOG.info(f"element {locator} is INclickable")

    def click(self, locator: tuple) -> None:
        self._is_clickable(locator).click()

    def send_keys(self, locator: tuple, value: str):
        self._is_visible(locator).send_keys(value)

    def get_text(self, locator):
        return self._is_visible(locator).text

    def get_url(self):
        return self.driver.current_url

    def _is_invisible(self, locator: tuple):
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def check_invisible_obj(self, locator: tuple):
        return self._is_invisible(locator)

