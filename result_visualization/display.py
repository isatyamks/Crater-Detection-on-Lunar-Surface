# result_visualization.py

import cv2
import matplotlib.pyplot as plt

def visualize_result(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.title('Detected Craters')
    plt.show()

def save_image(image, output_path):
    cv2.imwrite(output_path, image)
