
import allure
from pages.page_yangshipin.page_home import HomePage


@allure.epic("LoginPage")
@allure.feature("login related cases")
class TestLogin:
    def test_login_select_wechat(self, open_browser):
        with allure.step("Go to home page"):
            home_page = HomePage(open_browser)

        with allure.step("select login button under profile"):
            home_page.move_to_profile_button()
            home_page.click(home_page.login_button_profile)

        with allure.step("click signin agree button"):
            home_page.click_signin_agree_button()

        with allure.step("click on wechat button"):
            home_page.click_wechat_button()

        with allure.step("verify wechat login window displays"):
            home_page.verify_wechat_window_displays()

