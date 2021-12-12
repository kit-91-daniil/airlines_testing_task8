from .base_page import BasePage
from .locators import TransferPageLocators
from project_utils.browser_helper import PageHelper


class TransferPage(PageHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(TransferPage, self).__init__(*args, **kwargs)

        self.pick_up_country = None
        self.pick_up_point = None
        self.drop_off_point = None
        self.departure_date = None
        self.departure_time = None
        self.year = None
        self.month = None
        self.day = None

    def perform_transfer_search(self, pick_up_country, pick_up_point, drop_off_point,
                                departure_date, departure_time):
        self.pick_up_country = pick_up_country
        self.pick_up_point = pick_up_point
        self.drop_off_point = drop_off_point
        self.departure_date = departure_date
        self.departure_time = departure_time
        self.choose_pick_up_country()
        self.choose_pick_up_point()
        self.choose_drop_off_point()
        self.choose_pick_up_date()
        self.choose_pick_up_time()
        self.click_submit_button()

    def choose_pick_up_country(self):
        country_input_field = self.find_element_after_explicit_waiting(*TransferPageLocators.COUNTRY_INPUT_FIELD)
        country_ddm_element_locator = TransferPageLocators.get_country_ddm_element_locator(self.pick_up_country)
        country_input_field.clear()
        country_input_field.send_keys(self.pick_up_country)
        self.click_element_to_be_active_after_explicit_waiting(*country_ddm_element_locator)

    def choose_pick_up_point(self):
        airport_name, airport_code = [elem.strip() for elem in self.pick_up_point.rsplit("-")]
        departure_airport_ddm_element_locator = TransferPageLocators.get_departure_airport_ddm_element_locator(
            airport_code)
        departure_input_field = self.find_element_after_explicit_waiting(*TransferPageLocators.DEPARTURE_INPUT_FIELD)
        departure_input_field.clear()
        departure_input_field.send_keys(airport_name)
        self.click_element_to_be_active_after_explicit_waiting(*departure_airport_ddm_element_locator)

    def choose_drop_off_point(self):
        destination_point_locator = TransferPageLocators.get_destination_point_ddm_element_locator(
            self.drop_off_point)
        drop_off_point_input_field = self.find_element_after_explicit_waiting(
            *TransferPageLocators.DESTINATION_INPUT_FIELD)
        drop_off_point_input_field.clear()
        drop_off_point_input_field.send_keys(self.drop_off_point)
        self.click_element_to_be_active_after_explicit_waiting(*destination_point_locator)

    def choose_pick_up_date(self):
        self.year, self.month, self.day = self.departure_date.split("-")
        self.click_element_to_be_active_after_explicit_waiting(*TransferPageLocators.CALENDAR_BUTTON)
        departure_date_day_locator = TransferPageLocators.get_departure_date_day_locator(self.day)
        self.click_element_to_be_active_after_explicit_waiting(*departure_date_day_locator)

    def choose_pick_up_time(self):
        departure_time_locator = TransferPageLocators.get_departure_time_locator(self.departure_time)
        self.click_element_to_be_active_after_explicit_waiting(*departure_time_locator)

    def click_submit_button(self):
        self.click_element_to_be_active_after_explicit_waiting(*TransferPageLocators.SEARCH_BUTTON)

    def verify_transfer_options(self, departure_date, departure_time):
        year, month, day = departure_date.split("-")
        actual_transfer_date_time = self.get_text_of_the_element_after_explicit_waiting(
            *TransferPageLocators.TRANSFER_DATE_TIME)
        assert all(sub in actual_transfer_date_time for sub in (year, day, departure_time))

    def verify_price_presence(self):
        assert self.is_element_present(*TransferPageLocators.PRICE)
