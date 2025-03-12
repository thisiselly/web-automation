import pytest
from selenium import webdriver

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.implicitly_wait(3)
    yield driver
    driver.quit()