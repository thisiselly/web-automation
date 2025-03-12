from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils.assert_util import *


class PageSourceDemo(BasePage):
    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_button = (By.XPATH, '//h3[@data-test="error"]')
    inventory_list = (By.CSS_SELECTOR, ".inventory_list")

    def verify_login_with_credential(self, username, password):
        valid_username, valid_password = "standard_user", "secret_sauce"
        no_username_msg, no_password_msg = "Epic sadface: Username is required", "Epic sadface: Password is required"
        incorrect_credential_msg = "Epic sadface: Username and password do not match any user in this service"

        self.send_keys(self.username_input, username)
        self.send_keys(self.password_input, password)
        self.click(self.login_button)

        if username == "" :
            actual_msg = self.get_text(self.error_button)
            assert_equal(no_username_msg, actual_msg, "error msg not shown when username is empty")
        elif password == "":
            actual_msg = self.get_text(self.error_button)
            assert_equal(no_password_msg, actual_msg, "error msg not shown when password is empty")
        elif username != valid_username or password != valid_password:
            actual_msg = self.get_text(self.error_button)
            assert_equal(incorrect_credential_msg, actual_msg, "error msg not shown when username or password is incorrect")
        elif username == valid_username and password == valid_password:
            inventory_list_shown = self.element_exist(self.inventory_list)
            assert_true(inventory_list_shown, "login success.")

