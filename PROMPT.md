## Phase 1 檢查（Checkpoint Review）

### 檢查結果
- Backend 結構符合 architecture 設計
- router / service / model 分層清楚
- 未超出 Phase 1 範圍

### 發現問題
1. 尚未定義依賴（缺少 requirements.txt）
2. auth endpoint 設計仍為 mock（token 處理未完善）
3. model 時間欄位缺少預設值

### 決策
目前不進行修改，先維持 Phase 1 skeleton
後續視需求進行最小修正
## Phase 1 微修正（Minimal Fixes）

### 目的
根據 checkpoint review，僅進行 Phase 1 範圍內的小幅修正，不擴展到 Phase 2。

### Roo Code 執行內容
- 新增 `requirements.txt`
- 在 auth 相關檔案加入 TODO 註解，說明目前為 mock，未來應改為 JWT / token-based authentication
- 在 `models/entities.py` 補上 `created_at` / `updated_at` 的預設值或註記

### 結果
- 修正內容仍屬於 Phase 1
- 沒有新增 frontend 或 data pipeline
- 沒有改變原本架構