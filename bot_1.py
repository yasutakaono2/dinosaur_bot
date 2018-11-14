#need pillow,pyautogui,numpy
#from PIL import ImageGrab
import pyautogui
#import numpy as np
import time

class Cordinates():
    replayBtn = (332,382)
    dinasour = (176,388)

def restartGame():
    pyautogui.click(Cordinates.replayBtn)

def pressSpace():
    pyautogui.keyDown('space')
    time.sleep(0.05)
    print('Jump')
    pyautogui.keyUp('space') 

restartGame()
time.sleep(1)
pressSpace()