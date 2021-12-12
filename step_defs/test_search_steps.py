from features.pages.flight_page import FlightPage
from pytest_bdd import given, when, then, scenarios, parsers
from features.pages.urls import Urls
from features.pages.locators import MainPageLocators
from features.pages.main_page import MainPage
from features.pages.main_page_flight_tab import MainPageFlightTab
from features.pages.main_page_car_hire_tab import MainPageCarHireTab
from features.pages.main_page_hotels_tab import MainPageHotelsTab
from features.pages.car_hire_page import CarHirePage
from features.pages.hotels_page import HotelsPage
from features.pages.cheap_flights_page import CheapFlightsPage
from features.pages.transfer_page import TransferPage
from support.logger_reporter import logger
import time


scenarios("../features/search.feature")


@given('I am on the main page')
def main_page_opened(main_page: MainPage):
    main_page.open()
    main_page.click_accept_cookie_popup_button()


@when(parsers.cfparse("I open the '{tab}' tab"))
def open_the_tab_on_main_page(main_page: MainPage, tab):
    tab_locator = MainPageLocators.get_tab_button_locator(tab)
    logger.info(tab_locator)
    main_page.click_element_to_be_active_after_explicit_waiting(*tab_locator)


# ********** FLIGHTS SEARCH STEPS


@when(parsers.cfparse(
    "I perform search : from '{origin_airport}' to '{destination_airport}' in next dates: "
    "departure '{depart_year_month_day}', return '{return_year_month_day}'"
    " and click the '{button}' button")
)
def perform_flights_search(main_page_flights_tab: MainPageFlightTab, origin_airport: str, destination_airport: str,
                           depart_year_month_day: str, return_year_month_day: str, button: str):
    main_page_flights_tab.perform_flight_search(
        origin_airport, destination_airport, depart_year_month_day, return_year_month_day)


@then(u'flight page should be displayed with title containing Flights')
def verify_displaying_flights_page(browser):
    time.sleep(5)
    assert Urls.FLIGHTS_PAGE_URL_PART in browser.current_url


@then(parsers.cfparse("I should see flights from '{origin_airport}' to '{destination_airport}' and arrival price"))
def verify_from_to_route_existence(browser, origin_airport, destination_airport):
    flight_page = FlightPage(browser=browser, url=browser.current_url)
    flight_page.verify_from_to_route_existence(origin_airport, destination_airport)


# ********** CAR HIRE SEARCH STEPS


@when(parsers.cfparse("I perform search : from '{pick_up_location}' in next period: "
                      "from '{pick_up_year_month_day}' '{pick_up_time}' "
                      "to '{drop_off_year_month_day}' '{drop_off_time}'"
                      " and click the '{button}' button"))
def perform_car_sharing(main_page_car_hire_tab: MainPageCarHireTab, pick_up_location: str,
                        pick_up_year_month_day: str, pick_up_time: str,
                        drop_off_year_month_day: str, drop_off_time: str, button: str):
    logger.info(f"pick_up_location: {pick_up_location}")
    logger.info(f"pick_up_year_month_day: {pick_up_year_month_day}")
    logger.info(f"pick_up_time: {pick_up_time}")
    logger.info(f"drop_off_year_month_day: {drop_off_year_month_day}")
    logger.info(f"drop_off_time: {drop_off_time}")

    main_page_car_hire_tab.perform_car_sharing(pick_up_location, pick_up_year_month_day, pick_up_time,
                                               drop_off_year_month_day, drop_off_time)


@then(parsers.cfparse("Car Hire page should be displayed with header containing '{header_text}'"))
def verify_header_presence_on_page(car_hire_page: CarHirePage, header_text):
    car_hire_page.should_be_correct_header_text(header_text)


# ********** ROOM SEARCH STEPS


@when(parsers.cfparse("I perform search: '{hotel}' in next period: "
                      "from '{check_in_year_month_day}' to '{check_out_year_month_day}' "
                      "and click the '{button}' button"))
def perform_room_search(main_page_hotels_tab: MainPageHotelsTab, hotel: str,
                        check_in_year_month_day: str, check_out_year_month_day: str):
    main_page_hotels_tab.perform_room_search(hotel, check_in_year_month_day, check_out_year_month_day)


@then(parsers.cfparse("Rooms page should be displayed with Rooms logo"))
def verify_rooms_page_is_displayed_with_logo(hotels_page: HotelsPage):
    hotels_page.verify_rooms_page_is_displayed_with_logo()


@then(parsers.cfparse("I should see '{hotel}' and period: "
                      "from '{check_in_year_month_day}' to '{check_out_year_month_day}'"))
def verify_destination_and_booking_period_presence(hotels_page: HotelsPage, hotel: str,
                                                   check_in_year_month_day: str, check_out_year_month_day: str):
    hotels_page.verify_destination_and_booking_period_presence(
        hotel, check_in_year_month_day, check_out_year_month_day)


# ********** CHEAP FLIGHTS
@when(parsers.cfparse("I open Plan menu"))
def open_plan_menu(main_page: MainPage):
    main_page.open_the_plan_menu()


@when(parsers.cfparse("click Fare Finder link"))
def open_the_cheap_flights_link(main_page: MainPage):
    main_page.open_the_fare_finder_link()


@when(parsers.cfparse("I Perform search: from '{origin_airport}' to '{destination_airport}' "
                      "with budget under '{budget}' and click Let's Go button"))
def cheap_flight_search(cheap_flights_page: CheapFlightsPage, origin_airport,
                        destination_airport, budget):
    cheap_flights_page.perform_cheap_flight_search(origin_airport, destination_airport,
                                                   budget)


@then(parsers.cfparse("I should see '{destination_airport}' and flight price less than '{budget}'"))
def verify_destination_airport_and_flight_price_are_correct(cheap_flights_page: CheapFlightsPage,
                                                            destination_airport, budget):
    cheap_flights_page.verify_destination_point_and_flight_price_are_correct(destination_airport, budget)

# ********** TRANSFER SEARCH


@when(parsers.cfparse("click 'Search Bus and Train link'"))
def open_the_cheap_flights_link(main_page: MainPage):
    main_page.open_the_transfer_search_link()


@when(parsers.cfparse("I Perform search: Pick Country '{pick_up_country}', "
                      "start from '{pick_up_point}' going to '{drop_off_point}' "
                      "on '{departure_date}' '{departure_time}' "
                      "and click Search button"))
def transfer_search(transfer_page: TransferPage, pick_up_country,  pick_up_point,
                    drop_off_point, departure_date, departure_time):
    transfer_page.perform_transfer_search(pick_up_country, pick_up_point, drop_off_point,
                                          departure_date, departure_time)


@then(parsers.cfparse("I should see transfer options: date '{departure_date}', "
                      "time '{departure_time}' and price"))
def verify_transfer_options(transfer_page: TransferPage, departure_date, departure_time):
    transfer_page.verify_transfer_options(departure_date, departure_time)
