import os
from PySide6.QtCore import QCoreApplication

ZH_TW = {
    "Support Me!": "支持我！",
    "\"Support Me!\"": "\"支持我！\"",
    "GitHub Page": "GitHub 頁面",
    "REAL Video Enhancer": "REAL 影片增強器",
    "Start Time (seconds)": "開始時間（秒）",
    "End Time (seconds)": "結束時間（秒）",
    "Render Preview": "渲染預覽",
    "ETA:": "預計剩餘：",
    "FPS:": "幀率：",
    "STATUS:": "狀態：",
    "General": "一般",
    "Select Input File": "選擇輸入檔案",
    "Batch Select": "批次選擇",
    "Select Output Folder": "選擇輸出資料夾",
    "Open Output Folder": "開啟輸出資料夾",
    "Backend": "後端",
    "Interpolate": "補幀",
    "Interpolate Model": "補幀模型",
    "Interpolation Multiplier": "補幀倍率",
    "SloMo Mode": "慢動作模式",
    "Decompress": "解壓縮",
    "Decompress Model": "解壓縮模型",
    "Denoise": "去噪",
    "Denoise Model": "去噪模型",
    "Deblur": "去模糊",
    "Deblur Model": "去模糊模型",
    "Upscale": "超解析",
    "Upscale Model": "超解析模型",
    "Upscale Scale": "超解析倍率",
    " Add to Render Queue": " 加入渲染佇列",
    "Encoder Settings": "編碼器設定",
    "Video Encoder": "視訊編碼器",
    "Video Encoder Speed": "視訊編碼速度",
    "Video Quality": "視訊品質",
    "Video Container": "視訊容器",
    "Video Pixel Format": "視訊像素格式",
    "Audio Encoder": "音訊編碼器",
    "Audio Bitrate": "音訊位元率",
    "Subtiitle Encoder": "字幕編碼器",
    "Subtitle Encoder": "字幕編碼器",
    "Encoder Options": "編碼器選項",
    "Render Queue": "渲染佇列",
    "Advanced": "進階",
    "Logs": "日誌",
    "Output Settings": "輸出設定",
    "Render Settings": "渲染設定",
    "RVE Settings": "RVE 設定",
    "Backends": "後端管理",
    "Import Custom Upscale Model": "匯入自訂超解析模型",
    "Select Model (NCNN/.bin+.param)": "選擇模型 (NCNN/.bin+.param)",
    "Select Model (PyTorch/TensorRT/.pth)": "選擇模型 (PyTorch/TensorRT/.pth)",
    "Uninstall App": "解除安裝應用",
    "Your PC does not have enough storage for PyTorch/TensorRT. Please free up at least 15gb.": "您的電腦儲存空間不足以安裝 PyTorch/TensorRT，請至少釋放 15GB。",
    "PyTorch Version": "PyTorch 版本",
    "PyTorch Backend": "PyTorch 後端",
    "Output folder directory": "輸出資料夾路徑",
    "Scene Change Detection Enabled": "場景變化偵測已啟用",
    "Scene Change Detection Method": "場景變化偵測方式",
    "Scene Change Detection Threshold": "場景變化偵測閾值",
    "Auto Border Cropping": "自動邊框裁剪",
    "Precision": "精度",
    "TensorRT Optimization Level": "TensorRT 最佳化等級",
    "Auto HDR Mode": "自動 HDR 模式",
    "TensorRT Dynamic Engine": "TensorRT 動態引擎",
    "Interpolation UHD Mode": "插幀 UHD 模式",
    "NCNN GPU ID": "NCNN GPU ID",
    "PyTorch GPU ID": "PyTorch GPU ID",
    "Preview Enabled": "預覽已啟用",
    "Discord Rich Presence": "Discord 豐富狀態",
    "Tiling": "分塊",
    "Tile Size": "分塊大小",
    "Dynamic Scaled Flow (Pytorch Only)": "動態縮放光流（僅 PyTorch）",
    "Ensemble (Pytorch/TensorRT Only)": "集成（僅 PyTorch/TensorRT）",
    "Benchmark Mode": "基準測試模式",
    "Upscale/Restoration Tile Settings": "超解析/修復分塊設定",
    "Interpolate Settings": "補幀設定",
    "General Settings": "一般設定",
    "Finished Output Files:": "已完成輸出檔案：",
    "Open RVE Folder": "開啟 RVE 資料夾",
    "Reset Settings": "重設設定",
    "Install Recommended Dependencies": "安裝推薦依賴",
    "Select File": "選擇檔案",
    "Select Folder": "選擇資料夾",
    "Select Input Directory": "選擇輸入目錄",
    "Select Output Directory": "選擇輸出目錄",
    "Select PyTorch Model": "選擇 PyTorch 模型",
    "Select NCNN Bin": "選擇 NCNN Bin",
    "Select NCNN Param": "選擇 NCNN Param",
    "Video files (*.mp4 *.mov *.webm *.mkv);;All Files (*)": "視訊檔案 (*.mp4 *.mov *.webm *.mkv);;所有檔案 (*)",
    "PyTorch Model (*.pth *.safetensors)": "PyTorch 模型 (*.pth *.safetensors)",
    "NCNN Bin (*.bin)": "NCNN Bin (*.bin)",
    "All Files (*)": "所有檔案 (*)",
    "Language": "語言",
    "English": "English",
    "Traditional Chinese": "繁體中文",
    "fastest": "最快",
    "fast": "快",
    "medium": "中等",
    "slow": "慢",
    "placebo": "極慢",
    "Lossless": "無損",
    "Ultra": "超高",
    "Very_High": "極高",
    "High": "高",
    "Medium": "中等",
    "Low": "低",
    "yuv420p": "yuv420p",
    "yuv422p": "yuv422p",
    "yuv444p": "yuv444p",
    "yuv420p (10 bit)": "yuv420p (10 位元)",
    "yuv422p (10 bit)": "yuv422p (10 位元)",
    "yuv444p (10 bit)": "yuv444p (10 位元)",
    "copy_audio": "複製音訊",
    "aac": "aac",
    "libmp3lame": "libmp3lame",
    "opus": "opus",
    "copy_subtitle": "複製字幕",
    "ass": "ass",
    "srt": "srt",
    "webvtt": "webvtt",
    "auto": "自動",
    "float16": "float16",
    "float32": "float32",
    "mkv": "mkv",
    "mp4": "mp4",
    "mov": "mov",
    "webm": "webm",
    "avi": "avi",
    "Do you want to use simple installation?\n(Recommended for most users)": "是否使用簡易安裝？\n（推薦大多數使用者）",
    "Please install at least one backend to enable processing.": "請至少安裝一個後端以啟用處理。",
    "Welcome to REAL Video Enhancer!\nPlease install at least one backend to get started.": "歡迎使用 REAL 影片增強器！\n請至少安裝一個後端以開始使用。",
    "End time must be greater than start time!": "結束時間必須大於開始時間！",
    "Video is not loaded!": "尚未載入影片！",
    "Please select at least one model!": "請至少選擇一個模型！",
    "Unable to download scene detection model, please check your network and try again.": "無法下載場景偵測模型，請檢查網路後重試。",
    "Unable to download model, please check your network and try again.": "無法下載模型，請檢查網路後重試。",
    "Unable to add to render queue.\nModel can't be downloaded.\nPlease check your network and try again.": "無法加入渲染佇列。\n模型無法下載。\n請檢查網路後重試。",
    "Skipped (Already in queue):": "已跳過（已在佇列中）：",
    "Output file already in queue!": "輸出檔案已在佇列中！",
    "Added to queue!": "已加入佇列！",
    "Render queue is empty!": "渲染佇列為空！",
    "Please select a video file!": "請選擇視訊檔案！",
    "No valid videos found in the selected folder!": "在所選資料夾中未找到有效影片！",
    "Not a valid input!": "無效的輸入！",
    "Please select a model file!": "請選擇模型檔案！",
    "Model imported successfully!\nPlease restart the app for the changes to take effect.": "模型匯入成功！\n請重新啟動應用程式以使變更生效。",
    "Please select a bin file!": "請選擇 bin 檔案！",
    "Please select a param file!": "請選擇 param 檔案！",
    "Failed to import model!\nPlease try again.": "匯入模型失敗！\n請重試。",
    "Are you sure you want to exit?": "確定要退出嗎？",
    "No permissions to export here!": "此處無寫入權限！",
    "No permissions to export here!\nSetting default output folder to home directory.": "此處無寫入權限！\n將預設輸出資料夾設為家目錄。",
    "No videos folder\nSetting default output folder to home directory.": "無影片資料夾\n將預設輸出資料夾設為家目錄。",
    "Output files in render queue already exist, do you want to overwrite?": "渲染佇列中的輸出檔案已存在，是否要覆蓋？",
    "Rendering failed! Please check the logs tab!": "渲染失敗！請檢查日誌分頁！",
    "No Network Connection": "無網路連線",
    "Network is required for this action!\nPlease connect to a network.": "此操作需要網路！\n請連接網路。",
    "Downloading Python": "正在下載 Python",
    "Are you sure you want to uninstall?": "確定要解除安裝嗎？",
    "Download Complete\nPlease restart the application to apply changes.": "下載完成\n請重新啟動應用程式以套用變更。",
    "Download Failed!\nPlease check logs for more info.": "下載失敗！\n請查看日誌以獲取更多資訊。",
    "Please select a valid PyTorch version from the dropdown.": "請從下拉選單中選擇有效的 PyTorch 版本。",
    "No valid output file selected!": "未選擇有效的輸出檔案！",
    "Loaded ": "已載入 ",
    " videos.": " 個影片。",
    " videos": " 個影片",
    "Please install at least one backend to get started.": "請至少安裝一個後端以開始。",
    "Failed to import any backends!, please try to reinstall the app!": "無法匯入任何後端，請嘗試重新安裝應用！",
    "System Information:": "系統資訊：",
    "Software Information:": "軟體資訊：",
    "CUDA": "CUDA",
    "ROCm": "ROCm",
    "XPU": "XPU",
    # 下載頁面按鈕說明（效能描述）
    "NCNN Vulkan (All GPUs, slower inference, small download)": "NCNN Vulkan（所有 GPU，較慢推理，下載體積小）",
    "PyTorch (NVIDIA/CUDA, AMD/ROCm (Linux Only), INTEL/xpu, MacOS/MPS)": "PyTorch（NVIDIA/CUDA、AMD/ROCm（僅 Linux）、INTEL/xpu、MacOS/MPS）",
    "TensorRT (Nvidia RTX 20 series and up, fastest inference, largest download)": "TensorRT（Nvidia RTX 20 系列以上，推理最快，下載體積最大）",
    "DirectML - NOT IMPLEMENTED YET (All DirectX12 capable GPUs, faster inference, small download, Windows only)": "DirectML - 尚未實作（所有支援 DirectX12 的 GPU，推理較快，下載體積小，僅 Windows）",
    "mean": "平均值",
    "mean_segmented": "分段平均值",
    "pyscenedetect": "pyscenedetect",
    "sudo_scene_detect": "sudo_scene_detect",
    "Cancel": "取消",
    "Setting Up Backend": "正在設定後端",
    "Running Command": "正在執行指令",
    "Downloading: ": "正在下載：",
    "Process finished with return code ": "處理程序已完成，返回碼：",
    "Error in UpdateGUIThread: ": "UpdateGUIThread 錯誤：",
    "Error starting application: ": "啟動應用時發生錯誤：",
    "Building Engine, this may take a while.": "正在建構引擎，可能需要一段時間。",
    "Output video resolution not set.": "未設定輸出影片解析度。",
    "No render process!": "無渲染程序！",
    "FileExistsError! Using existing paused shared memory": "檔案已存在錯誤！使用現有的暫停共享記憶體",
    "UHD mode enabled": "已啟用 UHD 模式",
    "Language changed. Please restart the application to apply changes.": "語言已變更。請重新啟動應用程式以套用變更。",
    "Videos": "影片",
}

