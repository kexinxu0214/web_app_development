# 算命系統 流程圖 (Flowchart & Sequence Diagram)

根據需求規格書 (PRD) 與系統架構文件 (Architecture)，此文件定義了使用者的操作流程、後端處理的序列圖，以及系統初步的路由設計對照表。

## 1. 使用者流程圖 (User Flow)

描述使用者從進入首頁後，到抽籤、查看紀錄與捐香油錢的整體操作路徑。

```mermaid
flowchart LR
    Start([使用者進入首頁]) --> Home[首頁 - 選擇算命項目]
    
    Home --> Choice{要執行什麼操作？}
    
    Choice -->|進行抽籤/占卜| Draw[進入抽籤畫面]
    Draw --> Animation[呈現微動畫與儀式感]
    Animation --> Result[顯示籤詩與白話文解析]
    
    Result --> Action{對結果進行後續動作}
    Action -->|儲存| AuthCheck{是否已登入？}
    AuthCheck -->|是| SaveRecord[儲存結果至歷史紀錄]
    AuthCheck -->|否| Auth[導向登入/註冊頁面]
    Action -->|分享| Share[產生社群分享預覽]
    
    Choice -->|查看歷史| History[歷史紀錄列表]
    
    Choice -->|捐獻香油錢| Donate[香油錢入口]
    Donate --> DonateForm[填寫捐獻金額與祈福語]
    DonateForm --> DonateSuccess[顯示感謝與祈福動畫]
    
    Auth --> SaveRecord
    SaveRecord --> History
```

## 2. 系統序列圖 (Sequence Diagram)

以下以系統中最核心的「**登入使用者進行抽籤並自動儲存結果**」為例，展示前端瀏覽器、Flask 路由、Model 與 SQLite 之間的資料流動。

```mermaid
sequenceDiagram
    actor User as 使用者
    participant Browser
    participant Flask Route
    participant Model
    participant DB as SQLite

    User->>Browser: 點擊「開始抽籤」按鈕
    Browser->>Flask Route: POST /fortune/draw
    
    Flask Route->>Model: 呼叫產生隨機籤邏輯
    Model->>DB: SELECT * FROM lots ORDER BY RANDOM() LIMIT 1
    DB-->>Model: 回傳籤詩與解析內容
    
    Flask Route->>Flask Route: 確認使用者 Session (已登入)
    
    Flask Route->>Model: 儲存此抽籤紀錄 (包含 user_id, lot_id)
    Model->>DB: INSERT INTO history (user_id, lot_id, date)
    DB-->>Model: 儲存成功
    
    Model-->>Flask Route: 處理完成
    
    Flask Route->>Browser: 重導向到結果頁面 (GET /fortune/result/{id})
    Browser-->>User: 顯示抽籤結果與解析畫面
```

## 3. 功能清單對照表

本表格列出系統主要功能、對應的 URL 路徑 (Routes) 與適用的 HTTP 方法，供後續實作對齊使用。

| 功能模組 | 頁面/功能說明 | URL 路徑 | HTTP 方法 |
| -- | -- | -- | -- |
| **首頁** | 網站首頁，顯示系統介紹與功能入口 | `/` | GET |
| **會員系統** | 顯示註冊頁面 / 提交註冊表單 | `/register` | GET / POST |
| **會員系統** | 顯示登入頁面 / 提交登入表單 | `/login` | GET / POST |
| **會員系統** | 使用者登出 (清除 Session) | `/logout` | GET |
| **算命功能** | 顯示抽籤畫面 / 送出抽籤請求 | `/fortune/draw` | GET / POST |
| **算命功能** | 顯示特定一筆籤詩與解析 | `/fortune/result/<id>` | GET |
| **歷史紀錄** | 檢視個人過去的抽籤與算命結果 | `/history` | GET |
| **香油錢** | 顯示捐款畫面 / 送出虛擬捐款表單 | `/donate` | GET / POST |
