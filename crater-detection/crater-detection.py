# crater_detection.py

import cv2
import numpy as np

def detect_craters(image):
    # Apply Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(image, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=10, maxRadius=100)
    if circles is not None:
        circles = np.uint16(np.around(circles))
    return circles
