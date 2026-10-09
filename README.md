# QA Automation Portfolio

[![Run API Tests](https://github.com/406410141/qa_project/actions/workflows/api-tests.yml/badge.svg)](https://github.com/406410141/qa_project/actions/workflows/api-tests.yml)
[![Run UI Tests](https://github.com/406410141/qa_project/actions/workflows/ui_tests.yml/badge.svg)](https://github.com/406410141/qa_project/actions/workflows/ui_tests.yml)
[![Run UI-Playwright Tests](https://github.com/406410141/qa_project/actions/workflows/playwright.yml/badge.svg)](https://github.com/406410141/qa_project/actions/workflows/playwright.yml)

> **Run API Tests** 的紅燈是刻意保留的，原因見下方的 Known Issues。

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
│   └── tests/
│       ├── test_cart.py
│       ├── test_checkout.py
│       ├── test_inventory.py
│       ├── test_login.py
│       ├── test_navigation.py
│       └── test_smoke.py
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
└── README.md
```



---

## CI/CD Pipeline

| Tool | Trigger | Description |
|------|---------|-------------|
| **GitHub Actions** | Push / Pull Request | Run API, Selenium UI and Playwright tests |
| **Jenkins** | Manual Trigger | Run API, Selenium UI, Playwright UI and K6 tests |

---

## Known Issues（為什麼 API 測試是紅燈）

GitHub Actions 的 **Run API Tests** 目前固定失敗，這是刻意保留的結果，不是測試程式壞掉。

測試對象 [restful-booker](https://restful-booker.herokuapp.com) 是公開的練習用 API，本身帶有缺陷。以下 3 個負向案例送出不合法的資料，預期應被拒絕，實際卻回傳 `200` 並建立訂單：

| Case | 送出的資料 | 預期 | 實際 |
|------|-----------|------|------|
| `wrong_totalprice_type` | `totalprice: "one_hundred"` | 拒絕請求 | `200`，`totalprice` 存成 `null` |
| `wrong_depositpaid_type` | `depositpaid: "Yes"` | 拒絕請求 | `200`，存成 `true` |
| `wrong_bookingdates_format` | `checkin: "not-a-date"` | 拒絕請求 | `200`，日期存成 `0NaN-aN-aN` |

對應的測試在 `api-testing/test_case/test_CreateBooking.py` 的 `test_create_booking_invalid_inputs`。其餘 API 測試皆通過。

---

## AI-assisted Testing

這個專案使用 [Claude Code](https://claude.com/claude-code) 協助開發，主要用在三個地方：

| 用途 | 做法 |
|------|------|
| Code Review | 請 AI 檢查整個專案，列出問題後逐項判斷要不要處理 |
| 重構 | 抽出共用 fixture、測試資料外部化、合併重複的測試流程 |
| 除錯分析 | 分析失敗訊息、協助重現不穩定的測試 |

### 原則：AI 的說法要實測過才算數

- 程式修改在合併前，都會在本機執行對應的測試，並把實際結果寫在 PR 說明裡。
- 不穩定的測試不以「跑一次通過」為準，而是連續執行多次確認。
- AI 的推論與實際執行結果不一致時，以實際執行結果為準。

### 兩個實際案例

**1. AI 對程式行為的解讀錯誤**

一個「無效 token」的 API 測試一直是通過的。請 AI 解讀時，得到的回答是送出的 Cookie 為 `token=invalid_token_12345_xyz`，寫法沒有問題。實際把請求內容印出來後，送出的卻是：

```
token={'Cookie': 'token=invalid_token_12345_xyz'}
```

原因是測試把整個 header dict 傳進了預期為字串的 `token` 參數。伺服器同樣回 403，所以測試會通過，但驗到的不是預期的情境。修正見 [PR #4](https://github.com/406410141/qa_project/pull/4)。

**2. Flaky test 的原因要靠量測，不是靠猜**

Selenium 的結帳測試偶爾失敗，讀到上一頁的標題。一開始的想法是把全域等待時間拉長，實驗結果是連跑 10 次仍失敗 1 次。之後另外寫腳本量測，才確認原因：換頁時網址先更新、標題約晚 10ms 才更新，而新舊頁面共用同一個標題元素，「等元素可見」無法區分新舊。改為等待標題文字更新後，連跑 15 次全數通過。修正見 [PR #7](https://github.com/406410141/qa_project/pull/7)。

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
```

### Playwright Tests
```bash
cd playwright-testing

npm ci
npx playwright install

# Run tests
npx playwright test

# Playwright HTML Report
npx playwright show-report

# Allure Report
npm run allure:report
```

### K6 Performance Tests
```bash
cd performance-testing

# Baseline
k6 run create_booking.js

# Spike
k6 run spike_testing.js

# Stress
k6 run stress_testing.js

# Combined Report
node merge_reports.js
```

### Run By Tag

```bash
# Python (API + Selenium): smoke / regression / negative
pytest -m smoke
pytest -m "regression and not smoke"

# Playwright: @smoke / @regression / @negative
npx playwright test --grep @smoke
```

### Reports

| Report | Description |
|--------|-------------|
| **Allure Report** | API, Selenium UI and Playwright test results |
| **Playwright HTML Report** | Playwright test results with screenshots, videos and traces |
| **K6 HTML Report** | Baseline, Spike and Stress test results |