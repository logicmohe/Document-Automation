import os
import sys
import codecs
import pyautogui
from docx import Document
from docx.shared import Inches
from win32com import client as wc

#Get Position of Current Cursor
# >>> import pyautogui
# >>> pyautogui.position()
# (845, 554)
#Resolution
#pyautogui.size()

#Select Right doucument: 
pyautogui.click(x=1256, y=21)
pyautogui.hotkey('ctrl','a')
os.system("PAUSE")
