import pytest

from utils.get_file_data import get_settings

url = str(get_settings()['hosts']['douban_host_url']) + "/chart"


@pytest.fixture(scope="function")
def open_douban(driver):
    driver.get(url)
    yield driver
