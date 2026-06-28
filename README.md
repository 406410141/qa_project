# QA Automation Portfolio

這是一個用於練習與展示自動化測試與效能測試的整合專案，採用常見的測試框架與設計模式，目標是模擬實務上的測試架構與流程。

---


## Tech Stack

| Category | Tool |
|------|------|
| Language | Python 3.9+, JavaScript (K6) |
| UI Testing | Selenium WebDriver |
| API Testing | pytest + requests |
| Performance Testing | K6 |
| Framework | pytest |
| Design Pattern | Page Object Model (POM) |
| Reporting | Allure Report |
| CI/CD | GitHub Actions, Jenkins |


## 專案目錄結構 (Project Structure)
```text
qa_project/
├── api-testing/                    # API 自動化測試
│   ├── api_requests/               
│   │   ├── __init__.py
│   │   ├── base_api.py             # CRUD
│   │   ├── auth_api.py             
│   │   └── booking_api.py          
│   ├── test_case/                  # 測試案例
│   │   ├── __init__.py
│   │   ├── conftest.py             # pytest fixtures
│   │   ├── test_auth.py            # 認證測試
│   │   └── test_booking.py         # 訂單 CRUD 測試
│   
│
├── ui-testing/                     # UI 自動化測試
│   ├── pages/                      # Page Object Model
│   │   ├── __init__.py
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory.py
│   │   ├── cart_page.py
│   │   ├── checkout_step_one_page.py
│   │   ├── checkout_step_two_page.py
│   │   └── checkout_complete.py
│   ├── tests/                      # 測試案例
│   │   ├── __init__.py
│   │   ├── conftest.py
│   │   ├── test_cart.py
│   │   ├── test_checkout.py
│   │   ├── test_inventory.py
│   │   ├── test_login.py
│   │   ├── test_navigation.py
│   │   └── test_smoke.py
│   
│
├── performance-testing/            # K6 效能測試
│   ├── create_booking.js           # 基礎測試腳本
│   ├── spike_testing.js            # 尖峰測試
│   └── stress_testing.js           # 壓力測試
│
├── .github/workflows/              # GitHub Actions CI
│   ├── api-tests.yml
│   └── ui-tests.yml
│
│
├── requirements.txt   
├── pytest.ini
├── Jenkinsfile                     #            
└── README.md


## How To Run 

```bash
# 1. Install Dependencies
pip install -r requirement.txt

# 2. Run Script && Generate Allure Report
rm -rf allure-results
pytest --alluredir=allure-results
allure serve allure-results



```markdown
## CI/CD Pipeline

| Tool | Trigger | Description |
|------|---------|-------------|
| **GitHub Actions** | Push / Pull Request / Schedule | Execute API & UI tests and generate Allure report |
| **Jenkins** | Manual Trigger | Parallel execution of API & UI tests with Allure report |
