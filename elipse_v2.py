import os

import cv2
import numpy as np

from calculate_surface import calculate_total_white_area_using_contours

DirPath = 'dir_path'
file = 'path_to_image'


def main():
    find_ellipse_with_axis()


def find_ellipse_with_axis():
    img_path = os.path.join(DirPath, file)
    image = cv2.imread(img_path)

    total_white_area, contour_image, _ = calculate_total_white_area_using_contours(img_path)

    # Convert to HSV
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Find average pixel
    mean_position = np.mean(np.argwhere(hsv_image[:, :, 2] > 0), axis=0)

    # Find the length of th eclipse axis based on the distance from the center
    long_axis_length, short_axis_length = find_length_ellipse_axis(mean_position, hsv_image)

    # Ellipse axis angle (0)
    angle = 0

    # Draw ellipse
    ellipse = ((mean_position[1], mean_position[0]), (long_axis_length, short_axis_length), angle)
    cv2.ellipse(contour_image, ellipse, (0, 255, 0), 2)

    # Extract axis length
    minor_axis_length = min(ellipse[1])
    major_axis_length = max(ellipse[1])

    # Convert from radian to degree
    angle_deg = ellipse[2]

    # Calculate ends of axis
    minor_axis_endpoints = (
        (ellipse[0][0] - minor_axis_length / 2 * np.cos(np.radians(angle_deg)),
         ellipse[0][1] - minor_axis_length / 2 * np.sin(np.radians(angle_deg))),
        (ellipse[0][0] + minor_axis_length / 2 * np.cos(np.radians(angle_deg)),
         ellipse[0][1] + minor_axis_length / 2 * np.sin(np.radians(angle_deg)))
    )

    major_axis_endpoints = (
        (ellipse[0][0] - major_axis_length / 2 * np.cos(np.radians(angle_deg + 90)),
         ellipse[0][1] - major_axis_length / 2 * np.sin(np.radians(angle_deg + 90))),
        (ellipse[0][0] + major_axis_length / 2 * np.cos(np.radians(angle_deg + 90)),
         ellipse[0][1] + major_axis_length / 2 * np.sin(np.radians(angle_deg + 90)))
    )

    # Draw axis
    cv2.line(contour_image, tuple(map(int, minor_axis_endpoints[0])), tuple(map(int, minor_axis_endpoints[1])),
             (0, 0, 255), 1)
    cv2.line(contour_image, tuple(map(int, major_axis_endpoints[0])), tuple(map(int, major_axis_endpoints[1])),
             (0, 0, 255), 1)

    # Display the image with drawn contours
    cv2.imshow('Image', image)
    cv2.imshow('Image with Contours', contour_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def find_length_ellipse_axis(mean_position, hsv_image):
    height, width, _ = hsv_image.shape
    long_axis_length = max(np.linalg.norm(mean_position - np.array([0, 0])),
                           np.linalg.norm(mean_position - np.array([0, width / 2])),
                           np.linalg.norm(mean_position - np.array([height / 2, 0])),
                           np.linalg.norm(mean_position - np.array([height / 3, width / 3])))

    short_axis_length = min(np.linalg.norm(mean_position - np.array([0, width / 2])),
                            np.linalg.norm(mean_position - np.array([height / 8, width / 8])))
    return long_axis_length, short_axis_length
