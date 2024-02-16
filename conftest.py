import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.index_page import IndexPage
from pages.input_and_click_page import InputAndClickPage
from env_config import ConfigURL
from pages.drag_and_drop_page import DragAndDrop
import time

@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


# @pytest.fixture
# def setup(get_webdriver):
#     url = 'https://toghrulmirzayev.github.io/ui-simulator/index.html'
#     get_webdriver.get(url)
#     yield get_webdriver
#     get_webdriver.quit()


@pytest.fixture
def index_page(get_webdriver):
    get_webdriver.get(ConfigURL.BASE_URL)
    yield IndexPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture
def input_and_click_page(get_webdriver):
    get_webdriver.get(ConfigURL.INPUT_AND_CLICK)
    yield InputAndClickPage(get_webdriver)
    get_webdriver.quit()

@pytest.fixture
def drag_and_drop_page(get_webdriver):
    get_webdriver.get(ConfigURL.DRAG_AND_DROP)
    yield DragAndDrop(get_webdriver)
    time.sleep(5)
    get_webdriver.quit()