<!-- PR 標題格式：類型: 做了什麼　例如　fix: 修正結帳測試的等待問題 -->

## 改了什麼
<!-- 一到三點，說明這個 PR 做了哪些修改 -->
-

## 為什麼要改
<!-- 修 bug、網站改版、重構、補測試案例…… -->

## 影響範圍
- [ ] API 測試（api-testing）
- [ ] Selenium UI 測試（ui-testing）
- [ ] Playwright 測試（playwright-testing）
- [ ] K6 效能測試（performance-testing）
- [ ] CI（GitHub Actions / Jenkins）
- [ ] 文件

## 測試結果
<!-- 只填有跑的；沒跑的寫「未執行」。API 的 3 個已知失敗見 README 的 Known Issues -->
| 測試 | 指令 | 結果 |
|------|------|------|
| API | `pytest api-testing/test_case` | |
| Selenium UI | `pytest ui-testing/tests` | |
| Playwright | `npx playwright test` | |

## 備註
<!-- 已知問題、還沒做完的部分、截圖。沒有就刪掉這一節 -->
