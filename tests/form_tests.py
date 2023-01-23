from page.form_page import FormPage
import pytest as pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(r'C:/Users/User/PycharmProjects/ui tests sunny/chromedriver.exe')
    driver.maximize_window()
    yield driver
    driver.quit()


class TestFormPage:

    def test_form(self, driver):
        form_page = FormPage(driver, 'http://65.109.58.238/help/volunteering')
        form_page.open()
        userName, userSurname, email = form_page.fill_fields_and_submit()
        result = form_page.form_result()
        assert f'{userName} {userSurname}' == result[0], 'the form has not been filled'
        assert email == result[1], 'the form has not been filled'
