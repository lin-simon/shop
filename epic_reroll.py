from time import sleep
import mouse
import pynput
import pyautogui
mouse = pynput.mouse.Controller()

def search():

    mystic = pyautogui.locateOnScreen('Assets/mystic_banner.png',confidence=0.88)
    covenant = pyautogui.locateOnScreen('Assets/covenant_banner.png',confidence=0.9)
    if (mystic):
        left,top,width,height = mystic
        pyautogui.leftClick(left+width-50,top+height-30)
        sleep(0.4)
        buy()

    if (covenant):
        left,top,width,height = covenant
        pyautogui.leftClick(left+width-50,top+height-30)
        sleep(0.4)
        buy()

def scroll():
    mouse.scroll(0,-100)

def refresh():
    pyautogui.doubleClick(346, 943)
    pyautogui.doubleClick(346, 943)
    sleep(0.3)
    pyautogui.doubleClick(1094, 645)
    pyautogui.doubleClick(1094, 645)

def buy():
    pyautogui.leftClick(1062,730)

while(True):
    search()
    sleep(0.2)
    scroll()
    sleep(0.2)
    search()
    sleep(0.2)
    refresh()
    sleep(1)
    