import windowcapture
import cv2 as cv
import numpy as np

findme_W_img = cv.imread('W.png', cv.IMREAD_GRAYSCALE)
findme_A_img = cv.imread('A.png', cv.IMREAD_GRAYSCALE)
findme_S_img = cv.imread('S.png', cv.IMREAD_GRAYSCALE)
findme_D_img = cv.imread('D.png', cv.IMREAD_GRAYSCALE)

def findLetter(screenshot, findme_img):
    result = cv.matchTemplate(screenshot, findme_img, cv.TM_CCOEFF_NORMED)

    threshold = 0.80
    # get the best match position
    min_val, max_val, min_loc, max_loc = cv.minMaxLoc(result)

    locations = np.where(result >= threshold)
    #some redimensioning array
    locations = list(zip(*locations[::-1]))

    if (max_val >= threshold):
        return locations
    
    return None

def wasd(x,y,w,h):

    finalValuesLocations = []
    finalSequence = None

    screenshot_colored = windowcapture.window_capture(x,y,w,h)
    screenshot = cv.cvtColor(screenshot_colored, cv.COLOR_BGR2GRAY)

    wasd = ['W', 'A', 'S', 'D']

    for letter in wasd:

        if letter == 'W':
            findme_img = findme_W_img
            locations = findLetter(screenshot, findme_img)

            if locations:                
                for loc in locations:
                    #get dimensions
                    find_w = findme_img.shape[1]
                    find_h = findme_img.shape[0]
                    top_left = loc
                    bottom_right =  (top_left[0] + find_w, top_left[1] + find_h)

                    #draw                    
                    cv.rectangle(screenshot_colored, top_left, bottom_right, color=(255,0,0), thickness = 2, lineType = cv.LINE_4)

                    #add loc
                    finalValuesLocations.append(('W', top_left[0], bottom_right[0]))

        if letter == 'A':
            findme_img = findme_A_img
            locations = findLetter(screenshot, findme_img)

            if locations:                
                for loc in locations:
                    #get dimensions
                    find_w = findme_img.shape[1]
                    find_h = findme_img.shape[0]
                    top_left = loc
                    bottom_right =  (top_left[0] + find_w, top_left[1] + find_h)

                    #draw                    
                    cv.rectangle(screenshot_colored, top_left, bottom_right, color=(0,255,0), thickness = 2, lineType = cv.LINE_4)

                    #add loc
                    finalValuesLocations.append(('A', top_left[0], bottom_right[0]))
        
        if letter == 'S':
            findme_img = findme_S_img
            locations = findLetter(screenshot, findme_img)

            if locations:                
                for loc in locations:
                    #get dimensions
                    find_w = findme_img.shape[1]
                    find_h = findme_img.shape[0]
                    top_left = loc
                    bottom_right =  (top_left[0] + find_w, top_left[1] + find_h)

                    #draw                    
                    cv.rectangle(screenshot_colored, top_left, bottom_right, color=(0,0,255), thickness = 2, lineType = cv.LINE_4)

                    #add loc
                    finalValuesLocations.append(('S', top_left[0], bottom_right[0]))

        if letter == 'D':
            findme_img = findme_D_img
            locations = findLetter(screenshot, findme_img)

            if locations:                
                for loc in locations:
                    #get dimensions
                    find_w = findme_img.shape[1]
                    find_h = findme_img.shape[0]
                    top_left = loc
                    bottom_right =  (top_left[0] + find_w, top_left[1] + find_h)

                    #draw                    
                    cv.rectangle(screenshot_colored, top_left, bottom_right, color=(255,255,255), thickness = 2, lineType = cv.LINE_4)

                    #add loc
                    finalValuesLocations.append(('D', top_left[0], bottom_right[0]))

    if len(finalValuesLocations) > 0:
        orderedValues = sorted(
        finalValuesLocations, 
        key=lambda x: x[1]
        )

        offset = orderedValues[0][1]
        #print(orderedValues)
        finalSequence = ''
        #get prompt screen width
        cell_w = (orderedValues[-1:][0][2] - orderedValues[0][1]) / 10
        cell_w = int(cell_w)
        for x in range(1, 11):
            cell_letter = ''
            for val in orderedValues:
                if (val[1] >= ((x-1)*cell_w) + offset ) & (val[1] < ((x)*cell_w) + offset):
                    cell_letter = val[0]
                    break

            finalSequence = finalSequence + cell_letter

    cv.imshow("see", screenshot_colored)

    return finalSequence


