import cv2
import numpy as np

image = cv2.imread('ch2_ohr_nrp_20211228T2209123959_b_brw_d18.png', cv2.IMREAD_GRAYSCALE)

if image is None:
    raise ValueError("Image not found or unable to load.")

blurred = cv2.GaussianBlur(image, (5, 5), 0)
edges = cv2.Canny(blurred, threshold1=50, threshold2=150)
dilated_edges = cv2.dilate(edges, None, iterations=1)

cv2.imwrite('moon_surface_highlighted.jpg', dilated_edges)
cv2.imshow('Original Image', image)
cv2.imshow('Highlighted Rough Surface', dilated_edges)
cv2.waitKey(0)
cv2.destroyAllWindows()
