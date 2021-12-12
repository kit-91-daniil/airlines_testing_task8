from .base_page import BasePage
from project_utils.browser_helper import PageHelper
from .locators import CarHirePageLocators


class CarHirePage(PageHelper, BasePage):
    def should_be_correct_header_text(self, expected_header_text):
        actual_header_text = self.get_text_of_the_element_after_explicit_waiting(
            *CarHirePageLocators.HEADER_TITLE)
        assert actual_header_text == expected_header_text
