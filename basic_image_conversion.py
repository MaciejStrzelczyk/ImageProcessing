import os

import cv2
import cv2 as cv
import numpy as np

DirPath = 'dir_path'
NewPath = 'new_dir_path'
files = os.listdir(DirPath)
i = 0

# define the alpha and beta
alpha = 1  # Contrast control
beta = -8  # Brightness control


def main():
    convert_files()


def convert_files():
    for v, file in enumerate(files):
        image = cv.imread(DirPath + '/' + file)

        # Convert the image to the HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Desaturate pixels in the mask
        saturated_image = hsv_image.copy()
        hsv_image[:, :, 1] = saturated_image[:, :, 1] * 0.9

        # Convert image again to BGR
        saturated_image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2RGB)

        preprocessed_image = get_preprocessed_image(saturated_image)

        image_with_threshold = apply_otsu_threshold(preprocessed_image)

        save_new_image(file, image_with_threshold)


def get_preprocessed_image(saturated_image):
    # Call convertScaleAbs function
    adjusted = cv2.convertScaleAbs(saturated_image, beta=beta)

    img = cv.cvtColor(adjusted, cv.COLOR_BGR2RGB)
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    _, thresh = cv2.threshold(gray, np.mean(gray), 255, cv2.THRESH_BINARY_INV)
    mask = np.zeros(img.shape[:2], dtype="uint8")
    dst = cv.bitwise_and(adjusted, img, mask=mask)
    segmented = cv2.cvtColor(dst, cv.COLOR_BGR2RGB)
    segmented = cv2.cvtColor(segmented, cv2.COLOR_RGB2GRAY)

    return cv2.convertScaleAbs(segmented, alpha=1)


def apply_otsu_threshold(adjusted2):
    (_, im_bw) = cv2.threshold(adjusted2, 15, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    return im_bw


def save_new_image(file, im_bw):
    new_file_name = file.replace('.jpg', '_otsu.jpg')
    cv2.imwrite(os.path.join(NewPath, new_file_name), im_bw)
