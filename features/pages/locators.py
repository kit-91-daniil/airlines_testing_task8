from selenium.webdriver.common.by import By
import sys
import os.path

# For import from a parent directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))


class BasePageLocators:
    pass


class CalendarWidgetLocators:
    CHOOSE_MONTH_BUTTON_LOCATOR_PATTERN = "//div[text()=' {month} ']"  # Jan
    CHOOSE_DAY_OF_MONTH_LOCATOR_PATTERN = "[data-id='{date}']"  # date yyyy-mm-dd

    @classmethod
    def get_calendar_month_button_locator(cls, month: str) -> tuple:
        return By.XPATH, cls.CHOOSE_MONTH_BUTTON_LOCATOR_PATTERN.format(month=month.title())

    @classmethod
    def get_calendar_day_button_locator(cls, date: str) -> tuple:
        return By.CSS_SELECTOR, cls.CHOOSE_DAY_OF_MONTH_LOCATOR_PATTERN.format(date=date)


class HeaderSectionLocators(BasePageLocators):
    HEADER_LOGO = (By.CSS_SELECTOR, "[title=Ryanair]")
    ACCEPT_COOKIE_POPUP_BUTTON = (By.CSS_SELECTOR, "button.cookie-popup-with-overlay__button")


class MainPageLocators(HeaderSectionLocators):

    TAB_BUTTON_LOCATOR_PATTERN = "[data-ref='search-widget-tabs__{tab_name}']"

    @classmethod
    def get_tab_button_locator(cls, tab: str) -> tuple:
        if tab == "hotels":
            tab = "rooms"
        return By.CSS_SELECTOR, cls.TAB_BUTTON_LOCATOR_PATTERN.format(
            tab_name=tab.replace(" ", "-"))

    PLAN_DDM_BUTTON = (By.CSS_SELECTOR, "[data-ref='header-menu-item__toggle-button'][aria-label='Plan']")
    FARE_FINDER_BUTTON = (By.CSS_SELECTOR, "[href$='/cheap-flights']")
    TRANSFER_LINK = (By.CSS_SELECTOR, "[aria-label='Search Bus and Train']")


class CheapFlightsPageLocators:
    DEPARTURE_AIRPORT_INPUT = (By.CSS_SELECTOR, "[label='From:'][departure-input] input[role='textbox']")
    DESTINATION_AIRPORT_INPUT = (By.CSS_SELECTOR, "[label='To:'][destination-input] input[role='textbox']")
    BUDGET_DDM_BUTTON = (By.CSS_SELECTOR, "farefinder-budget-input")

    SELECTOR_PATTERN_OF_ORIGIN_AIRPORT_DDM_ELEMENT = "//div[div[contains(text(), '{airport_code}')]]"

    @classmethod
    def get_ddm_origin_airport_link_locator(cls, airport_code):
        return By.XPATH, cls.SELECTOR_PATTERN_OF_ORIGIN_AIRPORT_DDM_ELEMENT.format(airport_code=airport_code)

    CUSTOM_BUDGET_INPUT_FIELD = (By.CSS_SELECTOR, "[name = 'custom-budget']")
    CONFIRM_CUSTOM_BUDGET = (By.CSS_SELECTOR, "button.core-btn-primary")
    LETS_GO_BUTTON = (By.CSS_SELECTOR, "[type='submit']")
    #  SEARCH RESULT
    SEARCH_RESULT_DESTINATION_AIRPORT = (By.CSS_SELECTOR, "span.airport")
    SEARCH_RESULT_PRICE_UNITS = (By.CSS_SELECTOR, ".price-units")
    SEARCH_RESULT_MONTH = (By.CSS_SELECTOR, ".ff-text-month")


class MainPageFlightTabLocators(HeaderSectionLocators):
    ORIGIN_AIRPORT_INPUT = (By.CSS_SELECTOR, "#input-button__departure")
    DEST_AIRPORT_INPUT = (By.CSS_SELECTOR, "#input-button__destination")

    CHOOSE_AIRPORT_FROM_DDM_PATTERN = "[data-id='{airport_code}']"  # ABC

    @classmethod
    def get_pick_an_airport_locator(cls, airport_code):
        return By.CSS_SELECTOR, cls.CHOOSE_AIRPORT_FROM_DDM_PATTERN.format(
            airport_code=airport_code.upper())

    CHOOSE_DEPART_DATE_BUTTON = (By.CSS_SELECTOR, "[uniqueid='dates-from']")
    CHOOSE_RETURN_DATE_BUTTON = (By.CSS_SELECTOR, "[uniqueid='dates-to']")

    SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-ref='flight-search-widget__cta']")


class MainPageCarHireTabLocators(HeaderSectionLocators):

    PICKUP_LOCATION_INPUT_DDM_BUTTON = (By.CSS_SELECTOR, "hp-input-button[uniqueid='pick-up-location']")
    PICKUP_LOCATION_INPUT = (By.CSS_SELECTOR, "hp-input-button[uniqueid='pick-up-location']>div>input")
    CAR_HIRE_TAB_PICK_UP_LOC_DDM_LOCATOR_PATTERN = "//button/span[text()='({code})']"

    @classmethod
    def get_pick_up_location_ddm_locator(cls, airport_code) -> tuple:
        return By.XPATH, cls.CAR_HIRE_TAB_PICK_UP_LOC_DDM_LOCATOR_PATTERN.format(code=airport_code)

    CHOOSE_PICKUP_DATE_BUTTON = (By.CSS_SELECTOR, "hp-input-button[uniqueid='pick-up-date']")
    PICK_UP_TIME_DDM_BUTTON = (By.CSS_SELECTOR, "hp-input-button[uniqueid='pick-up-time']")

    CHOOSE_DROP_OFF_DATE_BUTTON = (By.CSS_SELECTOR, "hp-input-button[uniqueid='drop-off-date']")
    DROP_OFF_TIME_DDM_BUTTON = (By.CSS_SELECTOR, "hp-input-button[uniqueid='drop-off-time']")

    TIME_DDM_ELEMENT_PATTERN = "//ry-tooltip[@role='tooltip']//*[text()='{time}']"

    @classmethod
    def get_time_ddm_element_locator(cls, time_="00:00") -> tuple:
        return By.XPATH, cls.TIME_DDM_ELEMENT_PATTERN.format(time=time_)

    LETS_GO_BUTTON = (By.CSS_SELECTOR, "[data-ref='car-hire-widget__cta']")


