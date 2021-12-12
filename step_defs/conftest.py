import allure
import os
import pytest

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from features.pages.car_hire_page import CarHirePage
from features.pages.cheap_flights_page import CheapFlightsPage
from features.pages.flight_page import FlightPage
from features.pages.hotels_page import HotelsPage
from features.pages.main_page import MainPage
from features.pages.main_page_flight_tab import MainPageFlightTab
from features.pages.main_page_car_hire_tab import MainPageCarHireTab
from features.pages.main_page_hotels_tab import MainPageHotelsTab
from features.pages.transfer_page import TransferPage
from features.pages.urls import Urls


def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en", help="choose language: es or en or ru")
    parser.addoption("--browser_name", action="store", default="chrome", help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def main_page(browser):
    return MainPage(browser=browser, url=Urls.MAIN_PAGE_URL)


@pytest.fixture(scope="function")
def main_page_flights_tab(browser):
    return MainPageFlightTab(browser=browser, url=browser.current_url)


@pytest.fixture(scope="function")
def main_page_car_hire_tab(browser):
    return MainPageCarHireTab(browser=browser, url=browser.current_url)


@pytest.fixture(scope="function")
def main_page_hotels_tab(browser):
    return MainPageHotelsTab(browser=browser, url=browser.current_url)


@pytest.fixture(scope="function")
def flight_page(browser):
    return FlightPage(browser=browser, url=browser.current_url)


@pytest.fixture(scope="function")
def car_hire_page(browser):
    return CarHirePage(browser=browser, url=Urls.MAIN_PAGE_URL)


@pytest.fixture(scope="function")
def hotels_page(browser):
    hotels_page = HotelsPage(browser=browser, url=browser.current_url)
    hotels_page.click_accept_cookie_popup_button()
    return hotels_page


@pytest.fixture(scope="function")
def cheap_flights_page(browser):
    return CheapFlightsPage(browser=browser, url=browser.current_url)


@pytest.fixture(scope="function")
def transfer_page(browser):
    return TransferPage(browser=browser, url=browser.current_url)


@pytest.fixture(scope="package")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    browser = None
    if browser_name == "chrome":
        options = Options()
        options.add_argument("--window-size=1600,1250")
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(executable_path=GeckoDriverManager().install(), firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser name should be chrome or firefox")
    yield browser
    browser.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        mode = 'a' if os.path.exists('failures') else 'w'
        try:
            with open('failures', mode) as f:
                if 'browser' in item.fixturenames:
                    web_driver = item.funcargs['browser']
                else:
                    print('Fail to take screen-shot')
                    return
            allure.attach(
                web_driver.get_screenshot_as_png(),
                name='screenshot',
                attachment_type=allure.attachment_type.PNG
            )
        except Exception as e:
            print('Fail to take screen-shot: {}'.format(e))
