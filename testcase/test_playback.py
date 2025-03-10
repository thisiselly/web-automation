import time

import allure
import pytest

from pages.page_playback import PlayPage

@allure.epic("Playback Test")
@allure.feature("playback test cases")
class TestPlayback:
    @pytest.mark.playback
    def test_playback_success(self, open_browser):
        with allure.step("go to home page"):
            play_page = PlayPage(open_browser)

        with allure.step("play a video from home page"):
            play_page.play_random_video_from_home()

        with allure.step("verify the video is playing success"):
            play_page.verify_video_is_playing()


    @pytest.mark.playback
    def test_paused_success(self, open_browser):
        with allure.step("go to home page"):
            play_page = PlayPage(open_browser)

        with allure.step("play a video from home page"):
            play_page.play_random_video_from_home()

        with allure.step("pause the video during playback"):
            play_page.select_pause_in_progress_bar()
            play_page.verify_video_is_paused()

        with allure.step("select the pause button to continue play the video"):
            play_page.select_play_in_progress_bar()

        with allure.step("verify the video continue playback"):
            play_page.verify_video_is_playing()


    @pytest.mark.playback
    def test_click_full_screen_button(self, open_browser):
        with allure.step("go to home page"):
            play_page = PlayPage(open_browser)

        with allure.step("play a video from home page"):
            play_page.play_random_video_from_home()

        with allure.step("click full screen button in the progress bar"):
            play_page.go_to_full_screen()

        with allure.step("verify video played in full screen"):
            play_page.verify_video_in_full_screen()

    @pytest.mark.playback
    def test_double_click_on_video(self, open_browser):
        with allure.step("go to home page"):
            play_page = PlayPage(open_browser)

        with allure.step("play a video from home page"):
            play_page.play_random_video_from_home()

        with allure.step("double click on the played video"):
            play_page.go_to_full_screen(click_full_screen_button=False)
            time.sleep(6)

        with allure.step("verify video played in full screen"):
            play_page.verify_video_in_full_screen()
