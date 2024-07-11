from pre_processing.input_image import load_image
from pre_processing.preprocessing import preprocess_image
from feature_extraction import extract_features
from crater_detection import detect_craters
from post_processing import draw_bounding_boxes
from result_visualization import visualize_result, save_image

# Path to the input image
image_path = 'test-isatyamks/Screenshot 2024-07-11 153733.png'
# Path to save the output image
output_path = 'output_image.png'

# Load the input image
image = load_image(image_path)

# Preprocess the image
preprocessed_image = preprocess_image(image)

# Extract features
features = extract_features(preprocessed_image)

# Detect craters
craters = detect_craters(features)

# Post-process the image to draw bounding boxes and label craters
output_image = draw_bounding_boxes(image, craters)

# Visualize the result
visualize_result(output_image)

# Save the final image
save_image(output_image, output_path)
