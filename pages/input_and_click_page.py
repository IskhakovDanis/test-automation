from base.base_object import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from support.assertions import Assertions
from pytest import mark


class InputAndClickPage(BaseObject, Assertions):

    PLACE_HOLDER = (By.ID, "inputText")
    ADD_BUTTON = (By.ID, "addBtn")
    DELETE_BUTTON = (By.ID, "deleteBtn")
    BACK_BUTTON = (By.CSS_SELECTOR, ".back-button")
    ITEMS = (By.CSS_SELECTOR, "#items > div:nth-child(1)")


    def __init__(self, driver : WebDriver):
        super().__init__(driver)

    def input_text(self):
        self.send_keys(self.PLACE_HOLDER, "Hello world")

    def click_add_btn(self):
        self.click(self.ADD_BUTTON)

    def click_dlt_btn(self):
        self.click(self.DELETE_BUTTON)

    def click_back_btn(self):
        self.click(self.BACK_BUTTON)

    def check_items(self):
        self.assert_equal(self.get_text(self.ITEMS), "Hello world")

    def check_items_after_dlt(self):
        self.check_invisible_obj(self.ITEMS)