import allure
import pytest
from pages.page_yangshipin.page_search import SearchPage
from utils.read_files import read_yaml_file


@allure.epic("Search Test")
@allure.feature("search test cases")
class TestSearch:
    @pytest.mark.search
    def test_search_default_highlight(self, open_browser):
        search_string = "test"
        with allure.step("go to home page"):
            search_page = SearchPage(open_browser)

        with allure.step(f"input {search_string} in search page"):
            search_page.input_search_content(search_string)

        with allure.step("click on the search button"):
            search_page.click_search_button()

        with allure.step("verify the comprehensive button is highlighted by default"):
            search_page.verify_button_is_selected(search_page.comprehensive_button)

    @pytest.mark.search
    def test_search_not_selected(self, open_browser):
        search_string = "test"
        with allure.step("go to home page"):
            search_page = SearchPage(open_browser)

        with allure.step(f"input {search_string} in search page"):
            search_page.input_search_content(search_string)

        with allure.step("click on the search button"):
            search_page.click_search_button()

        with allure.step("verify the other buttons are not highlighted by default"):
            search_page.verify_button_is_selected(search_page.live_button, expect_result=False)
            search_page.verify_button_is_selected(search_page.album_button, expect_result=False)
            search_page.verify_button_is_selected(search_page.video_button, expect_result=False)

    @pytest.mark.search
    def test_search_no_result(self, open_browser):
        search_string = "!!!!!!"
        with allure.step("go to home page"):
            search_page = SearchPage(open_browser)
        with allure.step(f"input {search_string} in search page"):
            search_page.input_search_content(search_string)

        with allure.step("click on the search button"):
            search_page.click_search_button()

        with allure.step("verify no result on comprehensive tab"):
            search_page.select_comprehensive_tab()
            search_page.verify_empty_search_result()

        with allure.step("verify no result on live tab"):
            search_page.select_live_tab()
            search_page.verify_empty_search_result()

        with allure.step("verify no result on album tab"):
            search_page.select_album_tab()
            search_page.verify_empty_search_result()

        with allure.step("verify no result on video tab"):
            search_page.select_video_tab()
            search_page.verify_empty_search_result()

    @pytest.mark.parametrize("search_string", read_yaml_file()["search_data"])
    @pytest.mark.search
    def test_search_program(self, open_browser, search_string):
        with allure.step("go to home page"):
            search_page = SearchPage(open_browser)

        with allure.step(f"input {search_string} in search page"):
            search_page.input_search_content(search_string)

        with allure.step("click on the search button"):
            search_page.click_search_button()

        with allure.step(f"verify all search title contains word {search_string}"):
            search_page.verify_search_text_correct(search_string)

    @pytest.mark.search
    def test_select_live_from_search(self, open_browser):
        search_string = "NBA"
        with allure.step("go to home page"):
            search_page = SearchPage(open_browser)

        with allure.step(f"input {search_string} in search page"):
            search_page.input_search_content(search_string)

        with allure.step("click on the search button"):
            search_page.click_search_button()

        with allure.step("select live tab"):
            search_page.select_live_tab()

        with allure.step("select a random live program"):
            search_page.select_first_video_in_search_result()

        with allure.step("verify the program can be played"):
            search_page.verify_video_playback_success()

    @pytest.mark.search
    def test_select_album_from_search(self, open_browser):
        search_string = "2025"
        with allure.step("go to home page"):
            search_page = SearchPage(open_browser)

        with allure.step(f"input {search_string} in search page"):
            search_page.input_search_content(search_string)

        with allure.step("click on the search button"):
            search_page.click_search_button()

        with allure.step("select live tab"):
            search_page.select_album_tab()

        with allure.step("select a random album program"):
            search_page.select_first_video_in_search_result()

        with allure.step("verify the program can be played"):
            search_page.verify_video_playback_success()

    @pytest.mark.search
    def test_select_video_from_search(self, open_browser):
        search_string = "super"
        with allure.step("go to home page"):
            search_page = SearchPage(open_browser)

        with allure.step(f"input {search_string} in search page"):
            search_page.input_search_content(search_string)

        with allure.step("click on the search button"):
            search_page.click_search_button()

        with allure.step("select video tab"):
            search_page.select_video_tab()

        with allure.step("select a random album program"):
            search_page.select_first_video_in_search_result()

        with allure.step("verify the program can be played"):
            search_page.verify_video_playback_success()

    def test_select_title_from_search(self, open_browser):
        pass

    @pytest.mark.search
    def test_displays_for_live(self, open_browser):
        search_string = "NBA"
        with allure.step("go to home page"):
            search_page = SearchPage(open_browser)

        with allure.step(f"input {search_string} in search page"):
            search_page.input_search_content(search_string)

        with allure.step("click on the search button"):
            search_page.click_search_button()

        with allure.step("select live tab"):
            search_page.select_live_tab()

        with allure.step("verify all live programs display correct icon"):
            search_page.verify_icon_displays_for_live()

    def test_displays_under_album(self, open_browser):
        pass

    def test_displays_under_video(self, open_browser):
        pass
