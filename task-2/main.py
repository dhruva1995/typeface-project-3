import cv2
import numpy as np
from tkinter import Tk  # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


def getCanny(grayImage):
    canny = cv2.Canny(grayImage, 125, 175)

    mask = np.zeros(canny.shape, "uint8")

    for i in range(len(mask[0])):
        mask[0][i] = 255
        mask[-1][i] = 255

    for i in range(len(mask)):
        mask[i][0] = 255
        mask[i][-1] = 255

    canny = cv2.bitwise_or(canny, mask)

    # cv2.imshow(f"Canny {name}", canny)
    return canny


def drawContours(inputImage):
    # eliminate slat and pepper noise
    image = cv2.bilateralFilter(inputImage, 30, 30, 30)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Split the image into separate channels
    b, g, r = cv2.split(image)

    # # b = cv2.bilateralFilter(b, 30, 30, 30)
    # # g = cv2.bilateralFilter(g, 30, 30, 30)
    # # r = cv2.bilateralFilter(r, 30, 30, 30)

    image1 = getCanny(b)
    image2 = getCanny(g)
    image3 = getCanny(r)

    canny = cv2.bitwise_or(image1, image2)
    canny = cv2.bitwise_or(canny, image3)
    cv2.imshow("Edges detected", canny)

    # Find contours
    contours, _ = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # Create a blank mask image
    mask = np.zeros(gray.shape, dtype=np.uint8)

    # Select the top 10 contours
    contours = sorted(contours, key=cv2.contourArea, reverse=True)
    contours = contours[1:11]

    color = 10
    # Iterate over each contour
    for contour in contours:
        # Fill the contour on the mask image with
        cv2.drawContours(mask, [contour], -1, color, -1)
        color += 20

    # Create a copy of the original image
    result = np.copy(image)

    # Apply the mask to the original image
    height, width = mask.shape
    for y in range(height):
        for x in range(width):
            if mask[y, x] != 0:
                result[y, x] = mask[y, x]

    cv2.imshow("Original", inputImage)
    # Display the result
    cv2.imshow("Contours detected", result)


def main():
    Tk().withdraw()
    filePath = askopenfilename()
    # Load the image
    image = cv2.imread(filePath)
    drawContours(image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
