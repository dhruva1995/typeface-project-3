import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


def getCanny(grayImage, name):
    canny = cv.Canny(grayImage, 30, 100)

    mask = np.zeros(canny.shape, "uint8")

    for i in range(len(mask[0])):
        mask[0][i] = 255
        mask[-1][i] = 255

    for i in range(len(mask)):
        mask[i][0] = 255
        mask[i][-1] = 255

    canny = cv.bitwise_or(canny, mask)
    return canny


##########################################

image = cv.imread("images/2.png")

image = cv.bilateralFilter(image, 45, 45, 45)
img = image
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
# Split the image into separate channels
b, g, r = cv.split(image)

# b = cv.bilateralFilter(b, 30, 30, 30)
# g = cv.bilateralFilter(g, 30, 30, 30)
# r = cv.bilateralFilter(r, 30, 30, 30)

image1 = getCanny(b, "Blue")
image2 = getCanny(g, "Green")
image3 = getCanny(r, "Red")

canny = cv.bitwise_or(image1, image2)
canny = cv.bitwise_or(canny, image3)
# canny = cv.dilate(canny, (3, 3), 1, iterations=3)
# draw_contours(image, canny)

canny = cv.dilate(canny, (3, 3), iterations=1)
cv.imshow("Canny", canny)

marker_image = np.zeros_like(gray, dtype=np.int32)
marker_image[canny > 0] = 255
# marker_image = canny.astype(np.int32)
# # Distance transform
# dist_transform = cv.distanceTransform(canny, cv.DIST_L2, 3)

# # Marker generation
# _, markers = cv.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
# markers = cv.convertScaleAbs(markers)
# ####################################3

markers = cv.watershed(img, marker_image)
img[marker_image == -1] = [0, 0, 255]
img[marker_image > 0] = [255, 0, 0]
cv.imshow("final", img)
cv.waitKey(0)
cv.destroyAllWindows()
