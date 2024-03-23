from base.base_object import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from support.assertions import Assertions
import allure



class  DragAndDrop(BaseObject, Assertions):

    TO_DRAG_ELEM = (By.ID, "item-1")
    TO_DROP_ELEM = (By.ID, "item-2")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("element selected")
    def select_elem(self):
        self.drag_and_drop(self.TO_DRAG_ELEM, self.TO_DROP_ELEM)

    def check_moving(self):
        pass

