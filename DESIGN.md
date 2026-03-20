# DESIGN.md

## 1. 系統目標（System Goal）

本專案旨在建立一個「AI 研究所考試準備平台」，協助學生有效準備研究所入學考試。

系統主要功能包括：
- 蒐集與整理歷年考古題
- 分析各科考試主題出現頻率
- 記錄學生錯題與弱點
- 自動生成個人化讀書計畫
- 預測未來可能出題重點

---

## 2. 使用情境（Use Cases）

### 學生端
- 瀏覽歷年考古題
- 查看各主題的重要程度
- 記錄錯題並分析弱點
- 取得 AI 生成的讀書計畫

### 系統端
- 分析歷年考題資料
- 統計各主題出現頻率
- 預測未來考試趨勢
- 動態調整讀書建議

---

## 3. 功能模組切分（Functional Modules）

本系統可分為以下模組：

- 資料蒐集模組（Data Collection）
- 資料前處理模組（Data Preprocessing）
- 題目分類模組（Question Classification）
- 預測與分析模組（Prediction & Analytics）
- 錯題追蹤模組（Mistake Tracking）
- 讀書計畫生成模組（Study Plan Generator）
- 後端 API 服務（Backend API）
- 前端使用者介面（Frontend Dashboard）

---

## 4. Orchestration 角色設計（Agent Roles）

本專案採用多 Agent 協作模式：

- Planner（規劃者）  
  負責拆解任務與安排執行流程

- Architect（架構設計者）  
  將高層設計轉換為系統架構

- Coder（開發者）  
  實作後端、前端與資料處理模組

- Reviewer（檢查者）  
  檢查程式正確性與整體一致性

- Tool Runner（工具執行者）  
  負責使用工具（讀檔、掃描 repo、執行指令）

---

## 5. 資料流與控制流程（Data Flow & Control Flow）

系統流程如下：

1. 蒐集歷年考試資料
2. 對資料進行清理與結構化處理
3. 將題目分類至不同主題
4. 分析各主題出現頻率
5. 後端透過 API 提供資料服務
6. 前端顯示分析結果與讀書建議
7. 使用者錯題會被記錄並回饋至系統
8. 系統根據錯題與趨勢生成讀書計畫

---

## 6. 為什麼需要 Orchestration（Why Orchestration is Required）

本系統具備以下特性：

- 包含多個相依模組（資料處理、分析、API、前端）
- 任務之間存在明確執行順序
- 需要多階段開發（設計 → 架構 → 實作 → 修正）
- 需要中間檢查與反覆修正

因此無法透過單一 Prompt 完成整個專案。

必須透過 Orchestration 模式來：
- 拆解任務
- 安排執行順序
- 協調不同 Agent
- 進行階段性檢查與優化