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
            self.LOG.error(f"element {locator} is INclickable")
            raise TimeoutException(f"element {locator} is not clicable during specified time")

    def click(self, locator: tuple) -> None:
        try:
            self._is_clickable(locator).click()
            self.LOG.info(f"element {locator} is click")
        except TimeoutException:
            self.LOG.error(f"element {locator} is unavailable for click")
            raise TimeoutException(f"element {locator} is not clicable during specified time")

    def send_keys(self, locator: tuple, value: str):
        try:
            self._is_visible(locator).send_keys(value)
            self.LOG.info(f"element {locator} is sended data")
        except TimeoutException:
            self.LOG.error(f"element {locator} is NOT sended data ")
            raise TimeoutException(f"element {locator} is not clicable during specified time")


    def get_text(self, locator):
        try:
            x = self._is_visible(locator).text
            self.LOG.info(f"element {locator} is sended data")
            return x
        except TimeoutException:
            self.LOG.error(f"element {locator} is NOT sended data ")
            raise TimeoutException(f"element {locator} is not clicable during specified time")


    def get_url(self):
        try:
            x = self.driver.current_url
            self.LOG.info(f"element gived url")
            return x
        except TimeoutException:
            self.LOG.error(f"element is NOT gived data ")
            raise TimeoutException(f"element  is not clicable during specified time")


    def _is_invisible(self, locator: tuple):

        try:
            x = self.wait.until(ec.invisibility_of_element_located(locator))
            self.LOG.info(f"element is Invisible")
            return x
        except TimeoutException:
            self.LOG.error(f"element is NOT Invisible ")
            raise TimeoutException(f"element  is not clicable during specified time")


    def check_invisible_obj(self, locator: tuple):
        try:
            x = self._is_invisible(locator)
            self.LOG.info(f"element is Invisible")
            return x
        except TimeoutException:
            self.LOG.error(f"element is NOT Invisible ")
            raise TimeoutException(f"element  is not clicable during specified time")


    def simulate_enter_click(self, locator: tuple):
        try:
            self.send_keys(locator, Keys.RETURN)
            self.LOG.info(f"element {locator} is enter_click")
        except TimeoutException:
            self.LOG.error(f"element {locator} is unavailable for enter_click")
            raise TimeoutException(f"element {locator} is not clicable during specified time")


    def get_attribute_of_elements(self, locator: tuple):
        try:
            attribute_elem = self._is_visible(locator).get_attribute("src")
            self.LOG.info(f"element {locator} is getted atrribute")
            return attribute_elem
        except TimeoutException:
            self.LOG.error(f"element {locator} is NOT getted attribute_elem  ")
            raise TimeoutException(f"element {locator} is not clicable during specified time")
        # image_element = self._is_visible(locator)
        # actual_text = image_element.get_attribute("src")
        # return actual_text

    def scroll_to_element(self, locator: tuple):
        try:
            element = self._is_visible(locator)
            self.actions.move_to_element(element).perform()
            self.LOG.info(f"element {locator} is scroll_to_element")
        except TimeoutException:
            self.LOG.error(f"element {locator} is NOT scroll_to_element")
            raise TimeoutException(f"element {locator} is not clicable during specified time")

        element = self._is_visible(locator)
        self.actions.move_to_element(element).perform()

    def hover_mouse(self, locator: tuple):
        try:
            elem = self._is_visible(locator)
            self.mouse.move_to_element(elem).perform()
            self.LOG.info(f"element {locator} is hover_mouse")
        except TimeoutException:
            self.LOG.error(f"element {locator} is NOT hover_mouse")
            raise TimeoutException(f"element {locator} is not clicable during specified time")

    def drop_down(self, locator: tuple):
        try:
            dropdown = self._is_visible(locator)
            select = Select(dropdown)
            select.select_by_visible_text("I")
            self.LOG.info(f"element {locator} is scroll_to_element")
        except TimeoutException:
            self.LOG.error(f"element {locator} is NOT scroll_to_element")
            raise TimeoutException(f"element {locator} is not clicable during specified time")


    def drag_and_drop(self, locator1: tuple, locator2: tuple):
        try:
            to_drag_elem = self._is_visible(locator1)  # находим элемент который будем тянуть
            to_drop_elem = self._is_visible(locator2)  # находим элемент куда будем тянуть первый элемент
            self.actions.drag_and_drop(to_drag_elem, to_drop_elem).perform()
            self.LOG.info(f"element {locator1} and {locator2} drag and droped")
        except TimeoutException:
            self.LOG.error(f"element {locator1} or {locator2} NOT drag and droped ")
            raise TimeoutException(f"element {locator1} or {locator2} is not clicable during specified time")




