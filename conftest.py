import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from utils.read_files import read_ini

browser_config = read_ini()["browser"]
browser_name = browser_config["name"].lower()
headless = browser_config.getboolean("headless")

@pytest.fixture(scope="session")
def driver():
    if browser_name == "chrome":
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.maximize_window()
    # driver.implicitly_wait(3)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    out = yield
    report = out.get_result()

    if report.when == 'call' and report.failed:
        driver = item.funcargs['driver']
        allure.attach(driver.get_screenshot_as_png(), "fail screenshot", allure.attachment_type.PNG)