SUPPORTED_LANGUAGES = {
    "en": "English",
    "zh_TW": "繁體中文",
}

ZH_TW_REVERSE = {v: k for k, v in ZH_TW.items()}

_current_lang = "zh_TW"

def get_language():
    return _current_lang

def set_language(lang: str):
    global _current_lang
    if lang in SUPPORTED_LANGUAGES:
        _current_lang = lang

def tr(text: str) -> str:
    if _current_lang == "en" or not text:
        return text
    if text in ZH_TW:
        return ZH_TW[text]
    for k, v in ZH_TW.items():
        if text.startswith(k):
            return text.replace(k, v, 1)
        if k in text:
            pass
    return ZH_TW.get(text.strip(), text)

def tr_with_fallback(text: str) -> str:
    if text is None:
        return ""
    return tr(text)

def tr_format(text: str, *args, **kwargs) -> str:
    t = tr(text)
    try:
        return t.format(*args, **kwargs)
    except Exception:
        return t

def reverse_tr(text: str) -> str:
    if not text:
        return text
    if text in ZH_TW_REVERSE:
        return ZH_TW_REVERSE[text]
    return text

HTML_PHRASE_MAP = {
    "Renders a small portion of the video to show the results (most useful for upscaling)": "渲染影片的一小段以顯示結果（對超解析最有用）",
    "Increase video length instead of framerate when interpolating.": "補幀時增加影片長度而非幀率。",
    "Audio and Subtitles will not be transfered to output video.": "音訊與字幕將不會轉移到輸出影片。",
    "Custom output scale no matter the model. Will run AI on video frame once, and scale the image to match the multiplier. Useful for 4x models.": "無論模型為何皆可自訂輸出倍率。僅對影片幀執行一次 AI，再縮放至指定倍率，適合 4x 模型。",
    "Encoder command:": "編碼器指令：",
    "Encoder settings passed to FFMpeg, can be manually tweaked.": "傳遞給 FFmpeg 的編碼器參數，可手動調整。",
    "Encoder:": "編碼器：",
    "Compression algorithm for video, most common is libx264": "視訊壓縮演算法，最常見為 libx264",
    "Any encoder without a device label is a CPU encoder.": "任何未標示裝置的編碼器皆為 CPU 編碼器。",
    "Lossy Encoders:": "有損編碼器：",
    "Lossless Encoders:": "無損編碼器：",
    "Encoder Speed:": "編碼速度：",
    "Speed at which the encoder processes the video,": "編碼器處理影片的速度，",
    "Slower": "較慢",
    "Better results for the file size": "對檔案大小有更好的效果",
    "Changes the video container in the default output file generated container.": "變更預設輸出檔案的視訊容器。",
    "is recomended due to its extensive support for different formats.": "因支援多種格式而被推薦。",
    "WARNING: Changing this": "警告：變更此項",
    "MAY": "可能",
    "break encoder compadibility.": "會破壞編碼器相容性。",
    "Please look at the audio and video encoder tooltips for compadibility.": "請查看音訊與視訊編碼器的提示以確認相容性。",
    "Pixel Format": "像素格式",
    "Recommended": "推薦",
    "to use": "使用",
    "if the video container is": "若視訊容器為",
    "not mkv,": "非 mkv，",
    "or if the output video has audio isses.": "或輸出影片有音訊問題。",
    "Higher bitrate = higher quality": "較高位元率 = 較高品質",
    "Only applies to": "僅適用於",
    "and": "與",
    "All encoders here are": "此處所有編碼器皆為",
    "Text Only.": "僅文字。",
    "If you are enhancing a": "若您正在增強",
    "DVD,": "DVD，",
    "used": "用於",
    "Show REAL Video Enhancer in discord.": "在 Discord 中顯示 REAL 影片增強器。",
    "This is the version downloaded": "此為已下載的版本",
    "Supports older CUDA enabled GPUs": "支援較舊的 CUDA GPU",
    "Supports all RTX cards, faster and recomended.": "支援所有 RTX 顯示卡，更快且推薦。",
    "Experimental.": "實驗性。",
    "xpu: Intel: idk fam, dunno if this even works lowkey": "xpu：Intel：老實說不確定是否可用",
    "MPS: Apple Mac M series SOCs only.": "MPS：僅 Apple Mac M 系列晶片。",
    "Scene Change Detection": "場景變化偵測",
    "Resolution:": "解析度：",
    "Frame Count:": "幀數：",
    "Container:": "容器：",
    "Color Space:": "色彩空間：",
    "Is HDR:": "是否 HDR：",
    "Bit Depth:": "位元深度：",
    "Perform processing without outputting new video. This tests the raw performance of the inference.": "執行處理但不輸出新影片，用於測試推理的原始效能。",
    "Perform processing without outputing new video. This tests the raw performance of the inference.": "執行處理但不輸出新影片，用於測試推理的原始效能。",
    "Auto": "自動",
    "Defaults to float16 if the GPU is supported (RTX 20 series and up)": "若 GPU 支援則預設為 float16（RTX 20 系列以上）",
    "Float16": "Float16",
    "Faster inference and less VRAM usage.": "推理速度較快，VRAM 使用量較少。",
    "Float32": "Float32",
    "Slower inference and more VRAM usage, supported on more GPUS.": "推理速度較慢，VRAM 使用量較多，支援更多 GPU。",
    "Lower means less optimization, but faster engine generation time.": "較低表示較少最佳化，但引擎生成時間較快。",
    "Higher means more optimization, but slower engine generation time.": "較高表示較多最佳化，但引擎生成時間較慢。",
    "NCNN GPU ID -": "NCNN GPU ID -",
    "Sets what GPU is used for NCNN": "設定用於 NCNN 的 GPU",
    "PyTorch GPU ID -": "PyTorch GPU ID -",
    "Sets what GPU is used for PyTorch": "設定用於 PyTorch 的 GPU",
    "recomended": "recommended",
    "Split up processing upscaled frames into chunks.": "將放大的幀分割成區塊處理。",
    "Lowers VRAM usage, but also slows down render.": "降低 VRAM 使用量，但也會減慢渲染速度。",
    "Only use when render failes due to VRAM limits.": "僅在因 VRAM 限制導致渲染失敗時使用。",
    "Scales optical flow based on the difference between frames.": "根據幀之間的差異縮放光流。",
    "Helps with anime interpolation.": "有助於動畫補幀。",
    "Ensembles flow, can produce better results.": "集成光流，可產生更好的結果。",
    "Only compadible with older RIFE models and GMFSS": "僅相容於舊版 RIFE 模型和 GMFSS",
    "Enabled: Attempts to detect when scenes change in a video.": "啟用：嘗試偵測影片中的場景變化。",
    "When running an interpolation, it will avoide interpolating over these scene changes.": "執行補幀時，將避免在這些場景變化上進行補幀。",
    "mean (segmented): fast, prone to overdetection": "mean (segmented)：快速，容易過度偵測",
    "Lower number: higher chance of detecting scene changes, with risk of overdetection.": "較低數字：較高的場景變化偵測機率，但有過度偵測的風險。",
    "Higher number: lower chance of detecting scene changes, with risk of underdetection.": "較高數字：較低的場景變化偵測機率，但有偵測不足的風險。",
    "Will automatically remove black bars if they are present throughout a video, can increase performance.": "若整個影片有黑邊，將自動移除以提升效能。",
    "Auto enables HDR mode if RVE detects that the video that is being rendered is HDR.": "若 RVE 偵測到正在渲染的影片為 HDR，則自動啟用 HDR 模式。",
    "This will cause slower rendering if the video is HDR.": "若影片為 HDR，將導致渲染速度變慢。",
    "HDR is only color tested on x264 and x265 encoders.": "HDR 僅在 x264 和 x265 編碼器上經過色彩測試。",
    "The preview colors may be distorted as the preview itself is not HDR.": "預覽色彩可能會失真，因為預覽本身不是 HDR。",
    "Enables TensorRT to build for many different resolutions in one engine.": "讓 TensorRT 能在一個引擎中建立多種不同解析度。",
    "Saves VRAM and speeds up inference at resolutions above 1080p by calculating flow at a lower resolution. (GMFSS/GIMM)": "透過在較低解析度計算光流，節省 VRAM 並加速 1080p 以上的推理。(GMFSS/GIMM)",


    "Threshold": "閾值",
    "higher": "較高",
    "chance of detecting scene changes": "偵測場景變化的機率",
    "with risk of": "伴隨",
    "overdetection": "過度偵測",
    "lower": "較低",
    "underdetection": "偵測不足",
    "2-3 for real life, 4 for animation.": "真實影片 2-3，動畫 4。",
    "Defines how color information is stored for each pixel in a video frame.": "定義色彩資訊如何儲存在影片幀的每個像素中。",
    "yuv 420/422/444 p10le: 10 bit version of each.": "yuv 420/422/444 p10le：各格式的 10 位元版本。",
    "mkv is recommended due to its extensive support for different formats.": "mkv 因支援多種格式而被推薦。",
    "mkv is recomended due to its extensive support for different formats.": "mkv 因支援多種格式而被推薦。",

    "processing time means": "處理時間意味著",
    "containers only": "僅限容器",

    "yuv420p: Most common, removes the most information.": "yuv420p：最常見，移除最多資訊。",
    "yuv422p: In between 420p and 444p.": "yuv422p：介於 420p 和 444p 之間。",
    "yuv444p: Keeps the most information.": "yuv444p：保留最多資訊。",
    "MKV and MP4 containers only": "僅限 MKV 和 MP4 容器",

    "Pixel Format-": "像素格式 -",
    "Audio Encoder-": "音訊編碼器 -",
    "Recommended to use aac if the video container is not mkv, or if the output video has audio isses.": "若視訊容器非 mkv 或輸出影片有音訊問題，推薦使用 aac。",
    "copy_audio: No re-encoding is done on the output": "copy_audio：不對輸出重新編碼",
    "aac: Most common, and high quality.": "aac：最常見且高品質。",
    "libmp3lame: Used less, low quality.": "libmp3lame：較少使用，品質較低。",
    "opus: Used for webm.": "opus：用於 webm。",
    "Audio Bitrate-": "音訊位元率 -",
    "Only applies to aac and libmp3lame.": "僅適用於 aac 和 libmp3lame。",
    "Subtitle Encoder-": "字幕編碼器 -",
    "Recommended to use webvtt if the video container is not mkv, or if the output video has audio isses.": "若視訊容器非 mkv 或輸出影片有音訊問題，推薦使用 webvtt。",
    "All encoders here are Text Only.": "此處所有編碼器皆為僅文字。",
    "If you are enhancing a DVD, use copy_subtitle.": "若您正在增強 DVD，請使用 copy_subtitle。",
    "Scene Change Detection Enabled:-": "場景變化偵測已啟用 -",
    "Scene Change Detection Method-": "場景變化偵測方式 -",
    "mean: fastest, least accurate": "mean：最快，最不準確",
    "pyscenedetect: slow, accurate (Recommended)": "pyscenedetect：慢，準確（推薦）",
    "Scene Change Detection Threshold -": "場景變化偵測閾值 -",
    "Recommended: 2-3 for real life, 4 for animation.": "推薦：真實影片 2-3，動畫 4。",
    "Audo Border Cropping:-": "自動邊框裁剪 -",
    "Precision:": "精度：",
    "Auto: Defaults to float16 if the GPU is supported (RTX 20 series and up)": "自動：若 GPU 支援則預設為 float16（RTX 20 系列以上）",
    "Float16: Faster inference and less VRAM usage.": "Float16：推理速度較快，VRAM 使用量較少。",
    "Float32: Slower inference and more VRAM usage, supported on more GPUS.": "Float32：推理速度較慢，VRAM 使用量較多，支援更多 GPU。",
    "TensorRT Optimization Level:-": "TensorRT 最佳化等級 -",
    "Auto HDR Mode-": "自動 HDR 模式 -",
    "TensorRT Dynamic Engine:-": "TensorRT 動態引擎 -",
    "PyTorch Version-": "PyTorch 版本 -",
    "2.6: Supports older CUDA enabled GPUs": "2.6：支援較舊的 CUDA GPU",
    "2.8: Supports all RTX cards, faster and recomended.": "2.8：支援所有 RTX 顯示卡，更快且推薦。",
    "2.9: Experimental.": "2.9：實驗性。",
    "PyTorch Backend-": "PyTorch 後端 -",
    "CUDA: NVIDIA GPUs 10 series and up": "CUDA：NVIDIA GPU 10 系列以上",
    "ROCm: AMD (Linux Only) 7000 series(maybe) and up": "ROCm：AMD（僅 Linux）7000 系列（可能）以上",
    "Render Preview:": "渲染預覽：",
    "Upscale Scale:": "超解析倍率：",
    "Slower processing time means": "較慢的處理時間意味著",
    "Better results for the file size.": "對檔案大小有更好的效果。",
}

