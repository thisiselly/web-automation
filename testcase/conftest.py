import pytest
from pages.page_home import HomePage
from project_config import ProjectConfig
from utils.logs_util import logger

def select_agree_button(driver):
    home_page = HomePage(driver)
    if not home_page.element_exist(home_page.agree_button, timeout=2):
        logger.info("the agree button does not shown, skip")
        return
    else:
        logger.info("the agree button does is shown, click on it.")
        home_page.click(home_page.agree_button)

@pytest.fixture(scope="session")
def open_browser(driver):
    driver.get(ProjectConfig.home_url)
    select_agree_button(driver)
    yield driver
    driver.quit()