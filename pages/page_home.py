from selenium.webdriver.common.by import By

from base.base_page import BasePage
from utils.assert_util import verification


class HomePage(BasePage):
    # 首页按钮
    # agree_button = (By.CSS_SELECTOR, '.winE-policy-close-b')
    vip_button = (By.CSS_SELECTOR, '.header-b-r-item1-img')
    view_history_button = (By.CSS_SELECTOR, '.header-b-r-item2-img')
    creator_button = (By.CSS_SELECTOR, '.header-b-r-item3-img')
    scan_button = (By.CSS_SELECTOR, '.header-b-r-item4-img')
    profile_button = (By.CSS_SELECTOR, '.header-b-r-item5')
    login_page = (By.CSS_SELECTOR, '.ysplogin-signin')
    close_login_button = (By.CSS_SELECTOR, '.ysplogin-icon-svg')

    # 悬浮窗口
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

    # 当前页面的方法
    # def select_agree_button(self):
    #     if self.element_exist(self.agree_button, timeout=2) == False:
    #         logger.info("the agree button does not shown, skip")
    #         return
    #     else:
    #         logger.info("the agree button does is shown, click on it.")
    #         self.click(self.agree_button)
    #

    def select_vip_button(self):
        self.click(self.vip_button)

    def move_to_vip_button(self):
        self.move_to_mouse(self.vip_button)

    def select_view_history_button(self):
        self.click(self.view_history_button)

    def move_to_view_history_button(self):
        self.move_to_mouse(self.view_history_button)

    def select_creator_button(self):
        self.click(self.creator_button)

    def move_to_creator_button(self):
        self.move_to_mouse(self.creator_button)

    def select_scan_button_button(self):
        self.click(self.scan_button)

    def move_to_scan_button(self):
        self.move_to_mouse(self.scan_button)

    def select_profile_button(self):
        self.click(self.profile_button)

    def move_to_profile_button(self):
        self.move_to_mouse(self.profile_button)

    def login_page_show(self):
        return self.element_exist(self.login_page)

    def close_login_window(self):
        self.click(self.close_login_button)

    def verify_login_page_show(self, expect_shown = True):
        actual_shown = self.element_exist(self.login_page)
        verification.assertion(expect_shown, "==", actual_shown)

    def switch_to_home_window(self):
        self.switch_to_window(to_parental_window=True)

    def switch_to_history_window(self):
        self.switch_to_window(to_parental_window=False)

    def switch_to_profile_window(self):
        self.switch_to_window(to_parental_window=False)

    def switch_to_search_window(self):
        self.switch_to_window(to_parental_window=False)
