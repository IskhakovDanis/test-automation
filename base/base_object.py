from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from support.logger import log_func, log_func_for_error


class BaseObject:

    LOG = log_func()
    LOG_ERROR = log_func_for_error()
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def _is_visible(self, locator: tuple) -> WebElement:
        try:

            self.LOG.info(f"element {locator} is visible1")
            return self.wait.until(ec.visibility_of_element_located(locator))
            #self.LOG_ERROR.info(f"element {locator} is visible2")
        except:
            self.LOG.info(f"element {locator} is INvisible")

    def _is_clickable(self, locator: tuple) -> WebElement:
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click(self, locator: tuple) -> None:
        self._is_clickable(locator).click()

    def send_keys(self, locator: tuple, value: str):
        self._is_visible(locator).send_keys(value)

    def get_text(self, locator):
        return self._is_visible(locator).text

    def get_url(self):
        return self.driver.current_url


    #TODO
    def _is_invisible(self, locator: tuple):
        return self.wait.until(ec.invisibility_of_element_located(locator))

    def check_invisible_obj(self, locator: tuple):
        return self._is_invisible(locator)

