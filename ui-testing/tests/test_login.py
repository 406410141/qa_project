import pytest
import allure
from pages.login_page import LoginPage
# test_login.py

EXPECTED_USERS = [
    "standard_user",
    "locked_out_user",
    "problem_user",
    "performance_glitch_user",
    "error_user",
    "visual_user"
]


@allure.epic("SauceDemo Project")
@allure.feature("Login Info")
@allure.story("Login Info")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("regression")
def test_tc002(driver):
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
    assert "secret_sauce" in pwd_text, f"No Expected -> : {pwd_text}"


@allure.epic("SauceDemo Project")
@allure.feature("Login Info")
@allure.story("Close ERROR MSG")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("regression")
def test_tc003(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.URL)

    login_page.login(login_page.ACCEPTED_USERNAMES, login_page.ACCEPTED_PASSWORD)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed or URL mismatch"


@allure.epic("SauceDemo Project")
@allure.feature("Login Info")
@allure.story("Close ERROR MSG")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("regression")
def test_tc004(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.URL)
    login_page.click(login_page.LOGIN_BUTTON)

    assert login_page.find_element(login_page.ERROR_REMIND).is_displayed(), "Error message not displayed"
    login_page.click(login_page.CLOSE_REMIND)
    try:
        visible = login_page.find_element(login_page.ERROR_REMIND).is_displayed()
    except Exception:
        visible = False
    assert visible == False, "Error message still displayed after closing"
