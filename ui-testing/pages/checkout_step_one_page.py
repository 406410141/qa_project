from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutStepOne(BasePage):
    CHECKOUT_TITLE = (By.CLASS_NAME, "title")
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    ZIP_CODE = (By.ID, 'postal-code')
    CONTINUE_BTN = (By.ID, 'continue')

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.fill(self.FIRST_NAME, first_name)
        self.fill(self.LAST_NAME, last_name)
        self.fill(self.ZIP_CODE, zip_code)

    def click_continue(self):
        self.click(self.CONTINUE_BTN)
