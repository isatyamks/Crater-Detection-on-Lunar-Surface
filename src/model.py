from ultralytics import YOLO
import cv2


def load_model(weights_path):
    """Load YOLOv8 model from weights."""
    return YOLO(weights_path)


def run_inference(model, image, conf=0.5):
    """Run inference on an image (numpy array or path)."""
    if isinstance(image, str):
        image = cv2.imread(image)
    results = model(image, conf=conf)
    return results 