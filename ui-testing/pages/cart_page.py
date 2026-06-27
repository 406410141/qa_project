from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class Cart(BasePage):
    CONTINUE_SHOP = (By.ID, 'continue-shopping')
    CHECKOUT = (By.ID, 'checkout')
    CART_TITLE = (By.XPATH, "//span[@data-test='title']")

    CART_ITEM_CONTAINER = (By.CLASS_NAME, "cart_item")
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_QTY = (By.CLASS_NAME, "cart_quantity")

    def get_all_items_detail(self):

        items_elements = self.find_elements(self.CART_ITEM_CONTAINER)
        parsed_items = []
        for element in items_elements:
            name = element.find_element(*self.ITEM_NAME).text
            price_raw = element.find_element(*self.ITEM_PRICE).text
            qty = element.find_element(*self.ITEM_QTY).text
            parsed_items.append({
                "name": name,
                "price": float(price_raw.replace('$', '')),
                "qty": int(qty)
            })
        return parsed_items
