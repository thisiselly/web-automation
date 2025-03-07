from selenium.webdriver.common.by import By

from base.base_page import BasePage
from utils.assert_util import verification
from utils.logs_util import logger


class SearchPage(BasePage):

    # 当前页面的元素定位
    search_text = (By.CSS_SELECTOR, "#search")
    search_icon = (By.CSS_SELECTOR, ".search-dark")
    selected_button = (By.CSS_SELECTOR, ".act")
    comprehensive_button = (By.XPATH, '//div[text()="综合"]')
    live_button = (By.XPATH, '//div[text()="直播"]')
    album_button = (By.XPATH, '//div[text()="专辑"]')
    video_button = (By.XPATH, '//div[text()="视频"]')
    no_search_result_text = (By.XPATH, "//p[text()='抱歉，没有找到相关视频']")
    no_search_result_icon = (By.XPATH, '//img[@src="https://img.yangshipin.cn/assets/7261661501599_.pic-l7a7wxcxi8yg.jpg"]')



    # 当前页面的方法
    def switch_to_search_window(self):
        self.switch_to_window(to_parental_window=False)

    def input_search_content(self, content):
        logger.info(f"input search string {content}")
        self.clear(self.search_text)
        self.send_keys(self.search_text, content)

    def click_search_button(self):
        logger.info("select Search button")
        self.click(self.search_icon)

    def is_button_selected(self, locator, expect=True):
        actual_selected_text = self.get_text(self.selected_button)
        if expect:
            logger.info(f"the button {locator} is selected as expect")
            verification.assertion(actual_selected_text, "in", locator[1])
        else:
            logger.info(f"the button {locator} is not selected as expect")
            verification.assertion(actual_selected_text, "not in", locator[1])

    def select_comprehensive_tab(self):
        logger.info("select the comprehensive tab")
        self.click(self.comprehensive_button)
        self.is_button_selected(self.comprehensive_button)

    def select_live_tab(self):
        logger.info("select the live tab")
        self.click(self.live_button)
        self.is_button_selected(self.live_button)

    def select_album_tab(self):
        logger.info("select the album tab")
        self.click(self.album_button)
        self.is_button_selected(self.album_button)

    def select_video_tab(self):
        logger.info("select the video tab")
        self.click(self.video_button)
        self.is_button_selected(self.video_button)

    def verify_empty_search_result(self):
        no_search_text_displayed = self.element_exist(self.no_search_result_text)
        no_search_icon_displayed = self.element_exist(self.no_search_result_icon)
        verification.assertion(no_search_text_displayed, "==", True)
        verification.assertion(no_search_icon_displayed, "==", True)