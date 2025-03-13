import pytest

from utils.read_files import read_ini

url = str(read_ini()['hosts']['sahi_host_url'])

@pytest.fixture(scope="function")
def open_sahi(driver):
    driver.get(url)
    yield driver

