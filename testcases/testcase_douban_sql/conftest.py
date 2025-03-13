import pytest

from utils.read_files import read_ini

url = str(read_ini()['hosts']['douban_host_url']) + "/chart"

@pytest.fixture(scope="function")
def open_douban(driver):
    driver.get(url)
    yield driver