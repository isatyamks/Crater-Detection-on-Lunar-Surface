import cv2

def read_image(path):
    image = cv2.imread(path)
    if image is None:
        raise IOError(f"Could not read image: {path}")
    return image

def save_image(path, image):
    cv2.imwrite(path, image) 