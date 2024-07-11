# input_image.py
import cv2

def load_image(image_path):
    image = cv2.imread(image_path)
    return image
