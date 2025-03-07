import time

from pages.page_playback import PlayPage


class TestPlayback:
    def test_playback_success(self, open_browser):
        play_page = PlayPage(open_browser)
        play_page.play_random_from_home()
        play_page.switch_to_window()
        time.sleep(5)
        play_page.verify_video_is_playing()
        play_page.close()
        play_page.switch_to_window(to_parental_window=True)