import pynput
import time
from pyautogui import * 
import pyautogui 
import time 
import keyboard 
import random
import win32api, win32con
import pynput
import time

from playsound import playsound

mouse = pynput.mouse.Controller()
keyboard = pynput.keyboard.Controller()

position = []
beforeBotting = []

print("Gzdingty - Empath bot")
print("Usage: Ask a friend")

def UltiHero(x,y):
    while True:
        if pyautogui.locateOnScreen('Ulti-on.png', grayscale=True, confidence=0.8) != None:
            print("I can see it")
            time.sleep(0.5)
        elif pyautogui.locateOnScreen('Ulti-off.png', grayscale=True, confidence=0.8) != None:
            keyboard.press('r')
            keyboard.release('r')
            time.sleep(0.1)
            beforeBotting.append(mouse.position[0])
            beforeBotting.append(mouse.position[1])
            mouse.position = (x,y)
            mouse.press(pynput.mouse.Button.left)
            mouse.release(pynput.mouse.Button.left)
            mouse.position = (beforeBotting[0], beforeBotting[1])
            beforeBotting.pop()
            beforeBotting.pop()
            print("I am unable to see it")
            time.sleep(0.5)

def on_click(x, y, button, pressed):
    print('{0} at {1}'.format(
        'Pressed' if pressed else 'Released',
        (x, y)))
    position.append(x)
    position.append(y)
    return False

def on_release(key):
    print('{0} release'.format(
        key))
    if key == pynput.keyboard.Key.esc:
        # Stop listener
        return False

#with pynput.mouse.Listener(on_click=on_click) as listener:
#    listener.join()

#UltiHero(position[0], position[1])

def LookForEnemy():
    while True:
        enemyLocation = pyautogui.locateOnScreen('enemyHealthBar.png', confidence=0.9)
        if enemyLocation != None:
            mouse.position = (enemyLocation[0]+50, enemyLocation[1]+100)
            mouse.press(pynput.mouse.Button.x2)
            time.sleep(0.05)
            mouse.release(pynput.mouse.Button.x2)
            mouse.press(pynput.mouse.Button.left)
            time.sleep(0.05)
            mouse.release(pynput.mouse.Button.left)
            print("I can see it")
            playsound('snap.wav')
            time.sleep(0.1)
     

LookForEnemy()