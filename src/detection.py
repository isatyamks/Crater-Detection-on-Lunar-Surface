import numpy as np
import cv2

def get_crater_boxes(results):
    """Extract bounding boxes from YOLO results."""
    return results[0].boxes.xywh.cpu().numpy()  # (x_center, y_center, w, h)

def generate_crater_mask(boxes, shape):
    """Generate a binary mask for detected craters."""
    mask = np.zeros(shape[:2], dtype=np.uint8)
    for (x, y, w, h) in boxes:
        center = (int(x), int(y))
        radius = int(max(w, h) / 2)
        cv2.circle(mask, center, radius, 255, -1)
    return mask

def find_safe_zone(heatmap, window_size=(100, 100), stride=20):
    """Find the safest landing zone using a sliding window over the heatmap."""
    h, w = heatmap.shape
    min_score = float('inf')
    best_box = None
    for y in range(0, h - window_size[1], stride):
        for x in range(0, w - window_size[0], stride):
            window = heatmap[y:y+window_size[1], x:x+window_size[0]]
            score = np.sum(window)
            if score < min_score:
                min_score = score
                best_box = (x, y, window_size[0], window_size[1])
    return best_box

def extract_crater_info(results):
    """Extract (x_center, y_center, diameter, confidence) for each detected crater."""
    boxes = results[0].boxes.xywh.cpu().numpy()
    confs = results[0].boxes.conf.cpu().numpy() if hasattr(results[0].boxes, 'conf') else np.ones(len(boxes))
    crater_info = []
    for (x, y, w, h), conf in zip(boxes, confs):
        diameter = max(w, h)
        crater_info.append({'x_center': float(x), 'y_center': float(y), 'diameter': float(diameter), 'confidence': float(conf)})
    return crater_info

def find_safe_zone_by_crater_count(boxes, window_size=(100, 100), stride=20, max_craters=0, image_shape=None):
    """Find a window with at most max_craters craters inside. Returns the first such window found, or None."""
    if image_shape is None:
        return None
    h, w = image_shape[:2]
    for y in range(0, h - window_size[1], stride):
        for x in range(0, w - window_size[0], stride):
            count = 0
            for (cx, cy, cw, ch) in boxes:
                if x <= cx < x + window_size[0] and y <= cy < y + window_size[1]:
                    count += 1
            if count <= max_craters:
                return (x, y, window_size[0], window_size[1])
    return None 