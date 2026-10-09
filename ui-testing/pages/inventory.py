from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


class Inventory(BasePage):
    SIDE = (By.ID, 'react-burger-menu-btn')
    ALL_ITEMS_LINK = (By.ID, 'inventory_sidebar_link')
    ABOUT_LINK = (By.ID, 'about_sidebar_link')
    LOGOUT_LINK = (By.ID, 'logout_sidebar_link')
    RESET_LINK = (By.ID, 'reset_sidebar_link')
    CLOSE_SIDEBAR = (By.ID, 'react-burger-cross-btn')
    SIDE_BAR = (By.CLASS_NAME, 'bm-menu-wrap')
    SHOP_CART = (By.CLASS_NAME, 'shopping_cart_link')
    CART_ITEM = (By.CLASS_NAME, 'shopping_cart_badge')

    ADD_ITEM_BACKPACK = (By.ID, 'add-to-cart-sauce-labs-backpack')
    ADD_ITEM_ONESIE = (By.ID, 'add-to-cart-sauce-labs-onesie')
    ADD_ITEM_RED_TSHIRT = (By.ID, 'add-to-cart-test.allthethings()-t-shirt-(red)')

    Inventory_List = (By.CLASS_NAME, 'inventory_list')
    ITEM_NAMES = (By.CLASS_NAME, 'inventory_item_name')
    SORT_SELECT = (By.CLASS_NAME, 'product_sort_container')
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')

    def open_side_menu(self):
        self.click(self.SIDE)
        # 選單是滑入的動畫，等它完全滑進畫面（x 座標回到 0）再操作裡面的連結
        self.wait.until(lambda d: d.find_element(*self.SIDE_BAR).location["x"] >= 0)

    def is_sidebar_hidden(self):
        return self.wait_present(self.SIDE_BAR).get_attribute('aria-hidden') == 'true'

    def get_all_items_name(self):
        """獲取所有商品名稱的文字清單"""
        items = self.find_elements(self.ITEM_NAMES)
        return [item.text.strip() for item in items]

    def sort_by(self, value: str):
        # 排序選單是 <select>，用 Select 直接依 value 選取
        Select(self.wait_visible(self.SORT_SELECT)).select_by_value(value)

    def click_sort_za(self):
        self.sort_by("za")

    def click_sort_lohi(self):
        self.sort_by("lohi")

    def click_sort_hilo(self):
        self.sort_by("hilo")

    def get_all_items_price(self):
        items = self.find_elements(self.ITEM_PRICE)
        return [float(item.text.strip().replace('$', '')) for item in items]
