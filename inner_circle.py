import cv2
import numpy as np


def get_center(new_path, file):
    mask = cv2.imread(new_path + '/' + file, 0)
    white_pixel_coordinates = np.argwhere(mask == 255)

    centroid_x = 0
    centroid_y = 0

    # Calculate the centroid of white pixels
    if white_pixel_coordinates.size > 0:
        centroid_x = int(np.mean(white_pixel_coordinates[:, 1]))
        centroid_y = int(np.mean(white_pixel_coordinates[:, 0]))
        centroid = (centroid_x, centroid_y)
    else:
        centroid = None

    return centroid_x, centroid_y, centroid
