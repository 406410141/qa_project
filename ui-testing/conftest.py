import os
import platform
import pytest
import json
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from test_data import SAUCEDEMO_DATA


def _run_context():
    """依環境變數判斷測試是在哪裡執行的，供 Allure 報告顯示"""
    if os.getenv("GITHUB_ACTIONS") == "true":
        return {"name": "GitHub Actions", "type": "github", "build": os.getenv("GITHUB_RUN_NUMBER", "")}
    if os.getenv("JENKINS_URL"):
        return {"name": "Jenkins", "type": "jenkins", "build": os.getenv("BUILD_NUMBER", "")}
    return {"name": "Local", "type": "local", "build": "local"}


@pytest.fixture(scope="session", autouse=True)
def create_allure_environment_info(request):
    yield
    allure_dir = request.config.getoption("--alluredir")
    if allure_dir and os.path.exists(allure_dir):
        env_properties_path = os.path.join(allure_dir, "environment.properties")
        with open(env_properties_path, "w") as f:
            f.write("Browser=Chrome\n")
            f.write(f"Executor={_run_context()['name']}\n")
            f.write(f"Platform={platform.system()}\n")


def pytest_sessionfinish(session, exitstatus):
    results_dir = session.config.getoption('--alluredir')
    if results_dir and os.path.exists(results_dir):
        context = _run_context()
        executor_info = {
            "name": context["name"],
            "type": context["type"],
            "buildName": context["build"],
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

    # 通用設定
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-features=SafeBrowsingPasswordProtection")
    chrome_options.add_argument("--incognito")

    # ✅ 自動判斷 CI 環境
    is_ci = os.getenv("CI") == "true"

    if is_ci:
        # CI：無頭模式
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--window-size=1920,1080")
    else:
        # 本地：顯示視窗
        chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(options=chrome_options)

    if not is_ci:
        driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def logged_in_driver(driver):
    login_page = LoginPage(driver)
    driver.get(login_page.URL)
    credentials = SAUCEDEMO_DATA["credentials"]
    login_page.login(credentials["username"], credentials["password"])
    login_page.wait_url("https://www.saucedemo.com/inventory.html")
    return driver
