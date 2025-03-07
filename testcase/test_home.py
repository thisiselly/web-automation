import time

import allure
import pytest
from pages.page_home import HomePage
from project_config import ProjectConfig
from utils.assert_util import verification

@allure.epic("HomePage")
@allure.feature("home page cases")
class TestHomePage:

    @pytest.mark.homeselect
    def test_select_vip_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("select vip button"):
            home_page.select_vip_button()

        with allure.step("verify login page is shown"):
            home_page.verify_login_page_show()
            time.sleep(1)

        with allure.step("close the login page"):
            home_page.close_login_window()
            time.sleep(2)

    @pytest.mark.homeselect
    def test_select_view_history_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("select view history button"):
            home_page.select_view_history_button()

        with allure.step("verify history page loaded success"):
            home_page.switch_to_history_window()
            actual_url = open_browser.current_url
            verification.assertion(expect_result=ProjectConfig.history_url, compare_method="==", actual_result=actual_url)
            home_page.close()
            home_page.switch_to_home_window()

    @pytest.mark.homeselect
    def test_select_creator_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("select creator button"):
            home_page.select_creator_button()

        with allure.step("verify it stays on the home page"):
            actual_url = open_browser.current_url
            verification.assertion(expect_result=ProjectConfig.home_url, compare_method="==", actual_result=actual_url)

    @pytest.mark.homeselect
    def test_select_scan_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("select scan button"):
            home_page.select_scan_button_button()

        with allure.step("verify it stays on the home page"):
            actual_url = open_browser.current_url
            verification.assertion(expect_result=ProjectConfig.home_url, compare_method="==", actual_result=actual_url)

    @pytest.mark.homeselect
    def test_select_profile_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("select profile button"):
            home_page.select_profile_button()

        with allure.step("verify profile page loaded success"):
            home_page.switch_to_profile_window()
            actual_url = open_browser.current_url
            verification.assertion(expect_result=ProjectConfig.vip_url, compare_method="==",
                                   actual_result=actual_url)
            home_page.close()
            home_page.switch_to_home_window()

    @pytest.mark.homemove
    def test_move_to_vip_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to vip button"):
            home_page.move_to_vip_button()

        with allure.step("verify page shows correct"):
            actual_result = home_page.element_exist(home_page.win_vip)
            verification.assertion(True,"==", actual_result)
            actual_text = home_page.get_text(home_page.win_vip)
            expect_text = "开通VIP后\n可享受以下内容"
            verification.assertion(expect_text, "==", actual_text)

    @pytest.mark.homemove
    def test_move_to_history_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to view history button"):
            home_page.move_to_view_history_button()

        with allure.step("verify page shows correct"):
            actual_result = home_page.element_exist(home_page.win_history)
            verification.assertion(True,"==", actual_result)
            actual_text = home_page.get_text(home_page.win_history_head)
            expect_text = "观看历史"
            verification.assertion(expect_text, "==", actual_text)

    @pytest.mark.homemove
    def test_move_to_creator_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to creator button"):
            home_page.move_to_creator_button()

        with allure.step("verify page shows correct"):
            actual_result = home_page.element_exist(home_page.win_creator)
            verification.assertion(True,"==", actual_result)
            actual_text = home_page.get_text(home_page.win_creator)
            expect_text = "创作者平台\n创作者入驻"
            verification.assertion(expect_text, "==", actual_text)

    @pytest.mark.homemove
    def test_move_to_scan_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to scan button"):
            home_page.move_to_scan_button()

        with allure.step("verify page shows correct"):
            actual_result = home_page.element_exist(home_page.win_scan)
            verification.assertion(True,"==", actual_result)
            actual_text = home_page.get_text(home_page.win_scan_text)
            expect_text = "使用手机扫描二维码下载央视频客户端"
            icon_displayed = home_page.element_exist(home_page.win_scan_icon)
            verification.assertion(expect_text, "==", actual_text)
            verification.assertion(True, "==", icon_displayed)

    @pytest.mark.homemove
    def test_move_to_profile_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to profile button"):
            home_page.move_to_profile_button()

        with allure.step("verify page shows correct"):
            actual_result = home_page.element_exist(home_page.win_profile)
            verification.assertion(True,"==", actual_result)
            actual_text = home_page.get_text(home_page.win_profile)
            expect_text = "登录后\n可享受以下内容"
            verification.assertion(expect_text, "==", actual_text)

    @pytest.mark.homeclick
    def test_vip_click_login(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to vip button"):
            home_page.move_to_vip_button()

        with allure.step("click the login button"):
            home_page.click(home_page.login_button_vip)

        with allure.step("Verify login page shown"):
            home_page.verify_login_page_show()

    @pytest.mark.homeclick
    def test_history_click_login(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("move the mouse to the view history button"):
            home_page.move_to_view_history_button()

        with allure.step("click the login button"):
            home_page.click(home_page.login_button_history)

        with allure.step("Verify login page shown"):
            home_page.verify_login_page_show()

    @pytest.mark.homeclick
    def test_profile_click_login(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to profile button"):
            home_page.move_to_profile_button()

        with allure.step("click the login button"):
            home_page.click(home_page.login_button_profile)

        with allure.step("verify login page shown"):
            home_page.verify_login_page_show()


