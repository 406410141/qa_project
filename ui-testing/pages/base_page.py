from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


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

    def wait_text(self, locator, text: str):
        # 換頁後新舊頁面可能共用同一個 locator（例如 .title），
        # 所以要等「文字變成預期內容」，只等元素可見會讀到舊頁面的文字
        self.wait.until(
            EC.text_to_be_present_in_element(locator, text),
            message=f"Text '{text}' not shown in {locator}",
        )

    def wait_url(self, url: str):
        # 點擊後頁面跳轉需要時間，所以等網址變成預期值，逾時才算失敗
        try:
            self.wait.until(EC.url_to_be(url))
        except TimeoutException:
            raise AssertionError(f"Expected URL {url}, got {self.driver.current_url}") from None

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
        except NoSuchElementException:
            return True
