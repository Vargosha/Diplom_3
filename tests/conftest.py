import pytest
from selenium import webdriver
from helpers.urls import LOGIN_PAGE_URL, HOME_PAGE_URL, ORDER_FEED_PAGE_URL
from helpers.data import LOGIN_DATA
from pages.home_page import HomePageMethods
from pages.login_page import LoginPageMethods
from pages.order_feed_page import OrderFeedPageMethods


class WebDriverFactory:
    @staticmethod
    def get_webdriver(browser_name):
        if browser_name == "firefox":
            return webdriver.Firefox()
        elif browser_name == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Выбор браузера:'chrome' или 'firefox'"
    )

@pytest.fixture
def driver(request):
    browser_name = request.config.getoption("--browser")
    driver = WebDriverFactory.get_webdriver(browser_name)
    driver.maximize_window()

    yield driver

    driver.quit()

@pytest.fixture
def unregistered_user(driver):
    homepage = HomePageMethods(driver)

    driver.get(HOME_PAGE_URL)
    homepage.wait_for_load_home_page()

    return homepage

@pytest.fixture
def registered_user(driver):
    login_page = LoginPageMethods(driver)
    homepage = HomePageMethods(driver)
    email = LOGIN_DATA["email"]
    password = LOGIN_DATA["password"]

    driver.get(LOGIN_PAGE_URL)
    login_page.set_login_data_and_submit(email, password)

    homepage.wait_for_load_home_page()

    return homepage

@pytest.fixture
def get_orders_quantity(driver):
    homepage = HomePageMethods(driver)
    order_page = OrderFeedPageMethods(driver)

    driver.get(ORDER_FEED_PAGE_URL)
    order_page.wait_for_load_order_feed_page()

    total_orders = order_page.get_quantity_total_completed_orders()
    today_orders = order_page.get_quantity_today_completed_orders()

    driver.get(HOME_PAGE_URL)
    homepage.wait_for_load_home_page()

    return total_orders, today_orders

@pytest.fixture
def create_order(driver, registered_user):
    homepage = registered_user

    bun = homepage.get_random_bun()
    ingredient = homepage.get_random_ingredient()[0]
    homepage.drag_and_drop_ingredient_to_cart(bun)
    homepage.drag_and_drop_ingredient_to_cart(ingredient)
    homepage.click_submit_order_button()

    homepage.wait_for_popup_order_confirm_window()
    homepage.wait_for_load_order_number()

    order_number = homepage.get_order_number()
    homepage.click_cross_button_order_confirm()

    homepage.wait_for_load_home_page()
    homepage.wait_for_overlay_close()

    return order_number
