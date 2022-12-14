
import time
import cv2 as cv
import win32gui
import win32ui
import win32con
import numpy as np
import wasd
import LookForSpace
import hardware
import LookForTargetFish

print('Start BDO AutoFish')

x = 4106 - 200
y = 468 - 200
w = 4595 - x + 400
h = 540 - y + 400

def doSPACE():

    while(True):
            
        result = LookForSpace.isSpaceSeen(x,y,w,h) 
        if(result):
            break
        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

    return True


def doCHECKFISH():
    #give time for fish screen to show
    time.sleep(1)
    return LookForTargetFish.isTargetSeen(x,y,w,h)

def doWASD():
    points = 0
    patternCache = ''
    while(True):
            
        pattern = wasd.wasd(x, y, w ,h)
        if (patternCache == pattern):
            points = points + 1
        else:
            points = 0
        
        if ((points > 100) & (pattern != None)):
            break

        patternCache = pattern
        print(points)

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

    return patternCache


def doWASD():
    points = 0
    patternCache = ''
    while(True):
            
        pattern = wasd.wasd(x, y, w ,h)
        if (patternCache == pattern):
            points = points + 1
        else:
            points = 0
        
        if ((points > 10) & (pattern != None)):
            break
        
        if (points == 100):
            break
        patternCache = pattern
        print(points)

        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

    return patternCache



while(True):
    doSPACE()
    time.sleep(1.25)
    hardware.pressKey("SPACE")
    print("SPACE")
    time.sleep(1.05)
    hardware.pressKey("SPACE")
    print("SPACE")
    cv.destroyAllWindows()
    
    #go do WASD
    pattern = doWASD()
    if (pattern == None):
        hardware.pressKey("SPACE")
        time.sleep(10)
        continue

    for l in pattern:
        hardware.pressKey(l)

    #check if fish is red
    if(doCHECKFISH()):
        time.sleep(5)
        hardware.pressKey("R")
        print("R")
    time.sleep(2)
    hardware.pressKey("SPACE")
    time.sleep(10)





