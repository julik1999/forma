
import pytest as pytest
from selenium import webdriver


@pytest.fixture()
def driver():
    driver = webdriver.Chrome(r'C:\Users\User\PycharmProjects\forma\tests\chromedriver.exe')
    driver.maximize_window()
    timeout = 5
    yield driver
    driver.quit()
