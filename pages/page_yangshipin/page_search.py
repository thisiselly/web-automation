import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage
from pages.page_yangshipin.page_playback import PlayPage
from utils.assert_util import *
from utils.logs_util import logger


class SearchPage(BasePage):

    # elements in search page
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

    def switch_to_search_window(self):
        """
        switch the driver to the search window
        :return:
        """
        self.switch_to_window(to_home_window=False)

    def input_search_content(self, content):
        """
        input the search content
        :param content:
        :return:
        """
        logger.info(f"input search string: {content}")
        self.clear(self.search_text)
        self.send_keys(self.search_text, content)

    def click_search_button(self):
        """
        click the search button and switch the driver to the new window
        :return:
        """
        logger.info("select Search button")
        self.click(self.search_icon)
        self.switch_to_search_window()

    def wait_for_search_page_loaded(self):
        """
        wait for the search page load success
        :return:
        """
        self.find_element(self.search_result)

    def wait_for_tab_selected(self, locator, retry=3):
        """
        wait for the tab is selected
        :param locator: the locator of the tab
        :param retry: retry times
        :return:
        """
        attempt = 0
        while attempt < retry:
            if self.is_button_selected(locator):
                break
            else:
                logger.info(f"button {locator} is not selected, retrying {attempt} time(s)")
                time.sleep(1)
                attempt += 1

    def is_button_selected(self, locator):
        """
        checking the button is selected or not
        :param locator: the locator
        :return: True or False
        """
        actual_selected_text = self.get_text(self.selected_button)
        if actual_selected_text in locator[1]:
            return True
        else:
            return False

    def verify_button_is_selected(self, locator, expect_result=True):
        """
        verify the button is selected or not
        :param locator: the locator
        :param expect_result: True or False
        :return:
        """
        actual_result = self.is_button_selected(locator)
        assert_equal(expect_result, actual_result, "button is not selected as expect.")

    def select_comprehensive_tab(self):
        """
        select the comprehensive tab
        :return:
        """
        logger.info("select the comprehensive tab")
        self.click(self.comprehensive_button)
        self.wait_for_tab_selected(self.comprehensive_button)

    def select_live_tab(self):
        """
        select the live tab
        :return:
        """
        logger.info("select the live tab")
        self.click(self.live_button)
        self.wait_for_tab_selected(self.live_button)

    def select_album_tab(self):
        """
        select the album tab
        :return:
        """
        logger.info("select the album tab")
        self.wait_for_search_page_loaded()
        self.click(self.album_button)
        self.wait_for_tab_selected(self.album_button)

    def select_video_tab(self):
        """
        select the video tab
        :return:
        """
        logger.info("select the video tab")
        self.click(self.video_button)
        self.wait_for_tab_selected(self.video_button)

    def verify_empty_search_result(self):
        """
        verify when no result, it shows correct text and icon
        :return:
        """
        no_search_text_displayed = self.element_exist(self.no_search_result_text)
        no_search_icon_displayed = self.element_exist(self.no_search_result_icon)
        assert_true(no_search_text_displayed, "no search result text is not shown as expect")
        assert_true(no_search_icon_displayed, "no search result icon is not shown as expect")

    def get_all_displayed_title(self):
        """
        get all displayed title
        :return: list of all displays titles
        """
        all_ele = self.find_elements(self.search_title)
        displayed_title = []
        for ele in all_ele:
            displayed_title.append(ele.text)
        return displayed_title

    def verify_search_text_correct(self, context):
        """
        verify all displays titles contains correct context
        :param context:
        :return:
        """
        actual_text = self.get_all_displayed_title()
        expect_text = context
        result = all(expect_text in x for x in actual_text)
        assert_true(result, f"not all displays title contains search string {context}, actual_text: {actual_text}")


    def select_first_video_in_search_result(self):
        """
        select the first video poster in search result
        :return:
        """
        self.click(self.search_poster)
        self.switch_to_search_window()

    def verify_video_playback_success(self):
        """
        verify the video playback success
        :return:
        """
        play_page = PlayPage(self.driver)
        play_page.wait_for_playback_loaded()
        play_page.verify_video_is_playing()

    def verify_icon_displays_for_live(self):
        """
        verify the live or order icon displays for all live programs
        :return:
        """
        icon_displayed = True
        all_corner_makers = self.find_elements(self.corner_makers)
        for corner_maker in all_corner_makers:
            child_class = corner_maker.find_element(By.XPATH, "./div").get_attribute("class")
            if child_class != "live" or child_class != "order" or child_class != "reback":
                icon_displayed = False

        assert_true(icon_displayed, f"live or order or reback icon not displayed for all live programs, actual:{all_corner_makers}")


