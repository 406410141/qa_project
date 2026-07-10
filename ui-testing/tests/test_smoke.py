import pytest
import allure
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


@allure.epic("SauceDemo Project")
@allure.feature("Home Page")
@allure.tag("smoke")
@allure.severity(allure.severity_level.CRITICAL)
@allure.story(" homepage loading")
@pytest.mark.flaky(reruns=2, reruns_delay=1)
def test_tc001(driver):
    # test_smoke.py
    login_page = LoginPage(driver)
    driver.get(login_page.URL)

    assert login_page.find_element(login_page.LOGO).is_displayed(), "Login Logo Not Display"

    assert login_page.find_element(login_page.USER_ACCOUNT).is_displayed(), "Account Input Field Not Displayed"
    assert login_page.find_element(login_page.PASSWORD_INPUT).is_displayed(), "Password Input Field Not Displayed"
    assert login_page.find_element(login_page.LOGIN_BUTTON).is_displayed(), "Login BTN Not Displayed"
