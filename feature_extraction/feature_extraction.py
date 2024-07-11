# feature_extraction.py
import cv2
import numpy as np

def extract_features(image):
    # Perform edge detection
    edges = cv2.Canny(image, 100, 200)
    # Apply dilation and erosion
    kernel = np.ones((3, 3), np.uint8)
    dilated_image = cv2.dilate(edges, kernel, iterations=1)
    eroded_image = cv2.erode(dilated_image, kernel, iterations=1)
    return eroded_image
