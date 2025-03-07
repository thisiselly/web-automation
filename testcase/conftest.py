import allure
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from base.base_page import BasePage
from project_config import ProjectConfig
from utils.logs_util import logger

agree_button = (By.CSS_SELECTOR, '.winE-policy-close-b')

def select_agree_button(driver):
    base_page = BasePage(driver)
    if not base_page.element_exist(agree_button, timeout=2):
        logger.info("the agree button does not shown, skip")
        return
    else:
        logger.info("the agree button is shown, click on it.")
        base_page.click(agree_button)

@pytest.fixture(scope="session")
def open_browser():
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(3)
    driver.get(ProjectConfig.home_url)
    select_agree_button(driver)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    out = yield
    report = out.get_result()

    if report.when == 'call' and report.failed:
        allure.attach(driver.get_screenshot_as_png(), "fail screenshot", allure.attachment_type.PNG)
