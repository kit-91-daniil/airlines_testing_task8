from .base_page import BasePage
from .locators import CheapFlightsPageLocators
from project_utils.browser_helper import PageHelper


class CheapFlightsPage(PageHelper, BasePage):
    def __init__(self, *args, **kwargs):
        super(CheapFlightsPage, self).__init__(*args, **kwargs)
        self.origin_airport = None
        self.destination_airport = None
        self.budget = None

    def perform_cheap_flight_search(self, origin_airport, destination_airport, budget):
        self.origin_airport = origin_airport
        self.destination_airport = destination_airport
        self.budget = budget
        self.choose_origin_airport()
        self.choose_destination_airport()
        self.choose_budget()
        self.click_submit_button()

    def choose_origin_airport(self):
        origin_airport_name, origin_airport_code = [elem.strip() for elem in self.origin_airport.rsplit("-")]
        origin_airport_locator = CheapFlightsPageLocators.get_ddm_origin_airport_link_locator(
            origin_airport_code)
        origin_airport_input = self.find_element_after_explicit_waiting(
            *CheapFlightsPageLocators.DEPARTURE_AIRPORT_INPUT)
        origin_airport_input.click()
        origin_airport_input.clear()
        origin_airport_input.send_keys(origin_airport_name)
        self.click_element_to_be_active_after_explicit_waiting(*origin_airport_locator)

    def choose_destination_airport(self):
        destination_airport_name, destination_airport_code = [
            elem.strip() for elem in self.destination_airport.rsplit("-")]
        destination_airport_input = self.find_element_after_explicit_waiting(
            *CheapFlightsPageLocators.DESTINATION_AIRPORT_INPUT)
        destination_airport_input.clear()
        destination_airport_input.send_keys(destination_airport_name)

    def choose_budget(self):
        self.click_element_to_be_active_after_explicit_waiting(*CheapFlightsPageLocators.BUDGET_DDM_BUTTON)
        custom_budget_input_field = self.find_element_after_explicit_waiting(
            *CheapFlightsPageLocators.CUSTOM_BUDGET_INPUT_FIELD)
        custom_budget_input_field.send_keys(self.budget)
        self.click_element_to_be_active_after_explicit_waiting(*CheapFlightsPageLocators.CONFIRM_CUSTOM_BUDGET)

    def click_submit_button(self):
        self.click_element_to_be_active_after_explicit_waiting(*CheapFlightsPageLocators.LETS_GO_BUTTON)

    def verify_destination_point_and_flight_price_are_correct(self, destination_airport, budget):
        self.verify_destination_point_is_correct(destination_airport)
        self.verify_flight_price_is_correct(budget)

    def verify_destination_point_is_correct(self, expected_destination_airport):
        expected_destination_airport_name, expected_destination_airport_code = [
            elem.strip() for elem in expected_destination_airport.rsplit("-")]
        actual_destination_airport = self.get_text_of_the_element_after_explicit_waiting(
            *CheapFlightsPageLocators.SEARCH_RESULT_DESTINATION_AIRPORT)
        assert actual_destination_airport == expected_destination_airport_name

    def verify_flight_price_is_correct(self, budget):
        actual_price_units = self.get_text_of_the_element_after_explicit_waiting(
            *CheapFlightsPageLocators.SEARCH_RESULT_PRICE_UNITS)
        assert int(actual_price_units) < int(budget)
