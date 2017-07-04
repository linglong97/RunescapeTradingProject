# This bot automatically pulls input from 
import os
import win32api
import subprocess
import sys
from pyautogui import typewrite, hotkey



itemstobuy = {}
paths = 'C:/'


def Runescape_buying_bot(itemstobuy):
    soon= input("If you want input your own file, type ?")
    if soon == '?':
        default_path = input("Input the name of the file:")
        subprocess.call([default_path])
    else:
        path = 'C:\Python27\Github\RunescapeTradingProject\OSBuddy64.exe'
        subprocess.call([path])
    try:
        sleep(15)
        typewrite('Noobies4life')
    except:
        pass
Runescape_buying_bot
    





# path_to_notepad = 'C:\\Windows\\System32\\notepad.exe'
# path_to_file = 'C:\\Users\\Desktop\\hello.txt'
# 
# subprocess.call([path_to_notepad, path_to_file])





