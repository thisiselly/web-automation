import allure
import pytest

@allure.epic("Others")
@allure.feature("other cases")
class TestOthers:
    @allure.story("this is allure story")
    @allure.title("this is test title")
    @allure.testcase("http://www.baidu.com", "link for the case")
    @allure.issue("http://www.baidu.com", "link for the bug")
    @allure.description("this is description for the case")
    @allure.link("http://www.bilibili.com", "link")
    @allure.severity("blocker")
    def test_scroll_down_page(self, open_browser):
        pass

    def test_scroll_to_element(self, open_browser):
        pass


    @pytest.mark.skip(reason="hy: skip without condition")
    def test_refresh(self, open_browser):
        pass

    @pytest.mark.skip(1>2, reason="skip with condition")
    def test_refresh2(self, open_browser):
        pass