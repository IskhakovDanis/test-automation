from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from support.logger import log_func
from selenium.common import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select


class BaseObject:

    LOG = log_func()

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.actions = ActionChains(driver)
        self.mouse = ActionChains(driver)

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
            element = self.wait.until(ec.element_to_be_clickable(locator))
            self.LOG.info(f"element {locator} is clickable")
            return element
        except TimeoutException:
            self.LOG.info(f"element {locator} is INclickable")
            raise TimeoutException(f"element {locator} is not clicable during specified time")

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

    def simulate_enter_click(self, locator: tuple):
        self.send_keys(locator, Keys.RETURN)

    def get_attribute_of_elements(self, locator: tuple):
        image_element = self._is_visible(locator)
        actual_text = image_element.get_attribute("src")
        return actual_text

    def scroll_to_element(self, locator: tuple):
        element = self._is_visible(locator)
        self.actions.move_to_element(element).perform()

    def hover_mouse(self, locator: tuple):
        elem = self._is_visible(locator)
        self.mouse.move_to_element(elem).perform()

    def drop_down(self, locator: tuple):
        dropdown = self._is_visible(locator)
        select = Select(dropdown)
        select.select_by_visible_text("I")

    def drag_and_drop(self, locator1: tuple, locator2: tuple):
        to_drag_elem = self._is_visible(locator1)  # находим элемент который будем тянуть
        to_drop_elem = self._is_visible(locator2)  # находим элемент куда будем тянуть первый элемент
        self.actions.drag_and_drop(to_drag_elem, to_drop_elem).perform()




