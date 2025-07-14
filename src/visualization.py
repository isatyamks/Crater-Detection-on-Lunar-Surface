import cv2
import numpy as np

def draw_craters(frame, boxes):
    for (x, y, w, h) in boxes:
        center = (int(x), int(y))
        radius = int(max(w, h) / 2)
        cv2.circle(frame, center, radius, (0, 0, 255), 2)
    return frame

def draw_safe_zone(frame, box):
    if box:
        x, y, win_w, win_h = box
        cv2.rectangle(frame, (x, y), (x + win_w, y + win_h), (0, 255, 0), 2)
        cv2.putText(frame, "Safe Landing Zone", (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
    return frame

def overlay_results(frame, boxes, safe_box):
    frame = draw_craters(frame, boxes)
    frame = draw_safe_zone(frame, safe_box)
    return frame 