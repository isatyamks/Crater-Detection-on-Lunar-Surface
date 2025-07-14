import cv2

def open_video(path):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        raise IOError(f"Could not open video: {path}")
    return cap

def create_writer(path, frame_width, frame_height, fps):
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    return cv2.VideoWriter(path, fourcc, fps, (frame_width, frame_height))

def release_all(*objs):
    for obj in objs:
        if obj is not None:
            obj.release() 