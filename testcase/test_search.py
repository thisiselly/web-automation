import time

from selenium.webdriver.common.by import By

from pages.page_search import SearchPage


class TestSearch:
    def test_search_default_highlight(self, open_browser):
        search_page = SearchPage(open_browser)
        search_page.input_search_content("test")
        search_page.click_search_button()
        search_page.switch_to_search_window()
        search_page.is_button_selected(search_page.comprehensive_button)
        search_page.close()
        search_page.switch_to_window(True)
        time.sleep(4)

    def test_search_not_selected(self, open_browser):
        search_page = SearchPage(open_browser)
        search_page.input_search_content("test")
        search_page.click_search_button()
        search_page.switch_to_search_window()
        search_page.is_button_selected(search_page.live_button, expect=False)
        search_page.is_button_selected(search_page.album_button, expect=False)
        search_page.is_button_selected(search_page.video_button, expect=False)
        search_page.close()
        search_page.switch_to_window(True)
        time.sleep(4)


    def test_search_no_live(self, open_browser):
        search_page = SearchPage(open_browser)
        search_page.input_search_content("没有直播")
        search_page.click_search_button()
        search_page.switch_to_search_window()
        search_page.select_live_tab()
        search_page.verify_empty_search_result()
        search_page.close()
        search_page.switch_to_window(True)
        time.sleep(4)

    def test_search_no_album(self, open_browser):
        search_page = SearchPage(open_browser)
        search_page.input_search_content("没有专辑")
        search_page.click_search_button()
        search_page.switch_to_search_window()
        search_page.select_album_tab()
        search_page.verify_empty_search_result()
        search_page.close()
        search_page.switch_to_window(True)
        time.sleep(4)



    def test_search_movie(self, open_browser):
        search_page = SearchPage(open_browser)
        search_page.input_search_content("hello")
        search_page.click_search_button()
        time.sleep(3)
        search_page.switch_to_window()
        aa = open_browser.find_element(By.CSS_SELECTOR,'.searchA-item-r.search-s-r').text.split("\n")[0]
        print("!!!!!!!!!!!",aa,"!!!!!!!!!!!")
        bb = open_browser.find_element(By.CSS_SELECTOR, '.searchB-item-i-r.search-s-r>h3').text
        print("~~~~~~~~~", bb, "~~~~~~~~~")
        time.sleep(22)