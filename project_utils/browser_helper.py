from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import Config
from features.pages.base_page import BasePage
from features.pages.locators import HeaderSectionLocators
from support.logger_reporter import logger


class PageHelper(BasePage):
    def click_element_to_be_visible_after_explicit_waiting(self, how, what, timeout=Config.timeout):
        WebDriverWait(self.browser, timeout=timeout).until(EC.visibility_of_element_located((how, what))).click()
        logger.info(f"Element {how} - {what} has been clicked")

    def click_element_to_be_active_after_explicit_waiting(self, how, what, timeout=Config.timeout):
        logger.info(f"Try to click element {how} - {what} ")
        WebDriverWait(self.browser, timeout=timeout).until(EC.element_to_be_clickable((how, what))).click()
        logger.info(f"Element {how} - {what} has been clicked")

    def find_element_after_explicit_waiting(self, how, what, timeout=Config.timeout):
        logger.info(f"Trying to find element {how} - {what}")
        return WebDriverWait(self.browser, timeout=timeout).until(EC.presence_of_element_located((how, what)))

    def get_text_of_the_element_after_explicit_waiting(self, how, what, timeout=Config.timeout) -> str:
        logger.info(f"Trying to find element {how} - {what} and get element.text")
        return WebDriverWait(self.browser, timeout=timeout).until(
            EC.presence_of_element_located((how, what))).text

    def is_element_disappeared_after_explicit_waiting(self, how, what, timeout=Config.timeout) -> bool:
        try:
            logger.info(f"Trying to find element {how} - {what}")
            WebDriverWait(self.browser, timeout=timeout, poll_frequency=1, ignored_exceptions=TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            logger.error("Element was not found. TimeoutException was caught")
            return False
        return True

    def is_element_present(self, how, what, timeout=Config.timeout) -> bool:
        try:
            logger.info(f"Trying to find element {how} - {what}")
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            logger.error("Element was not found. TimeoutException was caught")
            return False
        return True

    def is_element_present_and_has_a_text(self, how, what, timeout=Config.timeout):
        try:
            logger.info(f"Trying to find element {how} - {what}")
            element = WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            logger.error("Element was not found. TimeoutException was caught")
            return False
        result = element.text if hasattr(element, "text") else True
        return result

    def is_not_element_present(self, how, what, timeout=Config.timeout):
        try:
            logger.info(f"Trying to find element {how} - {what}")
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            logger.error("Element was not found. TimeoutException was caught")
            return True
        return False

    def click_accept_cookie_popup_button(self):
        if self.is_element_present(*HeaderSectionLocators.ACCEPT_COOKIE_POPUP_BUTTON, timeout=2):
            self.click_element_to_be_active_after_explicit_waiting(*HeaderSectionLocators.ACCEPT_COOKIE_POPUP_BUTTON)
