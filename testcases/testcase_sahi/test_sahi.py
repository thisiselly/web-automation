from pages.page_sahi.page_sahi import SahiHomePage


class TestSahi:
    def test_alert(self, open_sahi):
        alert_msg = "hello world"
        sahi_home_page = SahiHomePage(open_sahi)
        sahi_home_page.go_to_alert_test()
        sahi_home_page.clear_alert_message()
        sahi_home_page.input_alert_message(alert_msg)
        sahi_home_page.click_for_alert()
        sahi_home_page.verify_alert_msg_in_pop_window(alert_msg)

    def test_alert_multilines(self, open_sahi):
        expect_msg = "You must correct the following Errors:\nYou must select a messaging price plan.\nYou must select an international messaging price plan.\nYou must enter a value for the Network Lookup Charge"
        sahi_home_page = SahiHomePage(open_sahi)
        sahi_home_page.go_to_alert_test()
        sahi_home_page.click_for_multiline_alert()
        sahi_home_page.verify_alert_multiline_msg(expect_msg)

    def test_alert_multilines_unicode(self, open_sahi):
        expect_msg = 'Verifique se todos os campos obrigatórios foram preenchidos.\n\nProduto:required.'
        sahi_home_page = SahiHomePage(open_sahi)
        sahi_home_page.go_to_alert_test()
        sahi_home_page.click_multiline_unicode()
        sahi_home_page.verify_alert_multiline_unicode_msg(expect_msg)

    def test_confirm_msg_accept(self, open_sahi):
        sahi_home_page = SahiHomePage(open_sahi)
        sahi_home_page.go_to_confirm_page()
        sahi_home_page.click_for_confirm()
        sahi_home_page.alert_window_accept()
        sahi_home_page.verify_confirm_msg_when_accept()

    def test_confirm_msg_dismiss(self, open_sahi):
        sahi_home_page = SahiHomePage(open_sahi)
        sahi_home_page.go_to_confirm_page()
        sahi_home_page.click_for_confirm()
        sahi_home_page.alert_window_dismiss()
        sahi_home_page.verify_confirm_msg_when_dismiss()

    def test_prompt_msg_correct(self, open_sahi):
        test_mgs = "hello world"
        sahi_home_page = SahiHomePage(open_sahi)
        sahi_home_page.go_to_prompt_page()
        sahi_home_page.click_for_prompt()
        sahi_home_page.alert_window_send_keys(test_mgs)
        sahi_home_page.alert_window_accept()
        sahi_home_page.verify_prompt_msg_after_input(test_mgs)

    def test_select(self, open_sahi):
        sahi_home_page = SahiHomePage(open_sahi)
        sahi_home_page.go_to_select_page()
        sahi_home_page.select_all_test()

    def test_click(self, open_sahi):
        sahi_home_page = SahiHomePage(open_sahi)
        sahi_home_page.go_to_clicks_page()
        sahi_home_page.select_clear_button()
        sahi_home_page.single_click()
        sahi_home_page.verify_msg_in_click_window(click=True)

        sahi_home_page.select_clear_button()
        sahi_home_page.double_click()
        sahi_home_page.verify_msg_in_click_window(double_click=True)

        sahi_home_page.select_clear_button()
        sahi_home_page.right_click()
        sahi_home_page.verify_msg_in_click_window(right_click=True)

    def test_disabled_button(self, open_sahi):
        sahi_home_page = SahiHomePage(open_sahi)
        sahi_home_page.go_to_clicks_page()
        sahi_home_page.verify_button_disabled()

    def test_move_mouse(self, open_sahi):
        sahi_home_page = SahiHomePage(open_sahi)
        sahi_home_page.go_to_mouse_over_page()
        sahi_home_page.move_mouse_to_button1()
        sahi_home_page.verify_text_in_first_output("Mouse moved")
        sahi_home_page.move_mouse_to_button2()
        sahi_home_page.verify_text_in_first_output("")
        sahi_home_page.move_mouse_to_zone_area()
        sahi_home_page.verify_text_in_second_output("mouseOver")

    def test_drag_and_drop(self, open_sahi):
        sahi_home_page = SahiHomePage(open_sahi)
        sahi_home_page.go_to_drag_drop_test()
        sahi_home_page.drag_item_to_all_windows()
        sahi_home_page.verify_all_items_dropped()

    def test_upload_files_by_sendkeys(self, open_sahi):
        sahi_home_page = SahiHomePage(open_sahi)
        sahi_home_page.go_to_file_upload_test()
        sahi_home_page.upload_file_by_send_keys()
        sahi_home_page.click_submit_single_button()

    # def test_upload_files_by_keyboard(self, open_sahi):
    #     sahi_home_page = SahiHomePage(open_sahi)
    #     sahi_home_page.go_to_file_upload_test()
    #     sahi_home_page.upload_file_by_keyboard()
    #     sahi_home_page.click_submit_single_button(2)

