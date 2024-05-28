from pytest import mark
import allure
from env_config import TOKEN_1, TOKEN_2

@allure.description('Success login')
@allure.label('owner', 'Danis')
@allure.title('Successful login')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.BLOCKER)
def test_successful_login(index_page):
    index_page.input_username(username=TOKEN_1)
    index_page.input_password(password=TOKEN_2)
    index_page.click_enter()
    index_page.click_to_login_btn()
    index_page.check_url()


case_1 = ["correct_username", "incorrect_password", "Password or username is incorrect"]
case_2 = ['', "incorrect_password", "Username field cannot be empty"]
case_3 = ['incorrect_password', "", "Password field cannot be empty"]



@allure.description('UNSuccess login')
@allure.label('owner', 'Danis')
@allure.title('UNSuccessful login')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.BLOCKER)
@mark.parametrize('username, password, error_msg', (case_1, case_2, case_3))

def test_unsuccessful_login(index_page, username, password, error_msg):
    index_page.input_username(username=username)
    index_page.input_password(password=password)
    index_page.click_to_login_btn()
    index_page.check_error_msg(error_msg=error_msg)


