# QA Automation Portfolio

這是一個用於練習與展示自動化測試、效能測試與 CI/CD 整合的完整專案，涵蓋 API、UI（Selenium 與 Playwright 雙框架）、效能測試三種層面，並將測試流程整合進 Jenkins 與 GitHub Actions 兩套 CI/CD 系統。

---

## Tech Stack

| Category | Tool |
|------|------|
| Language | Python 3.9+, TypeScript, JavaScript (K6) |
| UI Testing | Selenium WebDriver, Playwright |
| API Testing | pytest + requests |
| Performance Testing | K6 |
| Framework | pytest, Playwright Test Runner |
| Design Pattern | Page Object Model (POM) |
| Reporting | Allure Report, Playwright HTML Report, K6 HTML Report |
| CI/CD | GitHub Actions, Jenkins |

---

## 專案目錄結構 (Project Structure)

```text
qa_project/
├── api-testing/                    # API 自動化測試 (Python + pytest)
│   ├── api_requests/
│   │   ├── __init__.py
│   │   ├── base.py                 # API 共用請求方法
│   │   ├── auth_api.py
│   │   └── booking_api.py
│   ├── data/                       # API 測試資料
│   │   ├── create_booking_data.py
│   │   ├── get_booking_data.py
│   │   └── invalid_booking_cases.json
│   └── test_case/
│       ├── __init__.py
│       ├── conftest.py             # pytest fixtures
│       ├── test_auth.py
│       ├── test_CreateBooking.py
│       ├── test_DeleteBooking.py
│       ├── test_GetBooking.py
│       ├── test_GetBookingIds.py
│       ├── test_PartialUpdateBooking.py
│       └── test_UpdateBooking.py
│
├── ui-testing/                     # UI 自動化測試 (Python + Selenium)
│   ├── conftest.py                 # WebDriver、Allure、登入 fixture
│   ├── test_data.py                # 讀取專案共用 JSON 測試資料
│   ├── pages/                      # Page Object Model
│   │   ├── base_page.py
│   │   ├── login_page.py
│   │   ├── inventory.py
│   │   ├── cart_page.py
│   │   ├── checkout_step_one_page.py
│   │   ├── checkout_step_two_page.py
│   │   └── checkout_complete.py
│   ├── tests/
│   │   ├── test_cart.py
│   │   ├── test_checkout.py
│   │   ├── test_inventory.py
│   │   ├── test_login.py
│   │   ├── test_navigation.py
│   │   └── test_smoke.py
│   └── utils/                      # 工具函式
│
├── playwright-testing/             # UI 自動化測試 (TypeScript + Playwright)
│   ├── features/
│   │   └── login.feature           # BDD Feature 檔案
│   ├── fixtures/
│   │   └── authenticated.fixture.ts # 登入後的自訂 fixture
│   ├── pages/                      # Page Object Model
│   │   ├── base.page.ts
│   │   ├── login_page.ts
│   │   ├── inventory.ts
│   │   ├── cart_page.ts
│   │   ├── checkout_step_one_page.ts
│   │   ├── checkout_step_two_page.ts
│   │   └── checkout_complete.ts
│   ├── test-data/
│   │   └── saucedemo.data.ts       # TypeScript test-data helper
│   ├── tests/                      # Playwright 測試案例
│   │   ├── test_cart.spec.ts
│   │   ├── test_checkout.spec.ts
│   │   ├── test_inventory.spec.ts
│   │   ├── test_login.spec.ts
│   │   ├── test_navigation.spec.ts
│   │   └── test_smoke.spec.ts
│   ├── utils/                      # 工具函式
│   ├── playwright.config.ts
│   ├── package.json
│   └── package-lock.json
│
├── performance-testing/            # K6 效能測試
│   ├── create_booking.js           # Baseline 測試
│   ├── spike_testing.js            # 尖峰測試
│   ├── stress_testing.js           # 壓力測試
│   ├── merge_reports.js            # 報告彙整工具
│   ├── index.html                  # 效能報告首頁
│   └── report_data/                # 產生的 HTML / JSON 報告
│
├── test-data/
│   └── saucedemo.json              # Selenium 與 Playwright 共用測試資料
│
├── .github/workflows/              # GitHub Actions CI
│   ├── api-tests.yml
│   ├── ui_tests.yml
│   └── playwright.yml
│
├── Jenkinsfile                     # Jenkins Pipeline
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md




---

## CI/CD Pipeline

| Tool | Trigger | Description |
|------|---------|-------------|
| **GitHub Actions** | Push / Pull Request | Run API, Selenium UI and Playwright tests |
| **Jenkins** | Manual Trigger | Run API, Selenium UI, Playwright UI and K6 tests |

---

## How To Run

### Python Tests

```bash
pip install -r requirements.txt

# API Tests
pytest api-testing/test_case/ -v

# Selenium UI Tests
pytest ui-testing/tests/ -v

# Allure Report
pytest --alluredir=allure-results
allure serve allure-results

Playwright Tests
cd playwright-testing

npm ci
npx playwright install

# Run tests
npx playwright test

# Playwright HTML Report
npx playwright show-report

# Allure Report
npm run allure:report
K6 Performance Tests
cd performance-testing

# Baseline
k6 run create_booking.js

# Spike
k6 run spike_testing.js

# Stress
k6 run stress_testing.js

# Combined Report
node merge_reports.js
Reports
Report	Description
Allure Report	API, Selenium UI and Playwright results
Playwright HTML Report	Playwright results with screenshots, videos and traces
K6 HTML Report	Baseline, Spike and Stress results
```