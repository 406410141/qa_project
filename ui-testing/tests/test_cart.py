import pytest
import allure
from pages.inventory import Inventory
from pages.cart_page import Cart


@allure.epic("SauceDemo Project")
@allure.feature("Cart")
@allure.story("Click Cart Btn")
@allure.tag("smoke", "regression")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("""
測試目標：點擊購物車圖標，驗證跳轉到購物車頁面
預期結果：成功跳轉到購物車頁面，且頁面標題顯示 'Your Cart'
""")
def test_tc008(logged_in_driver):
    inventory_page = Inventory(logged_in_driver)
    inventory_page.click(inventory_page.SHOP_CART)

    assert logged_in_driver.current_url == "https://www.saucedemo.com/cart.html", "Cart Link Redirect Wrong URL"

    cart_page = Cart(logged_in_driver)
    assert cart_page.get_text(cart_page.CART_TITLE) == "Your Cart", "Wrong Title"


@allure.epic("SauceDemo Project")
@allure.feature("Cart")
@allure.story("Click CTU BTN")
@allure.tag("regression")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("""
測試目標：點擊繼續購物按鈕，驗證返回商品列表頁面
預期結果：成功返回商品列表頁面 (inventory.html)
""")
def test_tc009(logged_in_driver):
    inventory_page = Inventory(logged_in_driver)
    inventory_page.click(inventory_page.SHOP_CART)

    assert logged_in_driver.current_url == "https://www.saucedemo.com/cart.html", "Cart Link Redirect Wrong URL"

    cart_page = Cart(logged_in_driver)
    cart_page.click(cart_page.CONTINUE_SHOP)

    assert logged_in_driver.current_url == "https://www.saucedemo.com/inventory.html", "CTU button did't return to inventory page."
