import pytest
from selenium import webdriver



@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome('C:/Test_driver/chromedriver.exe')
    driver.implicitly_wait(10)

    yield driver
    driver.quit()