import windowcapture
import cv2 as cv
import numpy as np


findme_space_img = cv.imread('space.png', cv.IMREAD_GRAYSCALE)

def isSpaceSeen(x,y,w,h):
    screenshot_colored = windowcapture.window_capture(x,y,w,h)
    screenshot = cv.cvtColor(screenshot_colored, cv.COLOR_BGR2GRAY)

    result = cv.matchTemplate(screenshot, findme_space_img, cv.TM_CCOEFF_NORMED)

    threshold = 0.70
    # get the best match position
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    locations = np.where(result >= threshold)
    #some redimensioning array
    locations = list(zip(*locations[::-1]))

    if (max_val >= threshold):
        return locations

    if locations:                
        for loc in locations:
            #get dimensions
            find_w = findme_space_img.shape[1]
            find_h = findme_space_img.shape[0]
            top_left = loc
            bottom_right =  (top_left[0] + find_w, top_left[1] + find_h)

            #draw                    
            cv.rectangle(screenshot_colored, top_left, bottom_right, color=(255,0,0), thickness = 2, lineType = cv.LINE_4)
            cv.imshow("see", screenshot_colored)
            return True

    cv.imshow("see", screenshot_colored)

    return False


