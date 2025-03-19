import time
from pywinauto import keyboard
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base_page import BasePage
from utils.assert_util import *
from utils.get_file_path import *


class SahiHomePage(BasePage):
    # all link text
    alert_test = (By.LINK_TEXT, "Alert Test")
    confirm_page = (By.LINK_TEXT, "Confirm Page")
    prompt_page = (By.LINK_TEXT, "Prompt Page")
    save_as_test = (By.LINK_TEXT, "Save As Test")
    file_upload_test = (By.LINK_TEXT, "File Upload Test")
    frames_test = (By.LINK_TEXT, "Frames Test")
    iframe_test = (By.LINK_TEXT, "IFrames Test")
    clicks_page = (By.LINK_TEXT, "Clicks Page")
    select_test = (By.LINK_TEXT, "Select Test")
    mouse_over = (By.LINK_TEXT, "Mouse over")
    drag_drop_test = (By.LINK_TEXT, "Drag Drop Test")

    # alert related elements
    alert_test_input = (By.XPATH, '//input[@name="t1"]')
    alert_button = (By.XPATH, '//input[@name="b1"]')
    multiline_alert_button = (By.XPATH, '//input[@name="b2"]')
    multiline_unicode_button = (By.XPATH, '//input[@name="b3"]')

    # confirm related elements
    confirm_test_input = (By.XPATH, '//input[@name="t1"]')
    confirm_button = (By.XPATH, '//input[@name="b1"]')

    # prompt related elements
    prompt_button = (By.XPATH, '//input[@name="b1"]')
    prompt_test_input = (By.XPATH, '//input[@name="t1"]')

    # click elements
    clear_button = (By.XPATH, '//input[@value="Clear"]')
    dlb_click_button = (By.XPATH, '//input[@value="dbl click me"]')
    click_me_button = (By.XPATH, '//input[@value="click me"]')
    right_click_button = (By.XPATH, '//input[@value="right click me"]')
    disabled_button = (By.XPATH, '//input[@value="disable1"]')

    # mouse elements
    write_on_hover = (By.CSS_SELECTOR, 'input[value="Write on hover"]')
    blank_on_hover = (By.CSS_SELECTOR, 'input[value="Blank on hover"]')
    mouse_text1 = (By.NAME, 't1')
    mouse_zone = (By.XPATH, '//div[text()="Experiment Zone MouseOver"]')
    mouse_text2 = (By.ID, 'result')

    # drag and dop
    the_dragger = (By.ID, "dragger")
    item1 = (By.XPATH, '//div[text()="Item 1"]')
    item2 = (By.XPATH, '//div[text()="Item 2"]')
    item3 = (By.XPATH, '//div[text()="Item 3"]')
    item4 = (By.XPATH, '//div[text()="Item 4"]')

    # file upload
    choose_file = (By.CSS_SELECTOR, "#file")
    submit_single_button = (By.CSS_SELECTOR, '[value="Submit Single"]')

    def go_to_alert_test(self):
        self.click(self.alert_test)

    def go_to_confirm_page(self):
        self.click(self.confirm_page)

    def go_to_prompt_page(self):
        self.click(self.prompt_page)

    def go_to_save_as_test(self):
        self.click(self.save_as_test)

    def go_to_file_upload_test(self):
        self.click(self.file_upload_test)

    def go_to_frames_test(self):
        self.click(self.frames_test)

    def go_to_iframe_test(self):
        self.click(self.iframe_test)

    def go_to_clicks_page(self):
        self.click(self.clicks_page)

    def go_to_select_page(self):
        self.click(self.select_test)

    def go_to_mouse_over_page(self):
        self.click(self.mouse_over)

    def go_to_drag_drop_test(self):
        self.click(self.drag_drop_test)

    def clear_alert_message(self):
        self.clear(self.alert_test_input)

    def input_alert_message(self, content):
        self.send_keys(self.alert_test_input, content)

    def click_for_alert(self):
        self.click(self.alert_button)

    def click_for_multiline_alert(self):
        self.click(self.multiline_alert_button)

    def click_multiline_unicode(self):
        self.click(self.multiline_unicode_button)

    def get_alert_msg_in_pop_window(self):
        alert_window = self.driver.switch_to.alert
        return alert_window.text

    def verify_alert_msg_in_pop_window(self, expect_msg):
        actual_msg = self.get_alert_msg_in_pop_window()
        assert_equal(expect_msg, actual_msg, "the alert msg is now shown as expect")

    def verify_alert_multiline_msg(self, expect_msg):
        actual_msg = self.get_alert_msg_in_pop_window()
        assert_equal(expect_msg, actual_msg, "the alert msg is now shown as expect")

    def verify_alert_multiline_unicode_msg(self, expect_msg):
        actual_msg = self.get_alert_msg_in_pop_window()
        assert_equal(expect_msg, actual_msg, "the alert msg is now shown as expect")

    def click_for_confirm(self):
        self.click(self.confirm_button)

    def alert_window_accept(self):
        self.driver.switch_to.alert.accept()

    def alert_window_dismiss(self):
        self.driver.switch_to.alert.dismiss()

    def alert_window_send_keys(self, content):
        self.driver.switch_to.alert.send_keys(content)

    def get_confirm_result_msg(self):
        ele = self.find_element(self.confirm_test_input)
        return ele.get_attribute("value")

    def verify_confirm_msg_when_accept(self):
        actual_msg = self.get_confirm_result_msg()
        assert_equal("oked", actual_msg, "msg not correct")

    def verify_confirm_msg_when_dismiss(self):
        actual_msg = self.get_confirm_result_msg()
        assert_equal("canceled", actual_msg, "msg not correct")

    def click_for_prompt(self):
        self.click(self.prompt_button)

    def get_prompt_result_msg(self):
        ele = self.find_element(self.confirm_test_input)
        return ele.get_attribute("value")

    def verify_prompt_msg_after_input(self, content):
        actual_msg = self.get_prompt_result_msg()
        assert_equal(content, actual_msg, "msg not correct")

    def select_all_test(self):
        sel_s1_id = Select(self.find_element((By.ID, "s1Id")))
        sel_s1_id.select_by_index(0)

        sel_s2_id = Select(self.find_element((By.ID, "s2Id")))
        sel_s2_id.select_by_value("o1")

        sel_s3_id = Select(self.find_element((By.ID, "s3Id")))
        sel_s3_id.select_by_visible_text("With spaces")

        sel_s4_id = Select(self.find_element((By.ID, "s4Id")))
        sel_s4_id.select_by_value("o3val")

        sel_s1 = Select(self.find_element((By.ID, "s1")))
        sel_s1.select_by_visible_text("Cell Phone")

        test_input = Select(self.find_element((By.ID, "testInputEvent")))
        test_input.select_by_index(3)

    def single_click(self):
        actions = ActionChains(self.driver)
        element = self.find_element(self.click_me_button)
        actions.click(element).perform()

    def double_click(self):
        actions = ActionChains(self.driver)
        element = self.find_element(self.dlb_click_button)
        actions.double_click(element).perform()

    def right_click(self):
        actions = ActionChains(self.driver)
        element = self.find_element(self.right_click_button)
        actions.context_click(element).perform()

    def select_clear_button(self):
        self.click(self.clear_button)

    def get_window_msg(self):
        return self.find_element((By.NAME, "t2")).get_attribute("value")

    def verify_msg_in_click_window(self, click=False, double_click=False, right_click=False):
        actual_msg = self.get_window_msg()
        if click:
            assert_equal(actual_msg, "[CLICK]", "no CLICK")
        elif double_click:
            assert_equal(actual_msg, "[DOUBLE_CLICK]", "no DOUBLE_CLICK")
        elif right_click:
            assert_equal(actual_msg, "[RIGHT_CLICK]", "no RIGHT_CLICK")
        else:
            NameError("invalid name")

    def verify_button_disabled(self):
        ele = self.find_element(self.disabled_button)
        is_disabled = ele.get_attribute("disabled")
        assert_true(is_disabled, "the button is not disabled as expect")

    def move_mouse_to_button1(self):
        actions = ActionChains(self.driver)
        ele = self.find_element(self.write_on_hover)
        actions.move_to_element(ele).perform()

    def move_mouse_to_button2(self):
        actions = ActionChains(self.driver)
        ele = self.find_element(self.blank_on_hover)
        actions.move_to_element(ele).perform()

    def move_mouse_to_zone_area(self):
        actions = ActionChains(self.driver)
        ele = self.find_element(self.mouse_zone)
        actions.move_to_element(ele).perform()

    def verify_text_in_first_output(self, context):
        ele = self.find_element(self.mouse_text1)
        actual_output = ele.get_attribute("value")
        assert_equal(context, actual_output, "fail")

    def verify_text_in_second_output(self, context):
        ele = self.find_element(self.mouse_text2)
        actual_output = ele.get_attribute("value")
        assert_equal(context, actual_output, "fail")

    def drag_item_to_all_windows(self):
        actions = ActionChains(self.driver)
        ele_start = self.find_element(self.the_dragger)
        time.sleep(0.5)
        ele_end1 = self.find_element(self.item1)
        time.sleep(0.5)
        ele_end2 = self.find_element(self.item2)
        time.sleep(0.5)
        ele_end3 = self.find_element(self.item3)
        time.sleep(0.5)
        ele_end4 = self.find_element(self.item4)
        actions.drag_and_drop(ele_start, ele_end1).perform()
        actions.drag_and_drop(ele_start, ele_end2).perform()
        actions.drag_and_drop(ele_start, ele_end3).perform()
        actions.drag_and_drop(ele_start, ele_end4).perform()

    def verify_all_items_dropped(self):
        ele = self.find_elements((By.XPATH, '//div[text()="dropped"]'))
        actual_result = len(ele)
        assert_true(actual_result == 4, "validation fail.")

    def upload_file_by_send_keys(self):
        file_path = get_test_data_yaml_path
        self.send_keys(self.choose_file, file_path)

    def upload_file_by_keyboard(self):
        self.click(self.choose_file)
        file_path = get_test_data_credential_path
        keyboard.send_keys({file_path})
        keyboard.send_keys('{ENTER}')

    def click_submit_single_button(self, index=0):
        all_ele = self.find_element(self.submit_single_button)
        ele = all_ele[index]
        ele.click()
