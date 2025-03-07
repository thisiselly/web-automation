from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from project_config import ProjectConfig
from utils.logs_util import logger


class BasePage:

    # 初始化
    def __init__(self, driver):
        # self.driver = xx
        self.driver = driver
        # self.driver.get(ProjectConfig.home_url)

    def find_element(self, locator, timeout=10):
        logger.info(f"finding element {locator}")
        ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
        return ele

    # def find_element(self, locator, timeout=10, expect_found=True):
    #     if expect_found:
    #         ele = WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    #         return ele
    #     else:
    #         try:
    #             WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    #         except NoSuchElementException:
    #             return None

    def clear(self, locator):
        ele = self.find_element(locator)
        ele.clear()

    def send_keys(self, locator, content):
        ele = self.find_element(locator)
        ele.send_keys(content)

    def element_exist(self, locator, timeout=10):
        logger.info(f"Check element {locator} exist")
        try:
            ele = self.find_element(locator, timeout)
            logger.info("element exist")
            return True #element found
        except NoSuchElementException:
            logger.info("element exist, NoSuchElementException")
            return False  #element not found
        except TimeoutException:
            logger.info("element exist, TimeoutException")
            return False

    def click(self, locator):
        logger.info(f"click element {locator}")
        ele = self.find_element(locator)
        ele.click()

    def move_to_mouse(self, locator):
        logger.info(f"move the mouse to element {locator}")
        ele = self.find_element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def switch_to_window(self, to_parental_window=False):
        all_windows = self.driver.window_handles
        if to_parental_window:
            logger.info("switch to the parent window")
            self.driver.switch_to.window(all_windows[0])
        else:
            logger.info("switch to the current open window")
            current_window = self.driver.current_window_handle
            for window in all_windows:
                if window != current_window:
                    self.driver.switch_to.window(window)

    def get_text(self, locator):
        ele = self.find_element(locator)
        if ele.text is not None:
            logger.info(f"get text from text: {ele.text}")
            return ele.text
        elif ele.accessible_name is not None:
            logger.info(f"get text from accessible_name: {ele.accessible_name}")
            return ele.accessible_name
        else:
            logger.info(f"text and accessible_name is none")
            return None

    def close(self):
        logger.info("close the current window")
        self.driver.close()

