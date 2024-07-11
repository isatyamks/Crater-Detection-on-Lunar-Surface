
import time
from pre_processing.input_image import load_image

from pre_processing.preprocessing import preprocess_image
from feature_extraction.feature_extraction import extract_features
from crater_detection.crater_detection import detect_craters
from post_processing.post_processing import draw_bounding_boxes
from result_visualization.display import visualize_result, save_image




image_path = 'input_images/5.png'





timestamp = time.strftime("%Y%m%d-%H%M%S")
output_path = f'output_images/output_image_{timestamp}.png'
image = load_image(image_path)



preprocessed_image = preprocess_image(image)


features = extract_features(preprocessed_image)


craters = detect_craters(features)


output_image = draw_bounding_boxes(image, craters)


visualize_result(output_image)


save_image(output_image, output_path)
