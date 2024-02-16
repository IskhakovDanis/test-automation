from pytest import mark
import allure
#from env_config import Secrets

def test_drag_and_drop_page(drag_and_drop_page):
    drag_and_drop_page.select_elem()

