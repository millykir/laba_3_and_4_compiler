# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['vin.py'],
    pathex=[],
    binaries=[],
    datas=[('icons1', 'icons1'), ('txt\\classification.html', 'txt'), ('txt\\classification.txt', 'txt'), ('txt\\cod.txt', 'txt'), ('txt\\diagnostics.txt', 'txt'), ('txt\\grammar.txt', 'txt'), ('txt\\literature.txt', 'txt'), ('txt\\task.txt', 'txt'), ('txt\\analysis.png', 'txt'), ('txt\\test.html', 'txt')],
    hiddenimports=['docx', 'docx.opc.constants', 'docx.oxml', 'PIL.ImageTk'],
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
    a.binaries,
    a.datas,
    [],
    name='vin',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
