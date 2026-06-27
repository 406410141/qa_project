from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutComplete(BasePage):
    COMPLETE_TITLE = (By.CLASS_NAME, "title")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")
    COMPLETE_TEXT = (By.CLASS_NAME, "complete-text")
    BACK_HOME_BTN = (By.ID, 'back-to-products')

    def get_complete_title(self):
        # Checkout: Complete!
        return self.get_text(self.COMPLETE_TITLE)

    def get_complete_header(self):
        # THANK YOU FOR YOUR ORDER
        return self.get_text(self.COMPLETE_HEADER)

    def get_complete_text(self):
        # Your order has been dispatched, and will arrive just as fast as the pony can get there!
        return self.get_text(self.COMPLETE_TEXT)

    def click_back_home_btn(self):
        self.click(self.BACK_HOME_BTN)
