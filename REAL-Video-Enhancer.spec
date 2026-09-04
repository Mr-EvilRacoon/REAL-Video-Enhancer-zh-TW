# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['REAL-Video-Enhancer.py'],
    pathex=[],
    binaries=[],
    datas=[('src', 'src')],
    hiddenimports=['src.i18n', 'src.Util', 'src.constants', 'src.ModelHandler', 'src.Backendhandler', 'src.version', 'src.VideoInfo', 'src.DownloadDeps', 'src.DownloadModels', 'src.GenerateFFMpegCommand', 'src.DiscordRPC', 'src.BuiltInTorchVersions', 'src.ui'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='REAL-Video-Enhancer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icons\\logo-v2.ico'],
)
coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name='REAL-Video-Enhancer',
)
