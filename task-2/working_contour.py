import cv2 as cv
import numpy as np


img = cv.imread("images/3.png")
blank = np.zeros(img.shape, dtype="uint8")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


blur = gray.copy()

# cv.GaussianBlur(gray, (3, 3), cv.BORDER_DEFAULT)
# blur = cv.medianBlur(gray, 3)
# Bilateral filtering
# blur = cv.bilateralFilter(gray, 60, 60, 60)
cv.imshow("Blur", blur)

canny = cv.Canny(blur, 10, 30, apertureSize=3)

cv.imshow("Canny", canny)

mask = np.zeros(canny.shape, "uint8")

for i in range(len(mask[0])):
    mask[0][i] = 255
    mask[-1][i] = 255

for i in range(len(mask)):
    mask[i][0] = 255
    mask[i][-1] = 255

canny = cv.bitwise_or(canny, mask)

contours, hierarchies = cv.findContours(canny, cv.RETR_CCOMP, cv.CHAIN_APPROX_NONE)

# filtered_contours = [cnt for cnt in contours if cv.contourArea(cnt) > 100]

contours = sorted(contours, key=cv.contourArea, reverse=True)

top_contours = contours[1:3]


# largest_contour = contours[1:2]
# contour_points = np.squeeze(largest_contour)
# # Find the minimum area rectangle that bounds the contour
# rect = cv.minAreaRect(contour_points)
# box = cv.boxPoints(rect)
# box = np.int0(box)

# Draw the maximum rectangle on the image
# cv.drawContours(img, [box], 0, (0, 255, 0), 2)


# Select the contour(s) that best represent the surface
detected_image = cv.drawContours(
    img.copy(), top_contours, -1, ((0, 255, 0), (255, 0, 0)), -1
)


cv.imshow("Contour", img)

print(len(contours))

cv.waitKey()
