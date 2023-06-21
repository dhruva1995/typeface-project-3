import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), "uint8")
# fill a color
# blank[:] = 255, 0, 255
# blank[200:400, 150:350] = 127, 0, 127
# cv.imshow("Purple", blank)
# draw rectangle
# cv.rectangle(blank, (0, 0, 200, 290), (0, 255, 0), -1)
# cv.imshow("rect", blank)
cv.circle(blank, (250, 250), 100, (0, 0, 200), thickness=cv.FILLED)
cv.imshow("circle", blank)
cv.waitKey(0)
