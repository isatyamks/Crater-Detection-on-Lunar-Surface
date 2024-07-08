import pds4_tools
import numpy as np
import cv2
from pds4_tools.reader import read

try:
    data = read('isro.xml')

    image_data = data[0].data

    image_array = np.array(image_data)

    cv2.imshow('OHRC Image', image_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

except Exception as e:
    print(f"An error occurred: {e}")
