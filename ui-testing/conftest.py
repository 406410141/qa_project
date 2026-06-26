import pytest
import json
import os
import allure
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage


@pytest.fixture(scope="session", autouse=True)
def create_allure_environment_info(request):

    yield
    allure_dir = request.config.getoption("--alluredir")
    if allure_dir and os.path.exists(allure_dir):
        env_properties_path = os.path.join(allure_dir, "environment.properties")
        with open(env_properties_path, "w") as f:
            f.write("Browser=Chrome\n")
            f.write("Environment=Staging\n")
            f.write("Platform=macOS\n")

def pytest_sessionfinish(session, exitstatus):
    results_dir = session.config.getoption('--alluredir')
    if results_dir and os.path.exists(results_dir):
        executor_info = {
            "name": "Tung-MacBookPro",
            "type": "manual",
            "buildName": "Daily-Check-2026",
            "reportName": "UI-Automation-Suite"
        }
        with open(os.path.join(results_dir, 'executor.json'), 'w') as f:
            json.dump(executor_info, f)

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get('driver')
        
        if driver:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )

@pytest.fixture(scope="function")
def driver():
    chrome_options = Options()

    # 設定：禁用密碼管理員與密碼外洩警告
    # 防止 Chrome 彈出「變更你的密碼」視窗
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    #CI
    chrome_options.add_argument("--headless")                
    chrome_options.add_argument("--no-sandbox")              
    chrome_options.add_argument("--disable-dev-shm-usage")    
    chrome_options.add_argument("--disable-gpu")              
    chrome_options.add_argument("--window-size=1920,1080")

    # 禁用安全瀏覽的密碼保護功能並開啟無痕模式
    chrome_options.add_argument("--disable-features=SafeBrowsingPasswordProtection")
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(10)

    yield driver

    print("\n--- [Teardown] 關閉瀏覽器 ---")
    driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.URL)
    login_page.login("standard_user", "secret_sauce")


    assert driver.current_url == "https://www.saucedemo.com/inventory.html", "登入失敗，請檢查帳號密碼"
        
    return driver