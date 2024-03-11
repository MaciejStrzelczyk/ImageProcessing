import csv
import os

import cv2
import numpy as np

import inner_circle

oils = ['Ol_natur', 'Ol_synt']
whole_paths = ['/Image_const_tsh_', '/Image_const_tsh2_', '/Image_otsu_']


def calculate_mean_radius_for_oils():
    for oil in oils:
        for path in whole_paths:
            current_path = oil + path + oil.lower()
            method_name = path.replace('/Image_', '')
            csv_dir = oil + '/Mean_radius_' + method_name + oil.lower()
            os.mkdir(csv_dir)
            for root, subdirs, files in os.walk(current_path):
                for subdir in subdirs:
                    subdir_path = os.path.join(root, subdir)
                    samples = subdir[11:14]

                    calculate_and_save_to_csv(oil, csv_dir, subdir_path, samples)


def calculate_and_save_to_csv(oil, csv_dir, subdir_path, samples):
    files = os.listdir(subdir_path)
    if oil == 'Ol_natur':
        maskName = 'Mask_' + samples + '_02_circle.jpg'
    else:
        maskName = 'mask' + samples + '_circle.jpg'
    x_circle, y_circle, image_center = inner_circle.get_center(oil + '/Mask_' + oil.lower(), maskName)

    csv_filename = 'new_file.csv'
    csv_filepath = os.path.join(csv_dir, csv_filename)
    with open(csv_filepath, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(['File Name', 'Sum mask radius', 'Sum matrix product', 'Mean radius'])  # Write header

        for v, file in enumerate(files):
            sumMaskRadius, sumMatrixProduct, meanRadius = calculate_radius(subdir_path + '/' + file, x_circle,
                                                                           y_circle)
            csv_writer.writerow([file, sumMaskRadius, sumMatrixProduct, meanRadius])


def calculate_radius(file, x_circle, y_circle):
    mask = cv2.imread(file)
    Matrix = np.zeros(mask.shape)
    mask = mask / 255
    for i in range(0, len(mask[0])):
        for j in range(0, len(mask)):
            distance = np.sqrt(np.abs(pow(int(x_circle - i), 2) + pow(int(y_circle - j), 2)))
            Matrix[j, i, 0] = distance
    matrixProduct = Matrix * mask
    sumMaskRadius = np.sum(mask)
    sumMatrixProduct = np.sum(matrixProduct)
    meanRadius = sumMatrixProduct / sumMaskRadius
    return sumMaskRadius, sumMatrixProduct, meanRadius


def main():
    calculate_mean_radius_for_oils()
