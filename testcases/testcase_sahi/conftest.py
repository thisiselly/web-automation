import pytest

from utils.get_file_data import get_settings

url = str(get_settings()['hosts']['sahi_host_url'])


@pytest.fixture(scope="function")
def open_sahi(driver):
    driver.get(url)
    yield driver
