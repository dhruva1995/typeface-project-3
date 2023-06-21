import os
import cv2 as cv

# img = cv.imread("images/2.png")
# cv.imshow("Color", img)
# # Gray scale image
# gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
# cv.imshow("Gray", gray)

# # Blur image
# blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
# cv.imshow("Blur", blur)
# # Edge bit mask
# canny = cv.Canny(blur, 50, 180)
# cv.imshow("Canny", canny)
# cv.waitKey(0)

# resizing the images
# resized = cv.resize(img, (600, 500), interpolation=cv.INTER_CUBIC)

# show all images
for i in range(1, 5):
    img = cv.imread(f"images/{i}.png")
    cv.imshow("original", img)
    blurred = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)
    canny = cv.Canny(blurred, 30, 150)
    cv.imshow("edges", canny)
    cv.waitKey()
