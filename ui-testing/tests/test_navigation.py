import pytest
import allure
from pages.inventory import Inventory
from test_data import SAUCEDEMO_DATA


# test_navigation.py
expected_menu_items = SAUCEDEMO_DATA["navigation"]["menuItems"]


@allure.epic("SauceDemo Project")
@allure.feature("Navigation Bar")
@allure.story("Check Nav Bar Items")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@allure.tag("regression")
def test_tc005_sidebar_menu_items(logged_in_driver):
    inventory_page = Inventory(logged_in_driver)
    inventory_page.click(inventory_page.SIDE)
    menu_items = [
        inventory_page.get_text(inventory_page.ALL_ITEMS_LINK),
        inventory_page.get_text(inventory_page.ABOUT_LINK),
        inventory_page.get_text(inventory_page.LOGOUT_LINK),
        inventory_page.get_text(inventory_page.RESET_LINK)
    ]
    for item in menu_items:
        assert item in expected_menu_items, f"Menu item '{item}' not found in expected items"
    inventory_page.click(inventory_page.CLOSE_SIDEBAR)
    inventory_page.wait_invisible(inventory_page.SIDE_BAR)


@allure.epic("SauceDemo Project")
@allure.feature("Navigation Bar")
@allure.story("About")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@allure.tag("regression")
def test_tc006_sidebar_about_link(logged_in_driver):
    inventory_page = Inventory(logged_in_driver)
    inventory_page.click(inventory_page.SIDE)
    inventory_page.click(inventory_page.ABOUT_LINK)
    assert logged_in_driver.current_url == "https://saucelabs.com/", "About link did not navigate to the correct URL"


@allure.epic("SauceDemo Project")
@allure.feature("Navigation Bar")
@allure.story("Logout")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
@allure.tag("smoke", "regression")
def test_tc007_sidebar_logout(logged_in_driver):
    inventory_page = Inventory(logged_in_driver)
    inventory_page.click(inventory_page.SIDE)
    inventory_page.click(inventory_page.LOGOUT_LINK)
    assert logged_in_driver.current_url == "https://www.saucedemo.com/", "Logout link did not navigate to the correct URL"
