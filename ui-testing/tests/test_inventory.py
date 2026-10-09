import pytest
import allure
from pages.inventory import Inventory
from test_data import SAUCEDEMO_DATA

EXPECTED_AZ_LIST = SAUCEDEMO_DATA["sorting"]["az"]
EXPECTED_ZA_LIST = SAUCEDEMO_DATA["sorting"]["za"]
EXPECTED_PRICE_LOHI = SAUCEDEMO_DATA["sorting"]["priceLowToHigh"]
EXPECTED_PRICE_HILO = SAUCEDEMO_DATA["sorting"]["priceHighToLow"]


@allure.epic("SauceDemo Project")
@allure.feature("Item Sort")
@allure.story("A->Z")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@allure.tag("regression")
def test_tc011_sort_name_a_to_z(logged_in_driver):
    inventory = Inventory(logged_in_driver)

    # Check A->Z
    item_names = inventory.get_all_items_name()
    assert item_names == EXPECTED_AZ_LIST, f"wrong sort: {item_names} Not A->Z "

    print(f"item list: {item_names}")


@allure.epic("SauceDemo Project")
@allure.feature("Item Sort")
@allure.story("Z->A")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@allure.tag("regression")
def test_tc012_sort_name_z_to_a(logged_in_driver):
    inventory = Inventory(logged_in_driver)

    inventory.click_sort_za()
    # Check Z->A
    item_names = inventory.get_all_items_name()
    assert item_names == EXPECTED_ZA_LIST, f"wrong sort: {item_names} Not Z->A "

    print(f"item list: {item_names}")


@allure.epic("SauceDemo Project")
@allure.feature("Item Sort")
@allure.story("Lo->Hi")
@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.regression
@allure.tag("regression")
def test_tc013_sort_price_low_to_high(logged_in_driver):
    inventory = Inventory(logged_in_driver)
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
@pytest.mark.regression
@allure.tag("regression")
def test_tc014_sort_price_high_to_low(logged_in_driver):
    inventory = Inventory(logged_in_driver)
    inventory.click_sort_hilo()

    item_prices = inventory.get_all_items_price()

    assert item_prices == EXPECTED_PRICE_HILO, f"wrong sort: {item_prices} Not Price high to low"
    print(f"item list: {item_prices}")
