import cv2
import numpy as np

image = cv2.imread('path_to_image')

b, g, r = cv2.split(image)

ret, imgf = cv2.threshold(g, 40, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
mask = cv2.imread('path_to_mask', 0)
mask = cv2.bitwise_not(mask)
mask = np.where(mask <= 49, 0, mask)
mask = mask.astype("int8")

arr = np.uint8(imgf)
cv2.imshow('Image with Contours', arr)
cv2.waitKey(0)
cv2.destroyAllWindows()