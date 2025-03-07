import time
import pytest
from pages.page_home import HomePage
from project_config import ProjectConfig
from utils.assert_util import verification


class TestHomePage:

    @pytest.mark.p0
    def test_select_vip_button(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.select_vip_button()
        home_page.verify_login_page_show()
        time.sleep(3)
        home_page.close_login_window()
        time.sleep(2)

    @pytest.mark.p0
    def test_select_view_history_button(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.select_view_history_button()
        home_page.switch_to_history_window()
        actual_url = open_browser.current_url
        verification.assertion(expect_result=ProjectConfig.history_url, compare_method="==", actual_result=actual_url)
        home_page.close()
        home_page.switch_to_home_window()

    def test_select_creator_button(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.select_creator_button()
        actual_url = open_browser.current_url
        verification.assertion(expect_result=ProjectConfig.home_url, compare_method="==", actual_result=actual_url)

    def test_select_scan_button(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.select_scan_button_button()
        actual_url = open_browser.current_url
        verification.assertion(expect_result=ProjectConfig.home_url, compare_method="==", actual_result=actual_url)

    def test_select_profile_button(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.select_profile_button()
        home_page.switch_to_profile_window()
        actual_url = open_browser.current_url
        verification.assertion(expect_result=ProjectConfig.vip_url, compare_method="==",
                                   actual_result=actual_url)
        home_page.close()
        home_page.switch_to_home_window()

    def test_move_to_vip_button(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.move_to_vip_button()
        actual_result = home_page.element_exist(home_page.win_vip)
        verification.assertion(True,"==", actual_result)
        actual_text = home_page.get_text(home_page.win_vip)
        expect_text = r"开通VIP后\n可享受以下内容"
        verification.assertion(expect_text, "==", actual_text)

    def test_move_to_history_button(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.move_to_view_history_button()
        actual_result = home_page.element_exist(home_page.win_history)
        verification.assertion(True,"==", actual_result)
        actual_text = home_page.get_text(home_page.win_history_head)
        expect_text = "观看历史"
        verification.assertion(expect_text, "==", actual_text)

    def test_move_to_creator_button(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.move_to_creator_button()
        actual_result = home_page.element_exist(home_page.win_creator)
        verification.assertion(True,"==", actual_result)
        actual_text = home_page.get_text(home_page.win_creator)
        print(actual_text)
        expect_text = r"创作者平台\n创作者入驻"
        verification.assertion(expect_text, "==", actual_text)

    def test_move_to_scan_button(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.move_to_scan_button()
        actual_result = home_page.element_exist(home_page.win_scan)
        verification.assertion(True,"==", actual_result)
        actual_text = home_page.get_text(home_page.win_scan_text)
        expect_text = "使用手机扫描二维码下载央视频客户端"
        icon_displayed = home_page.element_exist(home_page.win_scan_icon)
        verification.assertion(expect_text, "==", actual_text)
        verification.assertion(True, "==", icon_displayed)

    def test_move_to_profile_button(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.move_to_profile_button()
        actual_result = home_page.element_exist(home_page.win_profile)
        verification.assertion(True,"==", actual_result)
        actual_text = home_page.get_text(home_page.win_profile)
        expect_text = r"登录后\n可享受以下内容"
        verification.assertion(expect_text, "==", actual_text)

    def test_vip_click_login(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.move_to_vip_button()
        home_page.click(home_page.login_button_vip)
        home_page.verify_login_page_show()

    def test_history_click_login(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.move_to_view_history_button()
        home_page.click(home_page.login_button_history)
        home_page.verify_login_page_show()

    def test_profile_click_login(self, open_browser):
        home_page = HomePage(open_browser)
        home_page.move_to_profile_button()
        home_page.click(home_page.login_button_profile)
        home_page.verify_login_page_show()


