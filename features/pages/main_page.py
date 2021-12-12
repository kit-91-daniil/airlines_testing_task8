from .base_page import BasePage
from .locators import MainPageLocators, HeaderSectionLocators
from project_utils.browser_helper import PageHelper


class MainPage(PageHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

    def open_the_plan_menu(self):
        self.click_element_to_be_active_after_explicit_waiting(*MainPageLocators.PLAN_DDM_BUTTON)

    def open_the_fare_finder_link(self):
        self.click_element_to_be_active_after_explicit_waiting(*MainPageLocators.FARE_FINDER_BUTTON)

    def open_the_transfer_search_link(self):
        self.click_element_to_be_active_after_explicit_waiting(*MainPageLocators.TRANSFER_LINK)
