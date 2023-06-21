import cv2 as cv
import numpy as np


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

    # cv.imshow(f"Canny {name}", canny)
    return canny


def getContour(grayImage, name):
    canny = getCanny(grayImage, name)

    contours, _ = cv.findContours(canny, cv.RETR_CCOMP, cv.CHAIN_APPROX_SIMPLE)

    contours = sorted(contours, key=cv.contourArea, reverse=True)

    top_contours = contours[1:10]

    # largest_contour = contours[1:2]
    # contour_points = np.squeeze(largest_contour)
    # # Find the minimum area rectangle that bounds the contour
    # rect = cv.minAreaRect(contour_points)
    # box = cv.boxPoints(rect)
    # box = np.int0(box)

    # Draw the maximum rectangle on the image
    # cv.drawContours(img, [box], 0, (0, 255, 0), 2)

    # Select the contour(s) that best represent the surface
    image = np.zeros(grayImage.shape, "uint8")
    image = cv.drawContours(image, top_contours, -1, (255, 0, 0), -1)
    # cv.imshow(name, blank)

    # filtered_contours = [cnt for cnt in contours[1:] if cv.contourArea(cnt) > 100]

    return image


def canyToConTour(cany):
    pass


def draw_contours(image, canny):
    contours, _ = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
    # result = np.zeros_like(canny)
    result = np.zeros(image.shape, "uint8")

    contours = [cnt for cnt in contours if cv.contourArea(cnt) > 1000]
    contours = sorted(contours, key=cv.contourArea, reverse=True)
    result = cv.drawContours(result, contours, -1, (255), -1)

    # result = cv.bitwise_not(result)

    cv.imshow("Contours", result)
    cv.waitKey()
    cv.destroyAllWindows()


image = cv.imread("images/5.png")

image = cv.bilateralFilter(image, 45, 45, 45)

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
markers = cv.dilate(canny, None)
cv.imshow("Canny", canny)

markers = markers.astype(np.int32)

cv.watershed(image, markers)
image[markers == -1] = [0, 0, 255]  # Mark watershed boundaries with red color

# Display the result
cv.imshow("Segmented Image", image)
cv.waitKey(0)
cv.destroyAllWindows()