_original_translate = QCoreApplication.translate

def _patched_translate(context, sourceText, disambiguation=None, n=-1):
    import sys
    import re
    if _current_lang != "en" and sourceText:
        if sourceText in ZH_TW:
            result = ZH_TW[sourceText]
            return result
        # Check for HTML content - strip tags for matching
        if "<html>" in sourceText or "<span" in sourceText or "<p>" in sourceText:
            text_only = re.sub(r'<[^>]+>', ' ', sourceText)
            text_only = re.sub(r'\s+', ' ', text_only).strip()
            all_phrases = list(HTML_PHRASE_MAP.items()) + [(k, v) for k, v in ZH_TW.items() if k not in HTML_PHRASE_MAP]
            sorted_phrases = sorted(all_phrases, key=lambda x: len(x[0]), reverse=True)
            # Strip HTML tags, replace phrases in plain text, return plain text
            text_only = re.sub(r'<[^>]+>', '', sourceText)
            original = text_only
            for en_phrase, zh_phrase in sorted_phrases:
                if en_phrase in text_only:
                    text_only = text_only.replace(en_phrase, zh_phrase)
            if text_only != original:
                return text_only
        # Partial match in ZH_TW
        for en_phrase, zh_phrase in ZH_TW.items():
            if en_phrase in sourceText and en_phrase != sourceText:
                return sourceText.replace(en_phrase, zh_phrase)
    try:
        return _original_translate(context, sourceText, disambiguation, n)
    except Exception:
        return sourceText

