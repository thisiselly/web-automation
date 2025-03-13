import pytest
from selenium import webdriver

from utils.read_files import read_ini

browser_name = read_ini()["browser"]["name"].lower()

@pytest.fixture(scope="session")
def driver():
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    # driver.implicitly_wait(3)
    yield driver
    driver.quit()