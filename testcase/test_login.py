import time

import allure
import pytest
from selenium.webdriver.common.by import By

from pages.page_home import HomePage


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




    # @pytest.mark.parametrize("phone_number, code", )
    # def test_login_fail(self, open_browser, phone_number,code):
    #     allure.dynamic.title(f"phone number is :{phone_number}")
    #     pass