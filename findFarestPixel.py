import cv2
import numpy as np

import inner_circle


def main():
    path_to_image = 'path_to_image'
    x_circle, y_circle, image_center = inner_circle.get_center('dir_path', 'mask_name')
    find_farest_pixel(path_to_image, x_circle, y_circle, image_center)


def draw_points_and_circles(image, image_center, x, y, max_sum):
    image = cv2.circle(image, (x, y), radius=5, color=(0, 255, 0), thickness=5)
    image = cv2.circle(image, image_center, radius=int(max_sum), color=(0, 255, 255), thickness=3)
    image = cv2.circle(image, image_center, radius=5, color=(255, 0, 0), thickness=3)
    image = cv2.line(image, image_center, (x, y), color=(0, 0, 255), thickness=3)
    image = image.astype("float32")
    cv2.imshow('Image with Contours', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.imwrite('new_file_name', image)


def find_farest_pixel(path_to_image, x_circle, y_circle, image_center):
    max_sum = 0
    x = 0
    y = 0

    image = cv2.imread(path_to_image)

    # Find farest pixels
    for i in range(25, len(image[0]) - 25):
        for j in range(25, len(image) - 25):
            if image[j, i, 0] == 255:
                # Finding distance
                distance = np.sqrt(np.abs(pow(int(x_circle - i), 2) + pow(int(y_circle - j), 2)))
                if distance > max_sum:
                    max_sum = distance
                    y = j
                    x = i
    draw_points_and_circles(image, image_center, x, y, max_sum)
