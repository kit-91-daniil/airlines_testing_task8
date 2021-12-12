from .base_page import BasePage
from .locators import MainPageCarHireTabLocators
from .locators import CalendarWidgetLocators
from project_utils.browser_helper import PageHelper
from support.logger_reporter import logger
from project_utils.text_formatter import months_numbers_and_names_dict


class MainPageCarHireTab(PageHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPageCarHireTab, self).__init__(*args, **kwargs)
        self.pick_up_location = None
        self.pick_up_year_month_day = None
        self.pick_up_time = None
        self.drop_off_year_month_day = None
        self.drop_off_time = None

    def perform_car_sharing(self, pick_up_location: str, pick_up_year_month_day: str, pick_up_time: str,
                            drop_off_year_month_day: str, drop_off_time: str):
        self.pick_up_location = pick_up_location
        self.pick_up_year_month_day = pick_up_year_month_day
        self.pick_up_time = pick_up_time
        self.drop_off_year_month_day = drop_off_year_month_day
        self.drop_off_time = drop_off_time
        self.choose_pick_up_location()
        self.choose_pick_up_date()
        self.choose_drop_off_date()
        self.choose_pick_up_time()
        self.choose_drop_off_time()
        self.click_submit_button()

    def choose_pick_up_location(self):
        pick_up_airport_name, origin_airport_code = [elem.strip() for elem in self.pick_up_location.rsplit("-")]
        pick_up_airport_locator = MainPageCarHireTabLocators.get_pick_up_location_ddm_locator(origin_airport_code)

        pick_up_airport_input = self.find_element_after_explicit_waiting(
            *MainPageCarHireTabLocators.PICKUP_LOCATION_INPUT)
        pick_up_airport_input.click()
        pick_up_airport_input.clear()
        pick_up_airport_input.send_keys(pick_up_airport_name)
        logger.info(f"pick_up_airport_locator: {pick_up_airport_locator}")
        self.click_element_to_be_active_after_explicit_waiting(*pick_up_airport_locator)

    def choose_pick_up_date(self):
        pick_up_year, pick_up_month, pick_up_day = self.pick_up_year_month_day.rsplit("-")
        pick_up_month_name = months_numbers_and_names_dict[int(pick_up_month)]  # Ex: Dec
        pick_up_date_month_locator = CalendarWidgetLocators.get_calendar_month_button_locator(pick_up_month_name)
        self.click_element_to_be_active_after_explicit_waiting(*pick_up_date_month_locator)
        pick_up_date_day_locator = CalendarWidgetLocators.get_calendar_day_button_locator(
            self.pick_up_year_month_day)
        self.click_element_to_be_active_after_explicit_waiting(*pick_up_date_day_locator)
        logger.info("pick up date was checked")

    def choose_drop_off_date(self):
        drop_off_year, drop_off_month, drop_off_day = self.drop_off_year_month_day.rsplit("-")
        drop_off_month_name = months_numbers_and_names_dict[int(drop_off_month)]  # Ex: Dec
        drop_off_date_month_locator = CalendarWidgetLocators.get_calendar_month_button_locator(drop_off_month_name)
        self.click_element_to_be_active_after_explicit_waiting(*drop_off_date_month_locator)
        drop_off_date_day_locator = CalendarWidgetLocators.get_calendar_day_button_locator(
            self.drop_off_year_month_day)
        self.click_element_to_be_active_after_explicit_waiting(*drop_off_date_day_locator)
        logger.info("drop off date was checked")

    def choose_pick_up_time(self):
        self.click_element_to_be_active_after_explicit_waiting(
            *MainPageCarHireTabLocators.PICK_UP_TIME_DDM_BUTTON)
        pick_up_time_ddm_element_locator = MainPageCarHireTabLocators.get_time_ddm_element_locator(self.pick_up_time)
        self.click_element_to_be_active_after_explicit_waiting(*pick_up_time_ddm_element_locator)

    def choose_drop_off_time(self):
        self.click_element_to_be_active_after_explicit_waiting(
            *MainPageCarHireTabLocators.DROP_OFF_TIME_DDM_BUTTON)
        drop_off_time_ddm_element_locator = MainPageCarHireTabLocators.get_time_ddm_element_locator(self.drop_off_time)
        self.click_element_to_be_active_after_explicit_waiting(*drop_off_time_ddm_element_locator)

    def click_submit_button(self):
        self.click_element_to_be_active_after_explicit_waiting(
            *MainPageCarHireTabLocators.LETS_GO_BUTTON)
