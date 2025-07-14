import argparse


def get_config():
    parser = argparse.ArgumentParser(description="Crater Detection on Lunar Surface")
    parser.add_argument('--input_video', type=str, help='Path to input video file')
    parser.add_argument('--output_video', type=str, help='Path to save annotated video')
    parser.add_argument('--input_image', type=str, help='Path to input image file')
    parser.add_argument('--output_image', type=str, help='Path to save annotated image')
    parser.add_argument('--conf', type=float, default=0.5, help='Confidence threshold for detection')
    parser.add_argument('--window_size', type=int, nargs=2, default=[100, 100], help='Safe zone window size (width height)')
    parser.add_argument('--stride', type=int, default=20, help='Sliding window stride')
    parser.add_argument('--weights', type=str, default='data/runs/detect/crater_model/weights/best.pt', help='Path to YOLO model weights')
    parser.add_argument('--max_craters', type=int, default=0, help='Maximum number of craters allowed in a safe landing window (default: 0)')
    args = parser.parse_args()
    return args 