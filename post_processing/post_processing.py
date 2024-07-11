# post_processing.py
import cv2

def draw_bounding_boxes(image, circles):
    output_image = image.copy()
    if circles is not None:
        for i in circles[0, :]:
            # Draw the outer circle
            cv2.circle(output_image, (i[0], i[1]), i[2], (255, 255, 0), 2)
            # Draw the center of the circle
            cv2.circle(output_image, (i[0], i[1]), 2, (255, 0, 0), 3)
            # Label the crater
            cv2.putText(output_image, 'Crater', (i[0] - 20, i[1] - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)
    return output_image
