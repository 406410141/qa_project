import pytest
import allure
from pages.login_page import LoginPage
from test_data import SAUCEDEMO_DATA
# test_login.py

EXPECTED_USERS = SAUCEDEMO_DATA["credentials"]["displayedUsers"]
EXPECTED_PASSWORD = SAUCEDEMO_DATA["credentials"]["password"]


@allure.epic("SauceDemo Project")
@allure.feature("Login Info")
@allure.story("Login Info")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@allure.tag("regression")
def test_tc002_login_page_shows_accepted_users(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.URL)
    locator = login_page.All_USERNAMES
    print(f"\n[Debug] Locator: {locator}")
    users_text = login_page.find_element(locator).text
    print(f"[Debug] Block Text:\n{users_text}")
    print("-" * 30)
    assert login_page.find_element(login_page.All_USERNAMES).is_displayed(), "Account No Show"
    assert login_page.find_element(login_page.All_PASSWORD).is_displayed(), "Password No show"

    users_text = login_page.find_element(login_page.All_USERNAMES).text
    pwd_text = login_page.find_element(login_page.All_PASSWORD).text
    for user in EXPECTED_USERS:
        assert user in users_text, f" No Expected : {user}"
        print(user)
    assert EXPECTED_PASSWORD in pwd_text, f"No Expected -> : {pwd_text}"


@allure.epic("SauceDemo Project")
@allure.feature("Login Info")
@allure.story("Close ERROR MSG")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@allure.tag("regression")
def test_tc003_login_success(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.URL)

    login_page.login(login_page.ACCEPTED_USERNAMES, login_page.ACCEPTED_PASSWORD)
    login_page.wait_url("https://www.saucedemo.com/inventory.html")


@allure.epic("SauceDemo Project")
@allure.feature("Login Info")
@allure.story("Close ERROR MSG")
@allure.severity(allure.severity_level.MINOR)
@pytest.mark.regression
@allure.tag("regression")
def test_tc004_close_login_error_message(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.URL)
    login_page.click(login_page.LOGIN_BUTTON)

    assert login_page.find_element(login_page.ERROR_CONTAINER).is_displayed(), "Error message not displayed"
    login_page.click(login_page.CLOSE_REMIND)
    login_page.wait_invisible(login_page.ERROR_CONTAINER)


@allure.epic("SauceDemo Project")
@allure.feature("Login Info")
@allure.story("Wrong Password")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.negative
@allure.tag("regression")
def test_tc016_login_wrong_password(driver):
    login = LoginPage(driver)
    login.login(login.ACCEPTED_USERNAMES, "wrong_password")
    error_message = login.get_error_message()
    assert error_message == "Epic sadface: Username and password do not match any user in this service", f"Unexpected error message: {error_message}"
    assert driver.current_url == login.URL, "Should stay on login page"


@allure.epic("SauceDemo Project")
@allure.feature("Login Info")
@allure.story("Empty Account")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.negative
@allure.tag("regression")
def test_tc017_login_empty_username(driver):
    login = LoginPage(driver)
    login.login("", login.ACCEPTED_PASSWORD)
    error_message = login.get_error_message()
    assert error_message == "Epic sadface: Username is required", f"Unexpected error message: {error_message}"
    assert driver.current_url == login.URL, "Should stay on login page"


@allure.epic("SauceDemo Project")
@allure.feature("Login Info")
@allure.story("Empty Password")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.regression
@pytest.mark.negative
@allure.tag("regression")
def test_tc018_login_empty_password(driver):
    login = LoginPage(driver)
    login.login(login.ACCEPTED_USERNAMES, "")
    error_message = login.get_error_message()
    assert error_message == "Epic sadface: Password is required", f"Unexpected error message: {error_message}"
    assert driver.current_url == login.URL, "Should stay on login page"
