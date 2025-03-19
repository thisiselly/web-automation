from selenium import webdriver
import pytest

from utils.get_file_data import get_settings

url = str(get_settings()['hosts']['saucedemo_host_url'])


@pytest.fixture(scope="function")
def open_saucedemo(driver):
    driver.get(url)
    yield driver
