# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['client.py'],
             pathex=['/home/chirag/Documents/reverse_shell/ClientSide'],
             binaries=[],
             datas=[ ("./pyaudio.py","."), ("./_portaudio.cpython-38-x86_64-linux-gnu.so",".") ],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='client',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )
