from .base_page import BasePage
from .locators import HotelsPageLocators
from project_utils.browser_helper import PageHelper
from project_utils.text_formatter import months_numbers_and_names_dict


class HotelsPage(PageHelper, BasePage):
    def verify_destination_and_booking_period_presence(self, hotel, check_in_year_month_day,
                                                       check_out_year_month_day):
        self.should_be_destination(hotel)
        self.should_be_correct_booking_period(check_in_year_month_day,
                                              check_out_year_month_day)

    def verify_rooms_page_is_displayed_with_logo(self):
        self.is_element_present(*HotelsPageLocators.HOTELS_LOGO)

    def should_be_destination(self, destination):
        actual_text = self.get_text_of_the_element_after_explicit_waiting(
            *HotelsPageLocators.SEARCH_RESULT_DESTINATION)
        assert destination in actual_text

    def should_be_correct_booking_period(self, check_in_year_month_day: str,
                                         check_out_year_month_day: str):
        in_year, in_month_number, in_day = check_in_year_month_day.split("-")
        out_year, out_month_number, out_day = check_out_year_month_day.split("-")
        in_month_name = months_numbers_and_names_dict[int(in_month_number)]  # Ex: Dec
        out_month_name = months_numbers_and_names_dict[int(out_month_number)]  # Ex: Dec
        expected_booking_period_text = f"{in_day} {in_month_name} {in_year} - " \
                                       f"{out_day} {out_month_name} {out_year}"
        actual_booking_period_text = self.get_text_of_the_element_after_explicit_waiting(
            *HotelsPageLocators.SEARCH_RESULT_DATES)[:-1]
        assert actual_booking_period_text == expected_booking_period_text
