from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con

while 1:
    if pyautogui.locateOnScreen('Ulti-on.png', grayscale=True, confidence=0.8) != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)