QCoreApplication.translate = _patched_translate

try:
    from PySide6.QtWidgets import QMessageBox, QFileDialog
    _orig_qmsg_question = QMessageBox.question
    def _patched_qmsg_question(*args, **kwargs):
        if len(args) >= 3 and isinstance(args[2], str):
            args = list(args)
            args[2] = tr(args[2])
            args = tuple(args)
        if len(args) >= 2 and isinstance(args[1], str):
            args = list(args)
            args[1] = tr(args[1])
            args = tuple(args)
        if "text" in kwargs and isinstance(kwargs["text"], str):
            kwargs["text"] = tr(kwargs["text"])
        if "title" in kwargs and isinstance(kwargs["title"], str):
            kwargs["title"] = tr(kwargs["title"])
        return _orig_qmsg_question(*args, **kwargs)
    QMessageBox.question = _patched_qmsg_question
    _orig_qmsg_warning = QMessageBox.warning
    def _patched_qmsg_warning(*args, **kwargs):
        if len(args) >= 3 and isinstance(args[2], str):
            args = list(args)
            args[2] = tr(args[2])
            args = tuple(args)
        return _orig_qmsg_warning(*args, **kwargs)
    QMessageBox.warning = _patched_qmsg_warning
    _orig_getOpen = QFileDialog.getOpenFileName
    def _patched_getOpen(*args, **kwargs):
        if "filter" in kwargs and isinstance(kwargs["filter"], str):
            f = kwargs["filter"]
            if f in ZH_TW:
                kwargs["filter"] = ZH_TW[f]
            elif "Video files" in f:
                kwargs["filter"] = f.replace("Video files", "視訊檔案").replace("All Files", "所有檔案")
            elif "PyTorch Model" in f:
                kwargs["filter"] = f.replace("PyTorch Model", "PyTorch 模型")
        if len(args) >= 4 and isinstance(args[3], str):
            f = args[3]
            if f in ZH_TW:
                args = list(args)
                args[3] = ZH_TW[f]
                args = tuple(args)
            elif "Video files" in f:
                args = list(args)
                args[3] = f.replace("Video files", "視訊檔案").replace("All Files", "所有檔案")
                args = tuple(args)
        if len(args) >= 3 and isinstance(args[2], str):
            args = list(args)
            args[2] = tr(args[2])
            args = tuple(args)
        if "caption" in kwargs and isinstance(kwargs["caption"], str):
            kwargs["caption"] = tr(kwargs["caption"])
        return _orig_getOpen(*args, **kwargs)
    QFileDialog.getOpenFileName = _patched_getOpen
    _orig_getDir = QFileDialog.getExistingDirectory
    def _patched_getDir(*args, **kwargs):
        if len(args) >= 2 and isinstance(args[1], str):
            args = list(args)
            args[1] = tr(args[1])
            args = tuple(args)
        if "caption" in kwargs and isinstance(kwargs["caption"], str):
            kwargs["caption"] = tr(kwargs["caption"])
        return _orig_getDir(*args, **kwargs)
    QFileDialog.getExistingDirectory = _patched_getDir
except Exception:
    pass

def load_language_from_settings():
    try:
        import os
        from .constants import CWD
        from .Util import currentDirectory
        try:
            base = currentDirectory()
        except Exception:
            base = CWD
        settings_path = os.path.join(base, "settings.txt")
        if os.path.isfile(settings_path):
            with open(settings_path, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("language,"):
                        lang = line.strip().split(",", 1)[1].strip()
                        if lang in SUPPORTED_LANGUAGES:
                            set_language(lang)
                        break
    except Exception:
        pass