class MainPageHotelsTabLocators(HeaderSectionLocators):

    HOTELS_SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-ref='rooms-search-widget__cta']")
    HOTEL_INPUT_FIELD = (By.CSS_SELECTOR, "#input-button__locations-or-properties")

    INPUT_HOTEL_DDM_ELEMENT_XPATH_PATTERN = "//hp-room-search-property-item[./div[text()='{hotel_name}']]"

    @classmethod
    def get_hotel_ddm_element_locator(cls, hotel_name: str) -> tuple:
        return By.XPATH, cls.INPUT_HOTEL_DDM_ELEMENT_XPATH_PATTERN.format(
            hotel_name=hotel_name)

    CHOOSE_CHECK_IN_DATE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[uniqueid='check-in']")
    CHOOSE_CHECK_OUT_DATE_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[uniqueid='check-out']")

    SEARCH_BUTTON_LOCATOR = (By.CSS_SELECTOR, "[data-ref='rooms-search-widget__cta']")


class FlightsPageLocators(HeaderSectionLocators):
    DEPARTURE_ROUTE = (By.CSS_SELECTOR, "h3[class*='ng-tns-c']")


class CarHirePageLocators(HeaderSectionLocators):
    HEADER_TITLE = (By.CSS_SELECTOR, "h3.header__title")
    PICK_UP_LOCATION = (By.CSS_SELECTOR, "[data-testid='pick-up-location']")
    DROP_OFF_LOCATION = (By.CSS_SELECTOR, "[data-testid='drop-off-location']")
    PICK_UP_DATE = (By.CSS_SELECTOR, "[data-testid='pick-up-date']")
    DROP_OFF_DATE = (By.CSS_SELECTOR, "[data-testid='drop-off-date']")


class HotelsPageLocators(HeaderSectionLocators):
    SEARCH_RESULT_DESTINATION = (By.CSS_SELECTOR, "[data-ref='search-summary__destination']")
    SEARCH_RESULT_DATES = (By.CSS_SELECTOR, "[data-ref='search-summary__dates']")
    HOTELS_LOGO = (By.CSS_SELECTOR, "a[title='Rooms logo']")


class TransferPageLocators:
    COUNTRY_INPUT_FIELD = (By.CSS_SELECTOR, "#country-div>input[type='text']")
    COUNTRY_DDM_ELEMENT_LOCATOR_PATTERN = "li[data-name*='{country}']"

    @classmethod
    def get_country_ddm_element_locator(cls, country: str) -> tuple:
        return By.CSS_SELECTOR, cls.COUNTRY_DDM_ELEMENT_LOCATOR_PATTERN.format(country=country)

    DEPARTURE_INPUT_FIELD = (By.CSS_SELECTOR, "#source-div>input[type='text']")
    DEPARTURE_AIRPORT_DDM_ELEMENT_LOCATOR_PATTERN = "li[data-code='{airport_code}']"

    @classmethod
    def get_departure_airport_ddm_element_locator(cls, airport_code: str) -> tuple:
        return By.CSS_SELECTOR, cls.DEPARTURE_AIRPORT_DDM_ELEMENT_LOCATOR_PATTERN.format(airport_code=airport_code)

    DESTINATION_INPUT_FIELD = (By.CSS_SELECTOR, "#target-div>input[type='text']")
    DESTINATION_POINT_DDM_ELEMENT_LOCATOR_PATTERN = "li[data-name*='{point}']"

    @classmethod
    def get_destination_point_ddm_element_locator(cls, point: str) -> tuple:
        return By.CSS_SELECTOR, cls.DESTINATION_POINT_DDM_ELEMENT_LOCATOR_PATTERN.format(point=point)

    CALENDAR_BUTTON = (By.CSS_SELECTOR, "input.dateFrom")
    DEPARTURE_DATE_DAY_LOCATOR_PATTERN = "//*[@data-month=11]//*[text()='{day_number}']"

    @classmethod
    def get_departure_date_day_locator(cls, day: str) -> tuple:
        return By.XPATH, cls.DEPARTURE_DATE_DAY_LOCATOR_PATTERN.format(day_number=day)

    DEPARTURE_TIME_LOCATOR_PATTERN = "#DepartureDate > [value='{time}']"

    @classmethod
    def get_departure_time_locator(cls, time: str) -> tuple:
        return By.CSS_SELECTOR, cls.DEPARTURE_TIME_LOCATOR_PATTERN.format(time=time)

    SEARCH_BUTTON = (By.CSS_SELECTOR, "input[value='Search']")

    TRANSFER_DATE_TIME = (By.CSS_SELECTOR, ".bigNBold")
    PRICE = (By.CSS_SELECTOR, "p.selectedPrice")


