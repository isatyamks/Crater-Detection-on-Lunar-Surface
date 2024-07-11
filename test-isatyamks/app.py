import cv2
import numpy as np
import matplotlib.pyplot as plt

image_path = 'test-isatyamks/Screenshot 2024-07-11 153733.png'
image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

normalized_image = cv2.normalize(gray_image, None, 0, 255, cv2.NORM_MINMAX)

blurred_image = cv2.GaussianBlur(normalized_image, (5, 5), 0)

edges = cv2.Canny(blurred_image, 100, 200)




kernel = np.ones((3, 3), np.uint8)
dilated_image = cv2.dilate(edges, kernel, iterations=1)
eroded_image = cv2.erode(dilated_image, kernel, iterations=1)







# Apply Hough Circle Transform to detect circles
circles = cv2.HoughCircles(eroded_image, cv2.HOUGH_GRADIENT, dp=1, minDist=20, param1=50, param2=30, minRadius=10, maxRadius=100)

# Draw bounding boxes and label craters
output_image = image.copy()
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Draw the outer circle
        cv2.circle(output_image, (i[0], i[1]), i[2], (255, 0, 0), 2)
        # Draw the center of the circle
        cv2.circle(output_image, (i[0], i[1]), 2, (255, 0, 0), 3)
        # Label the crater
        cv2.putText(output_image, 'Crater', (i[0] - 20, i[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

# Display the final image with detected craters
plt.imshow(cv2.cvtColor(output_image, cv2.COLOR_BGR2RGB))
plt.title('Detected Craters')
plt.show()










# cv2.imwrite('output_image.png', output_image)
