import csv
import os

import cv2

DirPath = 'dir_path'
files = os.listdir(DirPath)

csv_filename = 'csv_filename'


def main():
    calculate_white_areas_for_files()


def calculate_white_areas_for_files():
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['File Name', 'Total White Area'])  # Write header

        for v, file in enumerate(files):
            img_path = os.path.join(DirPath, file)

            total_white_area, _, _ = calculate_total_white_area_using_contours(img_path)

            # Write results to CSV
            csv_writer.writerow([file, total_white_area])


def calculate_total_white_area_using_contours(image_path):
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply threshold to segment white areas
    _, thresholded = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv2.findContours(thresholded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours in green with thickness 2
    contour_image = draw_contours(image, contours)

    # Initialize total white area
    total_white_area = 0

    # Iterate through contours and calculate areas
    for contour in contours:
        total_white_area += cv2.contourArea(contour)

    return total_white_area, contour_image, contours


def draw_contours(image, contours):
    contour_image = image.copy()
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
