from .base_page import BasePage
from .locators import MainPageHotelsTabLocators, CalendarWidgetLocators

from project_utils.browser_helper import PageHelper
from support.logger_reporter import logger
from project_utils.text_formatter import months_numbers_and_names_dict


class MainPageHotelsTab(PageHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPageHotelsTab, self).__init__(*args, **kwargs)
        self.hotel_name = None
        self.check_in_year_month_day = None
        self.check_out_year_month_day = None

    def perform_room_search(self, hotel_name: str, check_in_year_month_day: str,
                            check_out_year_month_day: str):
        self.hotel_name = hotel_name
        self.check_in_year_month_day = check_in_year_month_day
        self.check_out_year_month_day = check_out_year_month_day
        self.choose_hotel()
        self.choose_check_in_date()
        self.choose_check_out_date()
        self.click_submit_button()

    def choose_hotel(self):
        hotel_ddm_element_locator = MainPageHotelsTabLocators.get_hotel_ddm_element_locator(self.hotel_name)
        hotel_name_input = self.find_element_after_explicit_waiting(
            *MainPageHotelsTabLocators.HOTEL_INPUT_FIELD)
        hotel_name_input.click()
        hotel_name_input.clear()
        hotel_name_input.send_keys(self.hotel_name)
        self.click_element_to_be_active_after_explicit_waiting(*hotel_ddm_element_locator)

    def choose_check_in_date(self):
        self.click_element_to_be_active_after_explicit_waiting(
            *MainPageHotelsTabLocators.CHOOSE_CHECK_IN_DATE_BUTTON_LOCATOR)
        check_in_year, check_in_month, check_in_day = self.check_in_year_month_day.rsplit("-")
        check_in_month_name = months_numbers_and_names_dict[int(check_in_month)]  # Ex: Dec
        check_in_date_month_locator = CalendarWidgetLocators.get_calendar_month_button_locator(check_in_month_name)
        self.click_element_to_be_active_after_explicit_waiting(*check_in_date_month_locator)
        check_in_date_day_locator = CalendarWidgetLocators.get_calendar_day_button_locator(
            self.check_in_year_month_day)
        self.click_element_to_be_active_after_explicit_waiting(*check_in_date_day_locator)
        logger.info("check in date was chosen")

    def choose_check_out_date(self):
        self.click_element_to_be_active_after_explicit_waiting(
            *MainPageHotelsTabLocators.CHOOSE_CHECK_OUT_DATE_BUTTON_LOCATOR)

        check_out_year, check_out_month, check_out_day = self.check_out_year_month_day.rsplit("-")
        check_out_month_name = months_numbers_and_names_dict[int(check_out_month)]  # Ex: Dec
        check_out_date_month_locator = CalendarWidgetLocators.get_calendar_month_button_locator(
            check_out_month_name)
        self.click_element_to_be_active_after_explicit_waiting(*check_out_date_month_locator)
        check_out_date_day_locator = CalendarWidgetLocators.get_calendar_day_button_locator(
            self.check_out_year_month_day)
        self.click_element_to_be_active_after_explicit_waiting(*check_out_date_day_locator)
        logger.info("check out date was chosen")

    def click_submit_button(self):
        self.click_element_to_be_active_after_explicit_waiting(
            *MainPageHotelsTabLocators.SEARCH_BUTTON_LOCATOR)
