from base.base_object import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from support.assertions import Assertions
import allure



class  IndexPage(BaseObject, Assertions):

    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.CLASS_NAME, "login-button")
    ERROR_MSG = (By.CLASS_NAME, 'error-message')


    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Username added")
    def input_username(self, username):
        self.send_keys(locator=self.USERNAME_FIELD, value=username)

    @allure.step("Password added")
    def input_password(self, password):
        self.send_keys(locator=self.PASSWORD_FIELD, value=password)

    @allure.step("click login button")
    def click_to_login_btn(self):
        self.click(self.LOGIN_BTN)

    @allure.step("click Enter")
    def click_enter(self):
        self.simulate_enter_click(self.LOGIN_BTN)

    @allure.step("checking url")
    def check_url(self):
        self.assert_equal(actual=self.get_url(),
                          expected="https://toghrulmirzayev.github.io/ui-simulator/")

    @allure.step("checking error message")
    def check_error_msg(self, error_msg):
        self.assert_equal(actual=self.get_text(self.ERROR_MSG),
                          expected=error_msg)


