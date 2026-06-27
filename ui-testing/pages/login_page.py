from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    URL = 'https://www.saucedemo.com/'
    # ============================================================
    # (Actively Used Locators)
    # ============================================================
    USER_ACCOUNT = (By.ID, 'user-name')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')
    ERROR_CONTAINER = (By.CSS_SELECTOR, "h3[data-test='error']")
    CLOSE_REMIND = (By.CLASS_NAME, 'error-button')

    # ============================================================
    # (Reserved / Pending Cleanup)
    # ============================================================
    LOGO = (By.CLASS_NAME, 'login_logo')
    All_USERNAMES = (By.XPATH, '//*[@id="login_credentials"]')
    All_PASSWORD = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div/div[2]')
    ACCEPTED_USERNAMES = 'standard_user'
    ACCEPTED_PASSWORD = 'secret_sauce'
    ERROR_REMIND = (By.XPATH, '//*[@id="login_button_container"]/div/form/div[3]/h3')

    def login(self, username, password):
        self.driver.get(self.URL)
        self.fill(self.USER_ACCOUNT, username)
        self.fill(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(self.ERROR_CONTAINER)

    def click_error_button(self):
        self.click(self.CLOSE_REMIND)

    def is_error_message_hidden(self) -> bool:
        return not self.is_visible(self.ERROR_CONTAINER)
