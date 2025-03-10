from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from project_config import ProjectConfig
from utils.logs_util import logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator, retry=3, timeout=10):
        attempts = 1
        while attempts <= retry:
            try:
                logger.info(f"finding element: {locator}")
                ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
                return ele
            except (TimeoutException, NoSuchElementException) as e:
                logger.error(f"element {locator} not found, retrying {attempts} time(s)")
                attempts += 1

        raise TimeoutException(f"element {locator} not found after {retry} attempts.")

    def find_elements(self, locator, retry=3, timeout=10):
        attempt = 0
        while attempt < retry:
            try:
                logger.info(f"finding elements: {locator}")
                all_ele = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
                return all_ele
            except (TimeoutException, NoSuchElementException) as e:
                logger.error(f"elements {locator} not found with in {timeout} seconds with error: {e}")

        raise TimeoutException(f"elements {locator} not found after {retry} attempts.")


    def clear(self, locator):
        ele = self.find_element(locator)
        ele.clear()

    def send_keys(self, locator, content):
        ele = self.find_element(locator)
        ele.send_keys(content)

    def element_exist(self, locator, retry=3, timeout=10):
        logger.info(f"Check element {locator} exist")
        try:
            self.find_element(locator, retry, timeout)
            logger.info(f"element {locator} exist")
            return True #element found
        except NoSuchElementException:
            logger.info(f"element {locator} does not exist, NoSuchElementException")
            return False  #element not found
        except TimeoutException:
            logger.info(f"element {locator} does not exist, TimeoutException")
            return False

    def click(self, locator):
        logger.info(f"click element {locator}")
        ele = self.find_element(locator)
        ele.click()

    def move_to_mouse(self, locator):
        logger.info(f"move the mouse to element {locator}")
        ele = self.find_element(locator)
        ActionChains(self.driver).move_to_element(ele).perform()

    def switch_to_window(self, to_home_window=False):
        all_windows = self.driver.window_handles
        if to_home_window:
            logger.info("switch to the home window and close extra windows")
            for window in all_windows:
                self.driver.switch_to.window(window)
                if window != all_windows[0]:
                    self.driver.close()
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

