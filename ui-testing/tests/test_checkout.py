import pytest
import allure
from pages.inventory import Inventory
from pages.cart_page import Cart
from pages.checkout_step_one_page import CheckoutStepOne
from pages.checkout_step_two_page import CheckoutStepTwo
from pages.checkout_complete import CheckoutComplete
from test_data import SAUCEDEMO_DATA, item_details

CHECKOUT = SAUCEDEMO_DATA["checkout"]
CUSTOMER = CHECKOUT["customer"]


@allure.epic("SauceDemo Project")
@allure.feature("Checkout")
@allure.story("Single Item Checkout")
@allure.severity(allure.severity_level.CRITICAL)
@pytest.mark.smoke
@pytest.mark.regression
@allure.tag("smoke", "regression")
def test_tc010_single_item_checkout(logged_in_driver):
    inventory = Inventory(logged_in_driver)
    inventory.click(inventory.ADD_ITEM_BACKPACK)
    assert inventory.get_text(inventory.SHOP_CART) == '1', "Cart count is not 1 after adding item"
    inventory.click(inventory.SHOP_CART)
    inventory.wait_url("https://www.saucedemo.com/cart.html")

    cart_page = Cart(logged_in_driver)

    items_in_cart = cart_page.get_all_items_detail()

    assert len(items_in_cart) == 1, f"Expected 1 Item，Actually {len(items_in_cart)} items"

    expected_item = item_details(CHECKOUT["singleItemIds"])[0]
    target = items_in_cart[0]
    assert target["name"] == expected_item["name"], f"Name Error: {target['name']}"
    assert target["price"] == expected_item["price"], f"Amount Error: {target['price']}"
    assert target["qty"] == expected_item["qty"], f"Quantity Error: {target['qty']}"

    print("\nCart Structure Valid Success！")
    print(f"Item Info: {target}")

    cart_page.click(cart_page.CHECKOUT)
    cart_page.wait_url("https://www.saucedemo.com/checkout-step-one.html")
    CS1 = CheckoutStepOne(logged_in_driver)
    CS1.wait_text(CS1.CHECKOUT_TITLE, "Checkout: Your Information")
    assert CS1.get_text(CS1.CHECKOUT_TITLE) == "Checkout: Your Information", "Checkout page title not found"

    CS1.fill_checkout_info(CUSTOMER["firstName"], CUSTOMER["lastName"], CUSTOMER["postalCode"])
    CS1.click_continue()
    CS1.wait_url("https://www.saucedemo.com/checkout-step-two.html")

    CS2 = CheckoutStepTwo(logged_in_driver)
    CS2.wait_text(CS2.CHECKOUT_TITLE, "Checkout: Overview")
    assert CS2.get_text(CS2.CHECKOUT_TITLE) == "Checkout: Overview", "Checkout overview page title not found"
    checkout_overview_items = CS2.get_checkout_items_detail()
    assert len(
        checkout_overview_items) == 1, f" only 1 item expected in checkout overview, but found {len(checkout_overview_items)}"
    overview_item = checkout_overview_items[0]
    assert overview_item["name"] == expected_item["name"], f"Overview item name mismatch: got '{overview_item['name']}'"
    assert overview_item["price"] == expected_item["price"], f"Overview item price mismatch: got {overview_item['price']}"
    assert overview_item["qty"] == expected_item["qty"], f"Overview item quantity mismatch: got {overview_item['qty']}"

    actual_payment = CS2.get_payment_info()
    assert CHECKOUT["paymentInfo"] in actual_payment, f"Payment info mismatch, got: {actual_payment}"
    amounts = CS2.get_financial_summary()
    summary = CHECKOUT["singleItemSummary"]
    assert amounts["subtotal"] == summary["itemTotal"], f"Subtotal mismatch: {amounts['subtotal']}"
    assert amounts["tax"] == summary["tax"], f"Tax mismatch: {amounts['tax']}"
    assert amounts["total"] == summary["total"], f"Total mismatch: {amounts['total']}"

    CS2.click_finish()

    CS2.wait_url("https://www.saucedemo.com/checkout-complete.html")
    CC = CheckoutComplete(logged_in_driver)
    assert CC.get_text(CC.COMPLETE_HEADER) == "Thank you for your order!", "Checkout complete title not found"
    assert CC.get_text(
        CC.COMPLETE_TEXT) == "Your order has been dispatched, and will arrive just as fast as the pony can get there!", "Complete text mismatch"
    CC.click(CC.BACK_HOME_BTN)
    CC.wait_url("https://www.saucedemo.com/inventory.html")


@allure.epic("SauceDemo Project")
@allure.feature("Checkout")
@allure.story("Multiple Item Checkout")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.smoke
@pytest.mark.regression
@allure.tag("smoke", "regression")
def test_tc015_multiple_item_checkout(logged_in_driver):
    inventory = Inventory(logged_in_driver)
    inventory.click(inventory.ADD_ITEM_BACKPACK)
    inventory.click(inventory.ADD_ITEM_ONESIE)
    inventory.click(inventory.ADD_ITEM_RED_TSHIRT)
    assert inventory.get_text(inventory.CART_ITEM) == '3', "Cart count is not 3 after adding items"
    inventory.click(inventory.SHOP_CART)
    inventory.wait_url("https://www.saucedemo.com/cart.html")

    cart_page = Cart(logged_in_driver)

    items_in_cart = cart_page.get_all_items_detail()
    assert len(items_in_cart) == 3, f"Expected 3 items, but found  {len(items_in_cart)} "

    expected_items = item_details(CHECKOUT["multipleItemIds"])

    for expected in expected_items:
        match = next((item for item in items_in_cart if item["name"] == expected["name"]), None)
        assert match is not None, f"Can Not Find Item: {expected['name']}"
        assert match["price"] == expected["price"], f"{expected['name']} Amount Error: {match['price']}"
        assert match["qty"] == expected["qty"], f"{expected['name']} Quantity Error: {match['qty']}"

    cart_page.click(cart_page.CHECKOUT)
    CS1 = CheckoutStepOne(logged_in_driver)
    CS1.fill_checkout_info(CUSTOMER["firstName"], CUSTOMER["lastName"], CUSTOMER["postalCode"])
    CS1.click_continue()
    CS1.wait_url("https://www.saucedemo.com/checkout-step-two.html")
    CS2 = CheckoutStepTwo(logged_in_driver)
    overview_items = CS2.get_checkout_items_detail()
    assert len(overview_items) == 3, f"Incorrect Quantity In Checkout List: Expected 3, Actual {len(overview_items)}"

    actual_payment = CS2.get_payment_info()
    assert CHECKOUT["paymentInfo"] in actual_payment
    amounts = CS2.get_financial_summary()
    summary = CHECKOUT["multipleItemSummary"]
    assert amounts["subtotal"] == summary["itemTotal"], f"小計錯誤: {amounts['subtotal']}"
    assert amounts["tax"] == summary["tax"], f"稅金錯誤: {amounts['tax']}"
    assert amounts["total"] == summary["total"], f"總額錯誤: {amounts['total']}"

    CS2.click_finish()

    CC = CheckoutComplete(logged_in_driver)
    assert "THANK YOU FOR YOUR ORDER" in CC.get_text(CC.COMPLETE_HEADER).upper()
    CC.click(CC.BACK_HOME_BTN)
    CC.wait_url("https://www.saucedemo.com/inventory.html")
