import cv2
import os
import numpy as np

from calculate_surface import calculate_total_white_area_using_contours

DirPath = 'dir_path'
file = 'file_path'

img_path = os.path.join(DirPath, file)
image = cv2.imread(img_path)

total_white_area, contour_image, contours = calculate_total_white_area_using_contours(img_path)

# Combine all points from all contours
all_points = np.concatenate(contours)

# Fit an ellipse that encloses all points
ellipse = cv2.fitEllipseDirect(all_points)

# # Draw the fitted ellipse
cv2.ellipse(contour_image, ellipse, (0, 255, 0), 2)

# Extract major and minor axes lengths from the ellipse
minor_axis_length = min(ellipse[1])
major_axis_length = max(ellipse[1])

# Increase the dimensions of the ellipse by a certain factor (e.g., 1.2)
enlargement_factor = 1.2
enlarged_minor_axis_length = minor_axis_length * enlargement_factor
enlarged_major_axis_length = major_axis_length * enlargement_factor

# Print the dimensions of the ellipse
print("Minor Axis Length:", minor_axis_length)
print("Major Axis Length:", major_axis_length)

# Extract major and minor axes lengths and angle from the ellipse
center, axes, angle = ellipse

# Convert angle from radians to degrees
angle_deg = angle

# Calculate endpoints of the major and minor axes
minor_axis_endpoints = (
    (center[0] - enlarged_minor_axis_length / 2 * np.cos(np.radians(angle_deg)), center[1] - enlarged_minor_axis_length / 2 * np.sin(np.radians(angle_deg))),
    (center[0] + enlarged_minor_axis_length / 2 * np.cos(np.radians(angle_deg)), center[1] + enlarged_minor_axis_length / 2 * np.sin(np.radians(angle_deg)))
)

major_axis_endpoints = (
    (center[0] - enlarged_major_axis_length / 2 * np.cos(np.radians(angle_deg + 90)), center[1] - enlarged_major_axis_length / 2 * np.sin(np.radians(angle_deg + 90))),
    (center[0] + enlarged_major_axis_length / 2 * np.cos(np.radians(angle_deg + 90)), center[1] + enlarged_major_axis_length / 2 * np.sin(np.radians(angle_deg + 90)))
)

# Draw the major and minor axes
cv2.line(contour_image, tuple(map(int, minor_axis_endpoints[0])), tuple(map(int, minor_axis_endpoints[1])), (0, 0, 255), 1)
cv2.line(contour_image, tuple(map(int, major_axis_endpoints[0])), tuple(map(int, major_axis_endpoints[1])), (0, 0, 255), 1)

# Calculate ellipse
ellipse = ((center[0], center[1]), (enlarged_minor_axis_length, enlarged_major_axis_length), angle_deg)

# Draw ellipse
cv2.ellipse(contour_image, ellipse, (255, 0, 0), 2)

# Display the image with drawn contours
cv2.imshow('Image', image)
cv2.imshow('Image with Contours', contour_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
