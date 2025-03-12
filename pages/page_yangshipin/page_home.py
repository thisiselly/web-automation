import time

from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils.assert_util import *


class HomePage(BasePage):
    # home buttons
    vip_button = (By.CSS_SELECTOR, '.header-b-r-item1-img')
    view_history_button = (By.CSS_SELECTOR, '.header-b-r-item2-img')
    creator_button = (By.CSS_SELECTOR, '.header-b-r-item3-img')
    scan_button = (By.CSS_SELECTOR, '.header-b-r-item4-img')
    profile_button = (By.CSS_SELECTOR, '.header-b-r-item5')
    login_page = (By.CSS_SELECTOR, '.ysplogin-signin')
    close_login_button = (By.CSS_SELECTOR, '.ysplogin-icon-svg')
    signin_agree_radio_button = (By.CSS_SELECTOR, '.ysplogin-signin-agree-chickable')

    # hover windows
    win_vip = (By.CSS_SELECTOR, '.winG-mask-unLogin-top-title')
    login_button_vip = (By.CSS_SELECTOR, '.winG-mask-unLogin-bottom-img')

    win_history = (By.CSS_SELECTOR, '.winD-history-box')
    win_history_head = (By.CSS_SELECTOR, '.winD-history-box-head')
    login_button_history = (By.CSS_SELECTOR, '.winD-history-box-login')

    win_creator = (By.CSS_SELECTOR, '.winY-mask.fontSet')
    win_creator_platform = (By.XPATH, '//p[text()="创作者平台"]')
    win_creator_checkin = (By.XPATH, '//p[text()="创作者入驻"]')

    win_scan = (By.CSS_SELECTOR, '.winB.fontSet')
    win_scan_text = (By.CSS_SELECTOR, '.winB-txt.cp')
    win_scan_icon = (By.CSS_SELECTOR, 'img[src="https://img.yangshipin.cn/assets/a15-l6op37dmbzm2.png"]')

    win_profile = (By.CSS_SELECTOR, '.winA-mask-unLogin-top-title')
    login_button_profile = (By.CSS_SELECTOR, '.winA-mask-unLogin-bottom-img')

    # wechat popup window
    wechat_button = (By.CSS_SELECTOR, '.ysplogin-signin-extra-buttun.ysplogin-signin-btnwx')
    wechat_tips = (By.CSS_SELECTOR, '.web_qrcode_tips.js_web_qrcode_tips_normal')
    wechat_app_name = (By.CSS_SELECTOR, '.web_qrcode_app')
    wechat_qrcode_img = (By.CSS_SELECTOR, '.js_qrcode_img.web_qrcode_img')

    def select_vip_button(self):
        """
        select the vip button in home page
        :return:
        """
        self.click(self.vip_button)

    def move_to_vip_button(self):
        """
        move the mouse to vip button in home page
        :return:
        """
        self.move_to_mouse(self.vip_button)

    def select_view_history_button(self):
        """
        select the view history button in home page
        :return:
        """
        self.click(self.view_history_button)

    def move_to_view_history_button(self):
        """
        move the mouse to view history button in home page
        :return:
        """
        self.move_to_mouse(self.view_history_button)

    def select_creator_button(self):
        """
        select the creator button in home page
        :return:
        """
        self.click(self.creator_button)

    def move_to_creator_button(self):
        """
        move the mouse to creator button in home pgae
        :return:
        """
        self.move_to_mouse(self.creator_button)

    def select_scan_button_button(self):
        """
        select the scan button in home page
        :return:
        """
        self.click(self.scan_button)

    def move_to_scan_button(self):
        """
        move to mouse to scan button in home page
        :return:
        """
        self.move_to_mouse(self.scan_button)

    def select_profile_button(self):
        """
        select the profile button in home page
        :return:
        """
        self.click(self.profile_button)

    def move_to_profile_button(self):
        """
        move the mouse to profile button in home page
        :return:
        """
        self.move_to_mouse(self.profile_button)

    def close_login_window(self):
        """
        close the login pop up window
        :return:
        """
        self.click(self.close_login_button)

    def verify_login_page_shown(self):
        """
        verify the login page displays
        :return:
        """
        is_shown = self.element_exist(self.login_page)
        assert_true(is_shown, "login page is not shown as expect")

    def click_signin_agree_button(self):
        """
        click the signin agree button in login window
        :return:
        """
        time.sleep(1)
        self.click(self.signin_agree_radio_button)

    def click_wechat_button(self):
        """
        click the wechat button in login window
        :return:
        """
        self.click(self.wechat_button)

    def verify_wechat_window_displays(self):
        """
        verify the wechat login window popup
        :return:
        """
        time.sleep(3)
        self.switch_to_current_window()
        actual_window_title = self.driver.title
        assert_equal("微信登录", actual_window_title, "wechat window is not shown as expect")

    def switch_to_home_window(self):
        """
        switch the driver to the home window
        :return:
        """
        self.switch_to_window(to_home_window=True)

    def switch_to_current_window(self):
        """
        switch the driver to the current opening window
        :return:
        """
        self.switch_to_window(to_home_window=False)



