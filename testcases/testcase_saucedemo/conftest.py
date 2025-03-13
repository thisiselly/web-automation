from selenium import webdriver
import pytest

from utils.read_files import read_ini

url = str(read_ini()['hosts']['saucedemo_host_url'])

@pytest.fixture(scope="function")
def open_saucedemo(driver):
    driver.get(url)
    yield driver