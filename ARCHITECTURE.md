1. 目標（Goal）
在 AI 研究所考試準備平台 基礎上，確保系統可部署、具模組化、可測試、可擴展、支援 Orchestration（流程協調）。

2. 系統分層與模組
2.1 Backend 模組（核心服務、商業邏輯）
路徑：backend
責任：
提供 REST/GraphQL API
使用者（學生）認證與授權
管理題庫、分類、分析結果、錯題紀錄、讀書計畫
排程/即時計算：主題頻率、趨勢預測、讀書計畫生成、錯題更新
子模組：
api/
services/
models/（ORM）
jobs/（pipeline orchestration）
db/（PostgreSQL / SQLite / MySQL）
2.2 Frontend 模組（可視化與使用者互動）
路徑：frontend
責任：
Dashboard（題庫瀏覽、主題分析、錯題、計畫）
API 呼叫並呈現 JSON 數據
表單/事件：錯題回報、個人偏好、閱讀進度、刷新
auth 流程（登入、登出、session token）
UI 組件：題目瀏覽、統計圖表、推薦清單
2.3 Data Pipeline 模組（資料處理與 ETL）
路徑：data_pipeline/ 或 backend/pipeline/
責任：
歷年考古題收集（抓取 + 輸入）
格式化／清理（斷行、分段、標籤）
分類/標記（主題分類）
分析（主題份額、趨勢）
生成（讀書計畫、錯題分析）
可調度：Cron / Celery / Airflow / GitHub Actions
要件：
原始資料（RAW）→ 淨化（CLEAN）→ 結構化（STRUCTURED）→ 輸出到後端 DB
3. 組件關係圖（Who calls who）
frontend → backend API（主要）
backend → data pipeline（觸發或閱讀結果）
data pipeline → backend DB（寫入）
backend scheduler/job → data pipeline（批次、重訓）
backend → AI service（可選：內部/外部 LLM for 讀書計畫、預測）
使用者（學⽣）互動觸發 → 前端事件 → 後端 API → pipeline/DB 更新 → 前端刷新呈現
4. API 邊界（interface）
4.1 認證
POST /api/auth/login
POST /api/auth/register
POST /api/auth/logout
GET /api/auth/me
4.2 題庫 / 查詢
GET /api/questions（篩選：年度、科目、主題、難度）
GET /api/questions/:id
POST /api/questions（管理）
PUT /api/questions/:id
DELETE /api/questions/:id
4.3 主題分析 / 頻率
GET /api/analytics/topic-frequency
GET /api/analytics/trend
GET /api/analytics/coverage
4.4 錯題追蹤
GET /api/mistakes
POST /api/mistakes
PUT /api/mistakes/:id
DELETE /api/mistakes/:id
GET /api/mistakes/weakness
4.5 讀書計畫
GET /api/study-plan（個人）
POST /api/study-plan/refresh
PUT /api/study-plan/:id
4.6 Pipeline / Job
POST /api/pipeline/ingest
POST /api/pipeline/reprocess
GET /api/pipeline/status
GET /api/pipeline/history
5. 資料流與控制流
5.1 資料流
raw items:
data_pipeline/collect ← Web/data sources
to clean:
data_pipeline/preprocess
to classify:
data_pipeline/classify
to store:
DB tables：questions、topics、analytics、mistakes、study_plans
用户查詢：
frontend → backend API → DB
使用者新增錯題：
frontend → backend → mistakes table
system update：
job -> recalculates analytics -> study_plans/predictions
5.2 控制流
入口：frontend/Cron/手動 job
核心 orchestrator：backend/job scheduler (e.g., Celery beat)
條件：
新資料到來 → 觸發 pipeline
讀書計畫需求 → API 一次計算或拉取快照
錯題更新 → 觸發弱點重算
失敗處理：retry、警報、狀態監控
6. 模組責任詳細（清單）
backend
服務 API
DB schema/ORM
核心邏輯（analytics + recommendation）
認證 + RBAC
job orchestrator
監控 + 日誌
frontend
UX/UI
單頁應用 SPA / PWA
API client + state 管理 (Redux/Vuex/Pinia)
資料視覺圖（圖表、heatmap、表格）
互動：錯題標記、賽道設定
data pipeline
ETL workflow
自動分類機器（NLP/指標）
資料驗證/品質檢查
事件/排程：更新、重算
外部 AI：生成計畫/預測
7. 後續實作 Phase（Execution Plan）
Phase 1：架構建置
建檔：ARCHITECTURE.md、README.md
初始 code scaffolding：
backend（FastAPI/Django/Nest）
frontend（React/Vue）
DB migration
data pipeline skeleton
API contracts
CI/CD 設定
Phase 2：資料與模型
實作 ETL
import 歷年題庫 test data
建構 classification/analytics pipeline
DB schema 完成
Phase 3：API + 前端 MVP
backend 基礎 CRUD + 認證
frontend dashboard 基本
錯題操作 + 主題分布
pipeline job 含手動觸發
Phase 4：強化 AI/預測
讀書計畫 generator
趨勢預測 API
使用者個人化調整
performance tuning
Phase 5：測試與部署
單元/整合測試
E2E（Cypress/TestCafe）
安全檢查（OWASP）
部署（Docker、K8S、CI pipeline）
8. 交付文件
ARCHITECTURE.md（本指引）
DESIGN.md（原始高階）
API_SPEC.md（後續）
data_schema.md
release_plan.md
task_board / OKR 展現