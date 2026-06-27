from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePage:

    def __init__(self, driver, timeout: int = 10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def wait_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def wait_present(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def wait_invisible(self, locator):
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def find_element(self, locator):
        return self.wait_visible(locator)

    def find_elements(self, locator):
        self.wait.until(EC.presence_of_all_elements_located(locator))
        return self.driver.find_elements(*locator)

    def click(self, locator):
        self.wait_clickable(locator).click()

    def fill(self, locator, text: str, clear_first: bool = True):
        element = self.wait_visible(locator)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator) -> str:

        return self.wait_visible(locator).text.strip()

    def is_visible(self, locator) -> bool:
        try:
            self.wait_visible(locator)
            return True
        except TimeoutException:
            return False

    def is_not_visible(self, locator) -> bool:
        return not self.is_visible(locator)

    def is_element_hidden(self, locator) -> bool:
        try:
            element = self.driver.find_element(*locator)
            return not element.is_displayed()
        except:
            return True
