import pytest

@pytest.fixture(scope="function")
def open_douban(driver):
    driver.get("https://music.douban.com/chart")
    yield driver