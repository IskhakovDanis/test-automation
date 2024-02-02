from base.base_object import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from support.assertions import Assertions
from support.data_for_tests import Data
import allure



class  IndexPage(BaseObject, Assertions, Data):

    USERNAME_FIELD = (By.ID, "usernam")
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

    @allure.step("checking url")
    def check_url(self):
        self.assert_equal(self.get_url(),
                          self.get_info("hover_and_select_url"))

    @allure.step("checking error message")
    def check_error_msg(self, error_msg):
        self.assert_equal(actual=self.get_text(self.ERROR_MSG),
                          expected=error_msg)


