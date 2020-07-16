import keyboard
import pyautogui
import time
import tkinter

def getPosition():
    ss = pyautogui.screenshot()
    time.sleep(3)
    thePosition=pyautogui.position()
    colorRGB = ss.getpixel(thePosition)
    colorEntry.delete(0,end)
    colorEntry.insert(0, str(colorRGB))





