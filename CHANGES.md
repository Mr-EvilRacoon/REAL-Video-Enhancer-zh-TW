# 修改日誌

## [v2.4.1-zh-TW] - 2026-09-03

### 新增功能

- **GUI 繁體中文化**：將使用者可見的 GUI 介面（選單、按鈕、標籤、對話方塊、工具提示等）翻譯為繁體中文
- **語言切換功能**：新增「語言」設定選項，可於執行時切換繁體中文 / English
- **技術術語保留**：英文專有名詞（yuv420p、HDR、TensorRT、NCNN、PyTorch、CUDA、ROCm、DLSS、FSR 等）維持原文
- **i18n 翻譯系統**：新增 `src/i18n.py`，包含 `ZH_TW` 字典（一般翻譯）和 `HTML_PHRASE_MAP` 字典（HTML 工具提示翻譯）

### 修復項目

- **#251 可攜版無法啟動**：加入 tar.gz 例外處理、損壞自動清理、下載重試機制（最多 3 次，指數退避）
- **#241 字體問題**：將 `QTcustom.py` 中的 `QFont("Arial", 20)` 改為 `QFontDatabase.systemFont(QFontDatabase.FixedFont)`，確保跨平台字型一致性
- **#205 安裝路徑**：NSIS 安裝頁面已包含 `MUI_PAGE_DIRECTORY`，使用者可選擇安裝路徑
- **安全修補**：`Backendhandler.py` 改用 `ast.literal_eval()` 避免程式碼注入；`i18n.py` 移除 debug 檔案寫入；`RenderQueue.py` 初始化 `self._upscaleModel`

### 技術修改

- **打包設定**：修正 `build.py`，加入 `--add-data "src;src"` 和 `--hidden-import` 確保所有 `src/` 模組正確打包
- **命令列解析**：修正 `build.py` 使用 `shlex.split()` 安全分割命令字串
- **Python 版本**：確認使用 Python 3.12 進行打包（`python312.dll`）

### 已知問題

- 本版本僅支援 Windows 平台（PyInstaller 打包）
- Linux / macOS 版本需自行使用 `cx_Freeze` 或 `Nuitka` 打包

---

## 上游更新日誌

請參考 [TNTwise/REAL-Video-Enhancer](https://github.com/TNTwise/REAL-Video-Enhancer) 的官方更新日誌。

本繁體中文版的基準版本為 v2.4.1（commit SHA：`8541c46ca14e6f84fc86c5b9d3b75373e2573245`）。
