from selenium import webdriver
import pytest

@pytest.fixture(scope="function")
def open_saucedemo(driver):
    driver.get("https://www.saucedemo.com/")
    yield driver