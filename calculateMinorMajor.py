import csv
import os

import cv2
import numpy as np

from calculate_surface import calculate_total_white_area_using_contours

DirPath = 'dir_path'
files = os.listdir(DirPath)

csv_filename = 'cav_filename'

with open(csv_filename, 'w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['File Name', 'Major', 'Minor'])  # Write header

    for v, file in enumerate(files):
        img_path = os.path.join(DirPath, file)

        image = cv2.imread(img_path)

        total_white_area, contour_image, contours = calculate_total_white_area_using_contours(img_path)

        # Combine all points from all contours
        all_points = np.concatenate(contours)

        # Fit an ellipse that encloses all points
        ellipse = cv2.fitEllipseDirect(all_points)

        # Draw the fitted ellipse
        cv2.ellipse(contour_image, ellipse, (0, 255, 0), 2)

        # Extract major and minor axes lengths from the ellipse
        minor_axis_length = min(ellipse[1])
        major_axis_length = max(ellipse[1])

        # Write results to CSV
        csv_writer.writerow([file, major_axis_length, minor_axis_length])
