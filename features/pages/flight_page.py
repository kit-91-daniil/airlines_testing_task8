from .base_page import BasePage
from project_utils.browser_helper import PageHelper
from .locators import FlightsPageLocators


class FlightPage(PageHelper, BasePage):
    def verify_from_to_route_existence(self, origin_airport, destination_airport):
        origin_airport_name, origin_airport_code = [elem.strip() for elem in origin_airport.rsplit("-")]
        destination_airport_name, destination_airport_code = [elem.strip() for elem in destination_airport.rsplit("-")]
        flight_route_text = self.find_element_after_explicit_waiting(*FlightsPageLocators.DEPARTURE_ROUTE).text
        assert all(sub in flight_route_text for sub in (origin_airport_name, "to", destination_airport_name))
