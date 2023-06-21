import cv2 as cv
import numpy as np


img = cv.imread("images/4.png")
blank = np.zeros(img.shape, dtype="uint8")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blur = gray.copy()

# cv.GaussianBlur(gray, (7, 7), cv.BORDER_DEFAULT)
# blur = cv.medianBlur(gray, 5)
# Bilateral filtering
blur = cv.bilateralFilter(img, 60, 60, 60)
cv.imshow("Blur", blur)

canny = cv.Canny(
    blur,
    70,
    100,
)
cv.imshow("Canny", canny)

contours, hierarchies = cv.findContours(canny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)

cv.drawContours(blank, contours, -1, (0, 255, 0), -1)
cv.imshow("Contour", blank)

print(len(contours))

cv.waitKey()
