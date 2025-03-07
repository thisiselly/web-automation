import time

from selenium.webdriver.common.by import By

from base.base_page import BasePage


class PlayPage(BasePage):
    video_class = (By.CSS_SELECTOR, ".video-js.vjs-default-skin.vjs-big-play-centered")
    home_video = (By.CSS_SELECTOR, ".boxTip.actComWidth-item")


    def play_random_from_home(self):
        self.click(self.home_video)

    def verify_video_is_playing(self):
        ele = self.find_element(self.video_class)
        initial_time = self.driver.execute_script("return arguments[0].currentTime;", ele)
        time.sleep(2)  # 等待2秒
        current_time = self.driver.execute_script("return arguments[0].currentTime;", ele)
        if current_time > initial_time:
            print("the video is playing")
        else:
            print("the video is not playing")