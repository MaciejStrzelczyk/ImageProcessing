import csv
import os

import cv2
import numpy as np

DirPath = 'dir_path'
files = os.listdir(DirPath)

# Create a CSV file to store results
csv_filename = 'csv_filename'


def main():
    calculate_white_areas_for_files()


def calculate_white_areas_for_files():
    with open(csv_filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['File Name', 'Total White Area'])  # Write header

        for v, file in enumerate(files):
            img_path = os.path.join(DirPath, file)

            total_white_area = calculate_total_white_area(img_path)

            csv_writer.writerow([file, total_white_area])


def calculate_total_white_area(image_path):
    image = cv2.imread(image_path)
    image = np.where(image <= 49, 0, 255)
    return np.sum(image == 255)
