import pytest

@pytest.fixture(scope="function")
def open_sahi(driver):
    driver.get("https://sahitest.com/demo/")
    yield driver

