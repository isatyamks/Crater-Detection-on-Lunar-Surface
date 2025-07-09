from src.config import get_config
from src.model import load_model, run_inference
from src.detection import get_crater_boxes, generate_crater_mask, find_safe_zone, extract_crater_info, find_safe_zone_by_crater_count
from src.visualization import overlay_results
from src.video_utils import open_video, release_all
from src.image_utils import read_image, save_image
import cv2
import numpy as np
import csv
import os

def export_craters_csv(crater_info, output_path):
    csv_path = os.path.splitext(output_path)[0] + '_craters.csv'
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['x_center', 'y_center', 'diameter', 'confidence']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in crater_info:
            writer.writerow(row)
    print(f"Crater info exported to: {csv_path}")

def process_video(args, model):
    cap = open_video(args.input_video)
    all_craters = []
    frame_idx = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        results = run_inference(model, frame, conf=args.conf)
        boxes = get_crater_boxes(results)
        mask = generate_crater_mask(boxes, frame.shape)
        heatmap = cv2.GaussianBlur(mask, (31, 31), 0)
        safe_box = find_safe_zone_by_crater_count(
            boxes,
            window_size=tuple(args.window_size),
            stride=args.stride,
            max_craters=args.max_craters,
            image_shape=frame.shape
        )
        if safe_box is None:
            safe_box = find_safe_zone(heatmap, window_size=tuple(args.window_size), stride=args.stride)
        annotated = overlay_results(frame.copy(), boxes, safe_box)
        if safe_box is None:
            cv2.putText(annotated, "No landing zone", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
        crater_info = extract_crater_info(results)
        for crater in crater_info:
            crater['frame'] = frame_idx
        all_craters.extend(crater_info)
        frame_idx += 1
        cv2.imshow("Craters + Landing Zone", annotated)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    release_all(cap)
    cv2.destroyAllWindows()
    csv_path = os.path.splitext(args.input_video)[0] + '_craters.csv'
    with open(csv_path, 'w', newline='') as csvfile:
        fieldnames = ['frame', 'x_center', 'y_center', 'diameter', 'confidence']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in all_craters:
            writer.writerow(row)
    print(f"Crater info exported to: {csv_path}")

def process_image(args, model):
    image = read_image(args.input_image)
    results = run_inference(model, image, conf=args.conf)
    boxes = get_crater_boxes(results)
    mask = generate_crater_mask(boxes, image.shape)
    heatmap = cv2.GaussianBlur(mask, (31, 31), 0)
    safe_box = find_safe_zone_by_crater_count(
        boxes,
        window_size=tuple(args.window_size),
        stride=args.stride,
        max_craters=args.max_craters,
        image_shape=image.shape
    )
    if safe_box is None:
        safe_box = find_safe_zone(heatmap, window_size=tuple(args.window_size), stride=args.stride)
    annotated = overlay_results(image.copy(), boxes, safe_box)
    if safe_box is None:
        cv2.putText(annotated, "No landing zone", (30, 40), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 255), 3)
    save_image(args.output_image, annotated)
    crater_info = extract_crater_info(results)
    export_craters_csv(crater_info, args.output_image)
    print(f"Done! Output saved as: {args.output_image}")

def main():
    args = get_config()
    model = load_model(args.weights)
    if args.input_video:
        process_video(args, model)
    elif args.input_image and args.output_image:
        process_image(args, model)
    else:
        print("Please provide valid input and output paths for either video or image.")

if __name__ == "__main__":
    main() 