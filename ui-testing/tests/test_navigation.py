import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory import Inventory
import time

#test_navigation.py
expected_menu_items = ['All Items', 'About', 'Logout', 'Reset App State']

@allure.epic("SauceDemo Project")
@allure.feature("Navigation Bar")
@allure.story("Check Nav Bar Items")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression")
def test_tc005(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.URL)

    login_page.login(login_page.ACCEPTED_USERNAMES, login_page.ACCEPTED_PASSWORD)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed or URL mismatch"

    inventory_page = Inventory(driver)
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
@allure.tag("regression")
def test_tc006(driver):
    driver.get(LoginPage.URL)
    login_page = LoginPage(driver)
    login_page.login(login_page.ACCEPTED_USERNAMES, login_page.ACCEPTED_PASSWORD)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed or URL mismatch"
    inventory_page = Inventory(driver)
    inventory_page.click(inventory_page.SIDE)
    inventory_page.click(inventory_page.ABOUT_LINK)
    assert driver.current_url == "https://saucelabs.com/", "About link did not navigate to the correct URL"



@allure.epic("SauceDemo Project")
@allure.feature("Navigation Bar")
@allure.story("Logout")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke","regression")
def test_tc007(driver):
    driver.get(LoginPage.URL)
    login_page = LoginPage(driver)
    login_page.login(login_page.ACCEPTED_USERNAMES, login_page.ACCEPTED_PASSWORD)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed or URL mismatch"
    inventory_page = Inventory(driver)
    inventory_page.click(inventory_page.SIDE)
    inventory_page.click(inventory_page.LOGOUT_LINK)
    assert driver.current_url == "https://www.saucedemo.com/", "Logout link did not navigate to the correct URL"