import allure
import pytest
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils.logs_util import logger
from utils.read_files import read_ini

agree_button = (By.CSS_SELECTOR, '.winE-policy-close-b')
url = read_ini()['hosts']['host_url']

@pytest.fixture(scope="function")
def open_browser(driver):
    driver.get(url)
    select_agree_button(driver)
    yield driver
    back_to_home_page(driver)

def select_agree_button(driver):
    """
    select the agree button if shows when launch home page
    :param driver:
    :return:
    """
    base_page = BasePage(driver)
    if not base_page.element_exist(agree_button, 1, timeout=2):
        logger.info("the agree button does not shown, skip")
        return
    else:
        logger.info("the agree button is shown, click on it.")
        base_page.click(agree_button)

def back_to_home_page(driver):
    """
    back to the home page and close extra windows after one case finished
    :param driver:
    :return:
    """
    base_page = BasePage(driver)
    base_page.switch_to_window(to_home_window=True)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    out = yield
    report = out.get_result()

    if report.when == 'call' and report.failed:
        driver = item.funcargs['driver']  # 从 item.funcargs 获取 driver
        allure.attach(driver.get_screenshot_as_png(), "fail screenshot", allure.attachment_type.PNG)
