from .base_page import BasePage
from .locators import MainPageFlightTabLocators
from .locators import CalendarWidgetLocators
from project_utils.browser_helper import PageHelper
from support.logger_reporter import logger
from project_utils.text_formatter import months_numbers_and_names_dict


class MainPageFlightTab(PageHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPageFlightTab, self).__init__(*args, **kwargs)
        self.origin_airport = None
        self.destination_airport = None
        self.depart_year_month_day = None
        self.return_year_month_day = None

    def perform_flight_search(self, origin_airport: str, destination_airport: str,
                              depart_year_month_day: str, return_year_month_day: str):
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.depart_year_month_day = depart_year_month_day
        self.return_year_month_day = return_year_month_day
        self.choose_origin_airport()
        self.choose_destination_airport()
        self.choose_departure_date()
        self.choose_return_date()
        self.click_submit_button()

    def choose_origin_airport(self):
        origin_airport_name, origin_airport_code = [elem.strip() for elem in self.origin_airport.rsplit("-")]
        origin_airport_locator = MainPageFlightTabLocators.get_pick_an_airport_locator(origin_airport_code)

        origin_airport_input = self.find_element_after_explicit_waiting(
            *MainPageFlightTabLocators.ORIGIN_AIRPORT_INPUT)
        origin_airport_input.click()
        origin_airport_input.clear()
        origin_airport_input.send_keys(origin_airport_name)
        self.click_element_to_be_active_after_explicit_waiting(*origin_airport_locator)

    def choose_destination_airport(self):
        destination_airport_name, destination_airport_code = [
            elem.strip() for elem in self.destination_airport.rsplit("-")]
        destination_airport_locator = MainPageFlightTabLocators.get_pick_an_airport_locator(destination_airport_code)

        destination_airport_input = self.find_element_after_explicit_waiting(
            *MainPageFlightTabLocators.DEST_AIRPORT_INPUT)
        destination_airport_input.send_keys(destination_airport_name)
        self.click_element_to_be_active_after_explicit_waiting(*destination_airport_locator)

    def choose_departure_date(self):
        depart_year, depart_month, depart_day = self.depart_year_month_day.rsplit("-")  # 2021, 01 , 14
        depart_month_name = months_numbers_and_names_dict[int(depart_month)]  # Ex: Dec
        self.click_element_to_be_active_after_explicit_waiting(
            *MainPageFlightTabLocators.CHOOSE_DEPART_DATE_BUTTON)
        depart_date_month_locator = CalendarWidgetLocators.get_calendar_month_button_locator(
            depart_month_name)
        self.click_element_to_be_active_after_explicit_waiting(*depart_date_month_locator)
        depart_date_day_locator = CalendarWidgetLocators.get_calendar_day_button_locator(
            self.depart_year_month_day)
        self.click_element_to_be_active_after_explicit_waiting(*depart_date_day_locator)
        logger.info("depart date was checked")

    def choose_return_date(self):
        return_year, return_month, return_day = self.return_year_month_day.rsplit("-")  # 2021
        return_month_name = months_numbers_and_names_dict[int(return_month)]  # Ex: Dec
        self.click_element_to_be_active_after_explicit_waiting(
            *MainPageFlightTabLocators.CHOOSE_RETURN_DATE_BUTTON)
        return_date_month_locator = CalendarWidgetLocators.get_calendar_month_button_locator(
            return_month_name)
        self.click_element_to_be_active_after_explicit_waiting(*return_date_month_locator)
        return_date_day_locator = CalendarWidgetLocators.get_calendar_day_button_locator(
            self.return_year_month_day)
        self.click_element_to_be_active_after_explicit_waiting(*return_date_day_locator)
        logger.info("return date was checked")

    def click_submit_button(self):
        self.click_element_to_be_active_after_explicit_waiting(
            *MainPageFlightTabLocators.SEARCH_BUTTON_LOCATOR
        )
