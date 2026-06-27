from pages.base_page import BasePage
from selenium.webdriver.common.by import By


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
    SORT_ZA_OPTION = (By.CSS_SELECTOR, "option[value='za']")
    SORT_LOHI_OPTION = (By.CSS_SELECTOR, "option[value='lohi']")
    SORT_HILO_OPTION = (By.CSS_SELECTOR, "option[value='hilo']")
    ITEM_PRICE = (By.CLASS_NAME, 'inventory_item_price')

    def click_side(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def is_sidebar_hidden(self):
        status = self.driver.find_element(*self.SIDE_BAR).get_attribute('aria-hidden')
        print(status)

        return status == 'true'

    def click(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    def get_all_items_name(self):
        """獲取所有商品名稱的文字清單"""
        # 使用 find_elements 抓取所有符合 ITEM_NAMES 的元素
        items = self.driver.find_elements(*self.ITEM_NAMES)
        # 加上 .strip() 確保去除換行或多餘空格，這對後續 A-Z 排序斷言非常重要
        name_list = [item.text.strip() for item in items]
        return name_list

    def click_sort_za(self):
        self.driver.find_element(*self.SORT_SELECT).click()
        self.driver.find_element(*self.SORT_ZA_OPTION).click()

    def click_sort_lohi(self):

        self.driver.find_element(*self.SORT_SELECT).click()
        self.driver.find_element(*self.SORT_LOHI_OPTION).click()

    def click_sort_hilo(self):

        self.driver.find_element(*self.SORT_SELECT).click()
        self.driver.find_element(*self.SORT_HILO_OPTION).click()

    def get_all_items_price(self):
        items = self.driver.find_elements(*self.ITEM_PRICE)
        price_list = [float(item.text.strip().replace('$', '')) for item in items]
        return price_list
