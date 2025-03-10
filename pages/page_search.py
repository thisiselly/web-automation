import time
import random

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from pages.page_playback import PlayPage
from utils.assert_util import verification
from utils.logs_util import logger


class SearchPage(BasePage):

    # 当前页面的元素定位
    search_text = (By.CSS_SELECTOR, "#search")
    search_icon = (By.CSS_SELECTOR, ".search-dark")
    search_result = (By.CSS_SELECTOR, ".search-result-l-item")
    selected_button = (By.CSS_SELECTOR, ".act")
    comprehensive_button = (By.XPATH, '//div[text()="综合"]')
    live_button = (By.XPATH, '//div[text()="直播"]')
    album_button = (By.XPATH, '//div[text()="专辑"]')
    video_button = (By.XPATH, '//div[text()="视频"]')
    no_search_result_text = (By.XPATH, "//p[text()='抱歉，没有找到相关视频']")
    no_search_result_icon = (By.XPATH, '//img[@src="https://img.yangshipin.cn/assets/7261661501599_.pic-l7a7wxcxi8yg.jpg"]')
    search_title = (By.CSS_SELECTOR, 'h3.overflow-1')
    search_poster= (By.CSS_SELECTOR, '.img.tobig')
    corner_makers= (By.CSS_SELECTOR, '.corner-marker')



    # 当前页面的方法
    def switch_to_current_window(self):
        self.switch_to_window(to_home_window=False)

    def input_search_content(self, content):
        logger.info(f"input search string {content}")
        self.clear(self.search_text)
        self.send_keys(self.search_text, content)

    def click_search_button(self):
        logger.info("select Search button")
        self.click(self.search_icon)

    def wait_for_search_page_loaded(self):
        self.find_element(self.search_result)

    def wait_for_button_selected(self, locator, retry=3):
        attempt = 0
        while attempt < retry:
            if self.is_button_selected(locator) == True:
                break
            else:
                logger.info(f"button {locator} is not selected, retrying {attempt} time")
                time.sleep(1)
                attempt += 1

    def is_button_selected(self, locator, expect=True):
        actual_selected_text = self.get_text(self.selected_button)
        if actual_selected_text in locator[1]:
            return True
        else:
            return False

    def select_comprehensive_tab(self):
        logger.info("select the comprehensive tab")
        self.click(self.comprehensive_button)
        self.wait_for_button_selected(self.comprehensive_button)

    def select_live_tab(self):
        logger.info("select the live tab")
        self.click(self.live_button)
        self.wait_for_button_selected(self.live_button)

    def select_album_tab(self):
        logger.info("select the album tab")
        self.wait_for_search_page_loaded()
        self.click(self.album_button)
        self.wait_for_button_selected(self.album_button)

    def select_video_tab(self):
        logger.info("select the video tab")
        self.click(self.video_button)
        self.wait_for_button_selected(self.video_button)

    def verify_empty_search_result(self):
        no_search_text_displayed = self.element_exist(self.no_search_result_text)
        no_search_icon_displayed = self.element_exist(self.no_search_result_icon)
        verification.assertion(no_search_text_displayed, "==", True)
        verification.assertion(no_search_icon_displayed, "==", True)

    def get_all_displayed_title(self):
        all_ele = self.find_elements(self.search_title)
        displayed_title = []
        for ele in all_ele:
            displayed_title.append(ele.text)
        return displayed_title

    def verify_search_text_correct(self, context):
        actual_text = self.get_all_displayed_title()
        expect_text = context
        result = all(expect_text in x for x in actual_text)
        verification.assertion(True, "==", result)

    def select_first_video_in_search_result(self):
        self.click(self.search_poster)

    def verify_video_playback_success(self):
        time.sleep(5)
        play_page = PlayPage(self.driver)
        play_page.verify_video_is_playing()

    def verify_icon_displays_for_live(self):
        icon_displayed = True
        all_corner_makers = self.find_elements(self.corner_makers)
        for corner_maker in all_corner_makers:
            child_class = corner_maker.find_element(By.XPATH, "./div").get_attribute("class")
            if child_class != "live" or child_class != "order":
                icon_displayed = False
                return

        verification.assertion(icon_displayed, "==", True, "live or order icon not displayed for all live programs")


