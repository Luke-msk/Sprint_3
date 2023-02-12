import pytest
from selenium import webdriver
url = 'https://stellarburgers.nomoreparties.site/'
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(url)
    yield driver
    driver.quit()