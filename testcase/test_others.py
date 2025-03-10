import time

import allure
import pytest
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

from pages.page_home import HomePage


@allure.epic("Others")
@allure.feature("other cases")
class TestOthers:
    # this module is just for note, not for test

    @allure.story("this is allure story")
    @allure.title("this is test title")
    @allure.testcase("http://www.baidu.com", "link for the case")
    @allure.issue("http://www.baidu.com", "link for the bug")
    @allure.description("this is description for the case")
    @allure.link("http://www.bilibili.com", "link")
    @allure.severity("blocker")
    def test_scroll_down_page(self, open_browser):
        HomePage(open_browser)
        time.sleep(5)
        open_browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)

    def test_scroll_to_element(self, open_browser):
        HomePage(open_browser)
        element = open_browser.find_element(By.XPATH, '//*[text()="电影放映厅"]')
        open_browser.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(5)

    @pytest.mark.skip(reason="hy: skip without condition")
    def test_refresh(self, open_browser):
        HomePage(open_browser)
        time.sleep(3)
        open_browser.refresh()
        time.sleep(3)

    @pytest.mark.skip(1>2, reason="skip with condition")
    def test_refresh_By_F5(self, open_browser):
        HomePage(open_browser)
        time.sleep(3)
        actions = ActionChains(open_browser)
        # actions.key_down(Keys.CONTROL).send_keys('r').key_up(Keys.CONTROL).perform()
        actions.send_keys(Keys.F5).perform()
        time.sleep(3)
