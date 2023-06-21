import cv2

# Load the image
image = cv2.imread("images/4.png")

# Apply Mean Shift segmentation
shifted = cv2.pyrMeanShiftFiltering(image, 9, 9, 30, cv2.TERM_CRITERIA_EPS)

# Display the original and segmented images
cv2.imshow("Original Image", image)
cv2.imshow("Mean Shift Segmentation", shifted)
cv2.waitKey(0)
cv2.destroyAllWindows()
