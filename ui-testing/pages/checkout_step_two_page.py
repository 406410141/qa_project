from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutStepTwo(BasePage):
    # Locators
    CHECKOUT_TITLE = (By.CLASS_NAME, "title")
    CART_ITEM = (By.CLASS_NAME, "cart_item")

    # Amounts
    ITEM_TOTAL = (By.CLASS_NAME, "summary_subtotal_label")
    TAX = (By.CLASS_NAME, "summary_tax_label")
    TOTAL = (By.CLASS_NAME, "summary_total_label")

    # Payment and Shipping Information
    PAYMENT_VALUE = (By.CSS_SELECTOR, '[data-test="payment-info-value"]')
    SHIPPING_VALUE = (By.CSS_SELECTOR, '[data-test="shipping-info-value"]')

    # Item Details
    ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")
    ITEM_PRICE = (By.CLASS_NAME, "inventory_item_price")
    ITEM_QTY = (By.CLASS_NAME, "cart_quantity")

    FINISH_BTN = (By.ID, "finish")

    # Methods
    def get_checkout_items_detail(self):
        items_elements = self.find_elements(self.CART_ITEM)
        parsed_items = []
        for element in items_elements:
            name = element.find_element(*self.ITEM_NAME).text
            price_raw = element.find_element(*self.ITEM_PRICE).text
            qty = element.find_element(*self.ITEM_QTY).text
            parsed_items.append(
                {
                    "name": name,
                    "price": float(price_raw.replace("$", "")),
                    "qty": int(qty),
                }
            )
        return parsed_items

    def get_payment_info(self) -> str:
        return self.get_text(self.PAYMENT_VALUE)

    def get_financial_summary(self) -> dict:
        subtotal = float(self.get_text(self.ITEM_TOTAL).replace("Item total: $", ""))
        tax = float(self.get_text(self.TAX).replace("Tax: $", ""))
        total = float(self.get_text(self.TOTAL).replace("Total: $", ""))
        return {"subtotal": subtotal, "tax": tax, "total": total}

    def click_finish(self):
        self.click(self.FINISH_BTN)
