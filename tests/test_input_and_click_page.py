

from pytest import mark


#@mark.homework
def test_input_and_click(input_and_click_page):
    input_and_click_page.input_text()
    input_and_click_page.click_add_btn()
    input_and_click_page.check_items()
    input_and_click_page.click_dlt_btn()


@mark.homework
def test_1():
    pass
