import allure
import pytest
from pages.page_yangshipin.page_home import HomePage
from utils.assert_util import *
from utils.read_files import read_ini


@allure.epic("HomePage")
@allure.feature("home page cases")
class TestHomePage:
    url = read_ini()['hosts']['yangshipin_host_url']

    @pytest.mark.home
    def test_select_vip_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("select vip button"):
            home_page.select_vip_button()

        with allure.step("verify login page is shown"):
            home_page.verify_login_page_shown()

    @pytest.mark.home
    def test_select_view_history_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("select view history button"):
            home_page.select_view_history_button()

        with allure.step("verify history page loaded success in new page"):
            home_page.switch_to_current_window()
            actual_url = open_browser.current_url
            assert_equal(self.url + "/user/history", actual_url, "the history page is not loaded as expect")

    @pytest.mark.home
    def test_select_creator_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("select creator button"):
            home_page.select_creator_button()

        with allure.step("verify it stays on the home page"):
            actual_url = open_browser.current_url
            assert_equal(self.url + "/", actual_url, "page does not stay on home page after click creator button")

    @pytest.mark.home
    def test_select_scan_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("select scan button"):
            home_page.select_scan_button_button()

        with allure.step("verify it stays on the home page"):
            actual_url = open_browser.current_url
            assert_equal(self.url + "/", actual_url, "page does not stay on home page after click scan button")

    @pytest.mark.home
    def test_select_profile_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("select profile button"):
            home_page.select_profile_button()

        with allure.step("verify profile page loaded success"):
            home_page.switch_to_current_window()
            actual_url = open_browser.current_url
            assert_equal(self.url + "/user/vip", actual_url, "the vip page is not loaded as expect")

    @pytest.mark.home
    def test_move_to_vip_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to vip button"):
            home_page.move_to_vip_button()

        with allure.step("verify page shows correct"):
            win_vip_shown = home_page.element_exist(home_page.win_vip)
            actual_text = home_page.get_text(home_page.win_vip)
            expect_text = "开通VIP后\n可享受以下内容"
            assert_true(win_vip_shown, "the vip button does not shown as expect.")
            assert_equal(expect_text, actual_text, "the text shows not correct")

    @pytest.mark.home
    def test_move_to_history_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to view history button"):
            home_page.move_to_view_history_button()

        with allure.step("verify page shows correct"):
            win_history_shown = home_page.element_exist(home_page.win_history)
            actual_text = home_page.get_text(home_page.win_history_head)
            expect_text = "观看历史"
            assert_true(win_history_shown, "the history windows does not displayed as expect")
            assert_equal(expect_text, actual_text, "the text does not shown correct as expect.")

    @pytest.mark.home
    def test_move_to_creator_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to creator button"):
            home_page.move_to_creator_button()

        with allure.step("verify page shows correct"):
            win_creator_shown = home_page.element_exist(home_page.win_creator)
            actual_text = home_page.get_text(home_page.win_creator)
            expect_text = "创作者平台\n创作者入驻"
            assert_true(win_creator_shown, "the win creator window does not shown as expect.")
            assert_equal(expect_text, actual_text, "the text does not shown correct as expect.")

    @pytest.mark.home
    def test_move_to_scan_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to scan button"):
            home_page.move_to_scan_button()

        with allure.step("verify page shows correct"):
            win_scan_shown = home_page.element_exist(home_page.win_scan)
            icon_displayed = home_page.element_exist(home_page.win_scan_icon)
            actual_text = home_page.get_text(home_page.win_scan_text)
            expect_text = "使用手机扫描二维码下载央视频客户端"
            assert_true(win_scan_shown, "the win scan window does not shown as expect.")
            assert_true(icon_displayed, "the icon does not shown as expect.")
            assert_equal(expect_text, actual_text, "the text does not shown correctly as expect.")

    @pytest.mark.home
    def test_move_to_profile_button(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to profile button"):
            home_page.move_to_profile_button()

        with allure.step("verify page shows correct"):
            win_profile_shown = home_page.element_exist(home_page.win_profile)
            actual_text = home_page.get_text(home_page.win_profile)
            expect_text = "登录后\n可享受以下内容"
            assert_true(win_profile_shown, "the win profile window does not shown as expect.")
            assert_equal(expect_text, actual_text, "the text does not shown as expect.")

    @pytest.mark.home
    def test_vip_click_login(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to vip button"):
            home_page.move_to_vip_button()

        with allure.step("click the login button"):
            home_page.click(home_page.login_button_vip)

        with allure.step("verify login page shown"):
            home_page.verify_login_page_shown()

    @pytest.mark.home
    def test_history_click_login(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("move the mouse to the view history button"):
            home_page.move_to_view_history_button()

        with allure.step("click the login button"):
            home_page.click(home_page.login_button_history)

        with allure.step("Verify login page shown"):
            home_page.verify_login_page_shown()

    @pytest.mark.home
    def test_profile_click_login(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("Move the mouse to profile button"):
            home_page.move_to_profile_button()

        with allure.step("click the login button"):
            home_page.click(home_page.login_button_profile)

        with allure.step("verify login page shown"):
            home_page.verify_login_page_shown()
