# 路由與頁面設計 (Routes & Template Plan)

根據系統流程圖與架構設計，本系統的路由規劃如下。

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| -- | -- | -- | -- | -- |
| 首頁 | GET | `/` | `templates/index.html` | 網站首頁，顯示系統介紹與功能入口 |
| 註冊頁面 | GET | `/register` | `templates/register.html` | 顯示註冊表單 |
| 送出註冊 | POST | `/register` | — | 接收表單，建立使用者，重導向至登入頁 |
| 登入頁面 | GET | `/login` | `templates/login.html` | 顯示登入表單 |
| 送出登入 | POST | `/login` | — | 驗證帳密，設定 Session，重導向至首頁 |
| 登出 | GET | `/logout` | — | 清除 Session，重導向至首頁 |
| 抽籤頁面 | GET | `/fortune/draw` | `templates/draw.html` | 顯示抽籤互動畫面與表單（填寫問題） |
| 進行抽籤 | POST | `/fortune/draw` | — | 隨機產生籤詩，儲存紀錄，重導向至結果頁 |
| 籤詩結果 | GET | `/fortune/result/<id>` | `templates/result.html` | 顯示特定解籤結果與白話文 |
| 歷史紀錄 | GET | `/history` | `templates/history.html` | 檢視個人過去的抽籤與算命結果 |
| 捐款頁面 | GET | `/donate` | `templates/donate.html` | 顯示香油錢捐獻表單 |
| 送出捐款 | POST | `/donate` | `templates/donate_success.html` | 接收表單，寫入紀錄，顯示感謝祈福畫面 |

---

## 2. 每個路由的詳細說明

### `main.py`
- **GET `/` (首頁)**
  - 處理邏輯：無複雜邏輯，直接渲染畫面。
  - 輸出：`index.html`
- **GET `/history` (歷史紀錄)**
  - 處理邏輯：檢查登入狀態。利用 `History.get_by_user_id` 撈取過去的抽籤與捐款結果。
  - 輸出：渲染 `history.html`。若未登入則導向 `/login`。

### `auth.py`
- **GET/POST `/register`**
  - 輸入：`username`, `email`, `password`。
  - 處理邏輯：驗證 email 是否已被註冊。若無，將密碼 Hash 化並呼叫 `User.create`。
  - 輸出：成功重導 `/login`，失敗回傳錯誤訊息並重新渲染 `register.html`。
- **GET/POST `/login`**
  - 輸入：`email`, `password`。
  - 處理邏輯：從 DB 抓取 User 驗證。成功則寫入 `session['user_id']`。
  - 輸出：成功重導 `/`，失敗回傳錯誤訊息並重新渲染 `login.html`。
- **GET `/logout`**
  - 處理邏輯：移除 session 資訊。
  - 輸出：重導 `/`。

### `fortune.py`
- **GET/POST `/fortune/draw`**
  - 輸入：(POST) `question`（問題）。
  - 處理邏輯：呼叫 `Lot.get_random` 取得結果。若使用者已登入，可同時呼叫 `History.create` 記錄至資料庫。
  - 輸出：重導至 `/fortune/result/<id>`。
- **GET `/fortune/result/<id>`**
  - 輸入：`id` (lot_id 或 history_id，視設計而定，建議帶 history_id 或透過 session 暫存結果)。
  - 處理邏輯：利用 `History.get_by_id` 及關聯 `Lot` 取得資料。
  - 輸出：呈現 `result.html`。
- **GET/POST `/donate`**
  - 輸入：(POST) `amount`, `message`。
  - 處理邏輯：接受訪客或登入使用者的捐獻，呼叫 `Donation.create` 產生紀錄。
  - 輸出：成功則渲染 `donate_success.html` 播放感謝動畫。

---

## 3. Jinja2 模板清單

所有模板皆繼承 `base.html`，以保持視覺風格一致：
- `base.html`: 共用佈局（Navbar, Footer, CSS 引入）。
- `index.html`: 首頁。
- `register.html`: 註冊畫面。
- `login.html`: 登入畫面。
- `draw.html`: 呈現抽籤按鈕與搖籤筒微動畫的頁面。
- `result.html`: 單一籤詩詳細解析。
- `history.html`: 條列過去求籤結果清單。
- `donate.html`: 捐獻香油錢表單頁面。
- `donate_success.html`: 捐獻後的感謝動畫/訊息頁。
