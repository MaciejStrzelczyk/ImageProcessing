# Image Processing Repository

## Overview
The Image Processing repository hosts a Python application focused on the analysis of partial discharges occurring on insulation pressboard in various types of liquids. The software is designed to process acquired images and perform analyses on geometric features. The workflow involves image loading, extraction of the green channel (where discharges are most visible), application of segmentation methods (Otsu and constant thresholding), overlaying masks (to eliminate image noise), and determination of image parameters (discharge radius, discharge area).

## Key Features
- Image loading and processing
- Green channel extraction for enhanced visibility of discharges
- Segmentation methods (Otsu, constant thresholding)
- Mask application to remove image noise
- Calculation of discharge parameters (radius, surface area)

## Dependiences
- Python
- cv2
- Numpy

## The course of the discharge on the insulating prepanel
![image](https://github.com/MaciejStrzelczyk/ImageProcessing/assets/94145559/59e46bfd-f5a8-4bd2-bba3-b3cecfbfc74e)

## Separation of individual colors
![image](https://github.com/MaciejStrzelczyk/ImageProcessing/assets/94145559/174a0e15-4f34-4618-ae18-c7b949db4c9b)

## Threshold results
![image](https://github.com/MaciejStrzelczyk/ImageProcessing/assets/94145559/b7331234-0040-446f-ba5e-cf7f1ae11711)
(a) fixed thresholding of 40, (b) fixed thresholding of 75, (c) thresholding using the Otsu method.

## Discharge characteristics
![image](https://github.com/MaciejStrzelczyk/ImageProcessing/assets/94145559/148d8f98-1bbb-4d5e-969a-34e5a797bad8)
Surface area


![image](https://github.com/MaciejStrzelczyk/ImageProcessing/assets/94145559/721cfee6-efeb-43ba-9d76-e7eb1813212b)

Representation of the center of the electrode, the farthest pixel, the radius, and the circle



