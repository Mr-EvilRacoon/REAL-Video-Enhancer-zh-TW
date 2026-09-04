# REAL Video Enhancer 繁體中文非官方版

> **免責聲明**：本專案是 REAL Video Enhancer 的**非官方繁體中文本地化版本**，並非由 TNTwise 官方發布或維護。原始專案請參考 [TNTwise/REAL-Video-Enhancer](https://github.com/TNTwise/REAL-Video-Enhancer)。

---

## 關於本專案

本專案基於 [REAL Video-Enhancer](https://github.com/TNTwise/REAL-Video-Enhancer) 進行繁體中文化修改，旨在為台灣及繁體中文使用者提供更友善的操作介面。

### 主要修改項目

- **GUI 介面繁體中文化**：將選單、按鈕、對話方塊、工具提示（tooltips）等使用者可見文字翻譯為繁體中文
- **新增語言切換功能**：可於設定中切換繁體中文 / English
- **保留英文專有名詞**：技術術語如 `yuv420p`、`HDR`、`TensorRT`、`NCNN`、`PyTorch`、`CUDA`、`ROCm` 等維持原文
- **修復拼字錯誤**：修正原專案中 `recomended` → `recommended`、`compadibility` → `compatibility` 等錯誤

### 翻譯協作

繁體中文翻譯初步由 **Hermes Agent（LongCat 2.0 模型）** 協助產生，由 **Mr-EvilRacoon** 整合、檢查、建置與發布。

### 測試狀態

- ✅ Windows 11 x64 測試通過
- ✅ NCNN Vulkan 後端測試通過（AMD GPU）
- ✅ 語言切換功能測試通過
- ⚠️ 資訊卡工具提示仍需使用者反饋（部分複雜 HTML 標籤可能尚未完美呈現）

### 已知限制

- 本版本僅支援 Windows 平台（PyInstaller 打包）
- Linux / macOS 版本需自行使用 `cx_Freeze` 或 `Nuitka` 打包
- 部分翻譯可能不盡完善，歡迎透過 Issues 回報

### 安全提醒

- 本程式會下載 Python 執行檔與 AI 模型權重檔
- 建議僅從本倉庫的 Releases 頁面下載，勿從不明來源取得
- 安裝時需管理員權限（寫入登錄程式與開始選單）

---

## 授權條款

本專案採用與原始專案相同的 **[GNU Affero General Public License v3.0](LICENSE)** 發布。

完整授權內容請見 [LICENSE](LICENSE) 檔案。

---

## 下載與安裝

### 安裝版

1. 前往 [Releases](../../releases) 頁面
2. 下載 `REAL-Video-Enhancer-2.4.1-zh-TW-Windows-Setup_x86_64.exe`
3. 執行安裝程式，依照指示完成安裝
4. 安裝後可從開始選單或桌面捷徑啟動

### 可攜版

1. 下載 `REAL-Video-Enhancer-2.4.1-zh-TW-Windows-Portable.zip`
2. 解壓縮到任意資料夾
3. 直接執行 `REAL-Video-Enhancer.exe`

### 系統需求

- Windows 10/11 64-bit
- 建議至少 16GB RAM（依模型與影片解析度而定）
- 支援 NCNN Vulkan / PyTorch CUDA / TensorRT 的 GPU

---

## 建構說明

若您想自行從原始碼建構：

```
# 1. 複製倉庫
git clone https://github.com/Mr-EvilRacoon/REAL-Video-Enhancer-zh-TW.git
cd REAL-Video-Enhancer-zh-TW

# 2. 建立 Python 3.12 虛擬環境
python -m venv venv312
venv312\Scripts\activate

# 3. 安裝依賴
pip install -r requirements.txt

# 4. 使用 PyInstaller 打包
python build.py --build pyinstaller --copy_backend

# 5. 輸出資料夾
# dist/REAL-Video-Enhancer/

# 6. 建立安裝程式（需要 NSIS）
"C:\Program Files (x86)\NSIS\makensis.exe" installer.nsi

# 7. 輸出檔案
# REAL-Video-Enhancer-2.4.1-zh-TW-Windows-Setup_x86_64.exe
```

---

## 支援原始作者

如果您喜歡 REAL Video Enhancer，請支持原始作者 TNTwise：

- [Steam](https://store.steampowered.com/app/4087640/)
- [Ko-Fi](https://ko-fi.com/tntwise)
- [Discord](https://discord.gg/hwGHXga8ck)
- [GitHub](https://github.com/TNTwise/REAL-Video-Enhancer)

---

## 問題回報

如發現翻譯錯誤或有改進建議，請透過 [Issues](../../issues) 回報。

---

## 致謝

- **TNTwise** — 原始專案開發者與所有上游貢獻者
- **Hermes Agent (LongCat 2.0)** — 繁體中文翻譯協作
- **RVE 社群** — 持續支持與反饋
