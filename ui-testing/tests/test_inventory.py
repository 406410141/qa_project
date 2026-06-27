import allure
from pages.login_page import LoginPage
from pages.inventory import Inventory


EXPECTED_AZ_LIST = [
    "Sauce Labs Backpack",
    "Sauce Labs Bike Light",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Onesie",
    "Test.allTheThings() T-Shirt (Red)"
]

EXPECTED_ZA_LIST = [
    "Test.allTheThings() T-Shirt (Red)",
    "Sauce Labs Onesie",
    "Sauce Labs Fleece Jacket",
    "Sauce Labs Bolt T-Shirt",
    "Sauce Labs Bike Light",
    "Sauce Labs Backpack"
]

EXPECTED_PRICE_LOHI = [7.99, 9.99, 15.99, 15.99, 29.99, 49.99]

EXPECTED_PRICE_HILO = [49.99, 29.99, 15.99, 15.99, 9.99, 7.99]


@allure.epic("SauceDemo Project")
@allure.feature("Item Sort")
@allure.story("A->Z")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression")
def test_tc011(driver):
    driver.get(LoginPage.URL)
    login_page = LoginPage(driver)
    login_page.login(login_page.ACCEPTED_USERNAMES, login_page.ACCEPTED_PASSWORD)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed or URL mismatch"
    inventory = Inventory(driver)

    # Check A->Z
    item_names = inventory.get_all_items_name()
    sorted_names = sorted(item_names)
    assert item_names == sorted_names, f"wrong sort: {item_names} Not A->Z "

    print(f"item list: {item_names}")


@allure.epic("SauceDemo Project")
@allure.feature("Item Sort")
@allure.story("A->Z")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression")
def test_tc012(driver):
    driver.get(LoginPage.URL)
    login_page = LoginPage(driver)
    login_page.login(login_page.ACCEPTED_USERNAMES, login_page.ACCEPTED_PASSWORD)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed or URL mismatch"
    inventory = Inventory(driver)

    inventory.click_sort_za()
    # Check Z->A
    item_names = inventory.get_all_items_name()
    sorted_names = sorted(item_names, reverse=True)
    assert item_names == sorted_names, f"wrong sort: {item_names} Not Z->A "

    print(f"item list: {item_names}")


@allure.epic("SauceDemo Project")
@allure.feature("Item Sort")
@allure.story("Lo->Hi")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression")
def test_tc013(driver):
    driver.get(LoginPage.URL)
    login_page = LoginPage(driver)
    login_page.login(login_page.ACCEPTED_USERNAMES, login_page.ACCEPTED_PASSWORD)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed or URL mismatch"
    inventory = Inventory(driver)
    inventory.click_sort_lohi()
    item_prices = inventory.get_all_items_price()

    assert item_prices == EXPECTED_PRICE_LOHI, f"wrong sort: {item_prices} Not Price low to high"
    print(f"item list: {item_prices}")


"""
### TC-14:   Price high to low
**測試目標**：消費流程 加入商品 -> 進入購物車 -> 結帳
| **Step 1** | 開啟 Chrome 瀏覽器並輸入 `https://www.saucedemo.com/` 
| **Step 2** | 登入 | 成功登入
| **Step 3** | 更改排序商品 Price high to low  |  Price high to low 排列正確
---
---
"""
@allure.epic("SauceDemo Project")
@allure.feature("Item Sort")
@allure.story("Hi->Lo")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression")
def test_tc014(driver):
    driver.get(LoginPage.URL)
    login_page = LoginPage(driver)
    login_page.login(login_page.ACCEPTED_USERNAMES, login_page.ACCEPTED_PASSWORD)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "Login failed or URL mismatch"
    inventory = Inventory(driver)
    inventory.click_sort_hilo()

    item_prices = inventory.get_all_items_price()

    assert item_prices == EXPECTED_PRICE_HILO, f"wrong sort: {item_prices} Not Price high to low"
    print(f"item list: {item_prices}")
