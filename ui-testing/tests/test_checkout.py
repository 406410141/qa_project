import pytest
import allure
from pages.login_page import LoginPage
from pages.inventory import Inventory
from pages.cart_page import Cart
from pages.checkout_step_one_page import CheckoutStepOne
from pages.checkout_step_two_page import CheckoutStepTwo
from pages.checkout_complete import CheckoutComplete


@allure.epic("SauceDemo Project")
@allure.feature("Checkout")
@allure.story("Single Item Checkout")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "regression")
def test_tc010(driver):
    driver.get(LoginPage.URL)
    login_page = LoginPage(driver)
    login_page.login(login_page.ACCEPTED_USERNAMES, login_page.ACCEPTED_PASSWORD)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed or URL mismatch"
    inventory = Inventory(driver)
    inventory.click(inventory.ADD_ITEM_BACKPACK)
    assert driver.find_element(*inventory.SHOP_CART).text == '1', "Cart count is not 1 after adding item"
    inventory.click(inventory.SHOP_CART)
    assert driver.current_url == "https://www.saucedemo.com/cart.html", "Cart link did not navigate to the correct URL"

    cart_page = Cart(driver)

    items_in_cart = cart_page.get_all_items_detail()

    assert len(items_in_cart) == 1, f"Expected 1 Item，Actually {len(items_in_cart)} items"

    target = items_in_cart[0]
    assert target["name"] == "Sauce Labs Backpack", f"Name Error: {target['name']}"
    assert target["price"] == 29.99, f"Amount Error: {target['price']}"
    assert target["qty"] == 1, f"Quantity Error: {target['qty']}"

    print("\nCart Structure Valid Success！")
    print(f"Item Info: {target}")

    cart_page.click(cart_page.CHECKOUT)
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-one.html", "Checkout link did not navigate to the correct URL"
    CS1 = CheckoutStepOne(driver)
    assert CS1.get_text(CS1.CHECKOUT_TITLE) == "Checkout: Your Information", "Checkout page title not found"

    CS1.fill_checkout_info("Tony", "Xie", "300")
    CS1.click_continue()
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "Did not navigate to checkout overview page"

    CS2 = CheckoutStepTwo(driver)
    assert CS2.get_text(CS2.CHECKOUT_TITLE) == "Checkout: Overview", "Checkout overview page title not found"
    checkout_overview_items = CS2.get_checkout_items_detail()
    assert len(
        checkout_overview_items) == 1, f" only 1 item expected in checkout overview, but found {len(checkout_overview_items)}"
    overview_item = checkout_overview_items[0]
    assert overview_item[
        "name"] == "Sauce Labs Backpack", f"Overview item name mismatch: expected 'Sauce Labs Backpack', got '{overview_item['name']}'"
    assert overview_item["price"] == 29.99, f"Overview item price mismatch: expected 29.99, got {overview_item['price']}"
    assert overview_item["qty"] == 1, f"Overview item quantity mismatch: expected 1, got {overview_item['qty']}"

    actual_payment = CS2.get_payment_info()
    assert "SauceCard #31337" in actual_payment, f"Payment info mismatch, got: {actual_payment}"
    amounts = CS2.get_financial_summary()
    assert amounts["subtotal"] == 29.99, f"Subtotal mismatch: {amounts['subtotal']}"
    assert amounts["tax"] == 2.40, f"Tax mismatch: {amounts['tax']}"
    assert amounts["total"] == 32.39, f"Total mismatch: {amounts['total']}"

    CS2.click_finish()

    assert driver.current_url == "https://www.saucedemo.com/checkout-complete.html", "Did not navigate to checkout complete page"
    CC = CheckoutComplete(driver)
    assert CC.get_text(CC.COMPLETE_HEADER) == "Thank you for your order!", "Checkout complete title not found"
    assert CC.get_text(
        CC.COMPLETE_TEXT) == "Your order has been dispatched, and will arrive just as fast as the pony can get there!", "Complete text mismatch"
    CC.click(CC.BACK_HOME_BTN)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Back home button did not navigate to inventory page"


@allure.epic("SauceDemo Project")
@allure.feature("Checkout")
@allure.story("Multiple Item Checkout")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("smoke", "regression")
def test_tc015(driver):
    driver.get(LoginPage.URL)
    login_page = LoginPage(driver)
    login_page.login(login_page.ACCEPTED_USERNAMES, login_page.ACCEPTED_PASSWORD)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed or URL mismatch"
    inventory = Inventory(driver)
    inventory.click(inventory.ADD_ITEM_BACKPACK)
    inventory.click(inventory.ADD_ITEM_ONESIE)
    inventory.click(inventory.ADD_ITEM_RED_TSHIRT)
    assert driver.find_element(*inventory.CART_ITEM).text == '3', "Cart count is not 3 after adding items"
    inventory.click(inventory.SHOP_CART)
    assert driver.current_url == "https://www.saucedemo.com/cart.html", "Cart link did not navigate to the correct URL"

    cart_page = Cart(driver)

    items_in_cart = cart_page.get_all_items_detail()
    assert len(items_in_cart) == 3, f"Expected 3 items, but found  {len(items_in_cart)} "

    expected_items = [
        {"name": "Sauce Labs Backpack", "price": 29.99, "qty": 1},
        {"name": "Sauce Labs Onesie", "price": 7.99, "qty": 1},
        {"name": "Test.allTheThings() T-Shirt (Red)", "price": 15.99, "qty": 1}
    ]

    for expected in expected_items:
        match = next((item for item in items_in_cart if item["name"] == expected["name"]), None)
        assert match is not None, f"Can Not Find Item: {expected['name']}"
        assert match["price"] == expected["price"], f"{expected['name']} Amount Error: {match['price']}"
        assert match["qty"] == expected["qty"], f"{expected['name']} Quantity Error: {match['qty']}"

    cart_page.click(cart_page.CHECKOUT)
    CS1 = CheckoutStepOne(driver)
    CS1.fill_checkout_info("Tony", "Xie", "300")
    CS1.click_continue()
    assert driver.current_url == "https://www.saucedemo.com/checkout-step-two.html", "Did not navigate to checkout overview page"
    CS2 = CheckoutStepTwo(driver)
    overview_items = CS2.get_checkout_items_detail()
    assert len(overview_items) == 3, f"Incorrect Quantity In Checkout List: Expected 3, Actual {len(overview_items)}"
       
    # (29.99 + 7.99 + 15.99 = 53.97)
    actual_payment = CS2.get_payment_info()
    assert "SauceCard #31337" in actual_payment
    amounts = CS2.get_financial_summary()

    # Item total: $53.97, Tax: $4.32, Total: $58.29
    assert amounts["subtotal"] == 53.97, f"小計錯誤: {amounts['subtotal']}"
    assert amounts["tax"] == 4.32, f"稅金錯誤: {amounts['tax']}"
    assert amounts["total"] == 58.29, f"總額錯誤: {amounts['total']}"

    CS2.click_finish()

    CC = CheckoutComplete(driver)
    assert "THANK YOU FOR YOUR ORDER" in CC.get_text(CC.COMPLETE_HEADER).upper()
    CC.click(CC.BACK_HOME_BTN)
    assert "inventory.html" in driver.current_url
