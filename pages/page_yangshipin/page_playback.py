import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from base.base_page import BasePage
from utils.assert_util import *
from utils.logs_util import logger

class PlayPage(BasePage):
    # playback related elements
    video_class = (By.CSS_SELECTOR, ".video-js.vjs-default-skin.vjs-big-play-centered")
    video_full_screen = (By.CSS_SELECTOR, ".y-full-bg")
    home_video = (By.CSS_SELECTOR, ".boxTip.actComWidth-item")
    play_button = (By.CSS_SELECTOR, ".play.play2")
    paused_button = (By.CSS_SELECTOR, ".play.play1")
    full_screen_button = (By.CSS_SELECTOR, ".full.full2")
    loading = (By.CSS_SELECTOR, ".loading.black-bg")

    def move_mouse_during_playback(self):
        """
        move the mouse during playback in order to make progress bar shows
        :return: None
        """
        ele = self.find_element(self.video_class)
        actions = ActionChains(self.driver)
        actions.move_to_element(ele).perform()

    def play_random_video_from_home(self):
        """
        random click one video from the home page
        :return: None
        """
        self.click(self.home_video)

        # wait until video start playing
        self.switch_to_window()
        self.wait_for_playback_loaded()

    def wait_for_playback_loaded(self, timeout=60):
        """
        wait until loading text dismissed
        :param timeout: timeout seconds
        :return: None
        """
        start_time = time.time()
        while time.time() - start_time < timeout:
            loading = self.element_exist(self.loading, retry=1, timeout=3)
            if loading:
                logger.info("still loading, wait for 2 seconds")
                time.sleep(2)
            else:
                return

    def select_pause_in_progress_bar(self):
        """
        select play button in the progress bar to pause the video
        :return: None
        """
        self.move_mouse_during_playback()
        self.click(self.play_button)

    def select_play_in_progress_bar(self):
        """
        select pause button in the progress bar to play the video
        :return: None
        """
        self.move_mouse_during_playback()
        self.click(self.paused_button)
        self.wait_for_playback_loaded()

    def go_to_full_screen(self, click_full_screen_button=True):
        """
        make video to full screen mode
        :param click_full_screen_button: if True, will click the full screen button, if False, will double-click on the video
        :return: None
        """
        if click_full_screen_button:
            logger.info("click the full screen video in the progress bar")
            self.move_mouse_during_playback()
            self.click(self.full_screen_button)
        else:
            logger.info("double click on the video")
            ele = self.find_element(self.video_class)
            actions = ActionChains(self.driver)
            actions.double_click(ele).perform()

    def verify_video_is_playing(self):
        """
        verify the video is playing by checking the time increased
        :return: None
        """
        ele = self.find_element(self.video_class)
        initial_time = self.driver.execute_script("return arguments[0].currentTime;", ele)
        time.sleep(5)  # play for 5 seconds
        current_time = self.driver.execute_script("return arguments[0].currentTime;", ele)
        logger.info(f"initial_time is {initial_time}, current_time is {current_time}")
        assert_greater(initial_time, 0, "initial_time is not greater than 0, the video not played successfully")
        assert_greater(current_time, 0, "current_time is not greater than 0, the video not played successfully")
        assert_greater(current_time, initial_time, "the video is not playing")

    def verify_video_is_paused(self):
        """
        verify the video is paused by check the time not changed
        :return: None
        """
        ele = self.find_element(self.video_class)
        initial_time = self.driver.execute_script("return arguments[0].currentTime;", ele)
        time.sleep(5)  # play for 5 seconds
        current_time = self.driver.execute_script("return arguments[0].currentTime;", ele)
        assert_greater(initial_time, 0, "initial_time is not greater than 0, the video not played successfully")
        assert_greater(current_time, 0, "current_time is not greater than 0, the video not played successfully")
        assert_equal(current_time, initial_time, "the video is not paused.")

    def verify_video_in_full_screen(self):
        """
        verify the video is playing in full screen
        :return: None
        """
        window_size = self.driver.get_window_size()
        screen_width = self.driver.execute_script("return screen.width;")
        screen_height = self.driver.execute_script("return screen.height;")
        assert_true(window_size['width'] == screen_width and window_size['height'] == screen_height, "video is not played in full screen")