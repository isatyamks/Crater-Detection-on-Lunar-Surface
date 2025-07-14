# Crater Detection on Lunar Surface

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

## Overview

This project provides an end-to-end pipeline for detecting craters on lunar surface images and videos using a YOLOv8 deep learning model. It also identifies the safest landing zones by analyzing crater density.

- **Modular, easy-to-understand codebase**
- **Video and image inference**
- **Safe landing zone detection**
- **Ready for research and deployment**

## Features
- Crater detection using YOLOv8
- Video and image processing
- Automatic safe landing zone suggestion
- Modular, well-documented code
- CLI for easy usage
- Visualization and result saving

## Project Structure
```
Crater-Detection-on-Lunar-Surface/
│
├── src/
│   ├── __init__.py
│   ├── config.py
│   ├── model.py
│   ├── detection.py
│   ├── video_utils.py
│   ├── image_utils.py
│   ├── visualization.py
│
├── main.py
├── requirements.txt
├── weights/
│   ├── best.pt
│   ├── last.pt
│   └── args.yaml
├── report/
│   └── Report_A1/
│       ├── val_batch0_pred.jpg
│       ├── val_batch1_pred.jpg
│       ├── val_batch2_pred.jpg
│       └── ...
├── result/
│   └── model_A1/
│       ├── predicted_image.jpg
│       └── video_craters.csv
├── testing/
│   ├── images/
│   │   └── image.png
│   └── videos/
│       └── video.mp4
├── README.md
└── ...
```

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Crater-Detection-on-Lunar-Surface.git
   cd Crater-Detection-on-Lunar-Surface
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Download model weights:**
   - Place your YOLOv8 weights in `weights/best.pt`.

## Usage

### Video Inference
```bash
python main.py --input_video path/to/video.mp4 --output_video path/to/output.mp4
```

### Image Inference
```bash
python main.py --input_image path/to/image.png --output_image path/to/output.jpg
```

### CLI Options
- `--input_video`: Path to input video
- `--output_video`: Path to save annotated video
- `--input_image`: Path to input image
- `--output_image`: Path to save annotated image
- `--conf`: Confidence threshold (default: 0.5)
- `--window_size`: Safe zone window size (default: 100 100)
- `--stride`: Sliding window stride (default: 20)
- `--weights`: Path to YOLO model weights (default: weights/best.pt)
- `--max_craters`: Maximum number of craters allowed in a safe landing window (default: 0)

## Example Results

> **To display images or videos in the README:**
> - Move/copy your desired output images (e.g., `result/model_A1/predicted_image.jpg` or any from `report/Report_A1/`) to an `images/` folder at the root, and reference as:
>   ```markdown
>   ![Detection Example](images/predicted_image.jpg)
>   ```
> - For videos, move/copy to a `videos/` folder at the root, and reference as:
>   ```markdown
>   ![Video Example](result/model_A1/best.mp4)
>   ```
> - Alternatively, upload to an image/video hosting service and use the direct URL.

### Crater Detection (Image)
<!-- Example: -->
<!-- ![Detection Example](images/predicted_image.jpg) -->

### Safe Landing Zone (Image)
<!-- Example: -->
<!-- ![Landing Zone Example](images/val_batch0_pred.jpg) -->

### Video Output
<!-- Example: -->
[![Custom thumbnail](https://images.unsplash.com/photo-1593434970421-886020b13769?q=80&w=1170&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D)](https://youtu.be/blEz4HXD2vY)


## Code Explanation
- **src/config.py**: Configuration and argument parsing
- **src/model.py**: Model loading and inference
- **src/detection.py**: Crater detection logic
- **src/video_utils.py**: Video reading/writing utilities
- **src/image_utils.py**: Image reading/writing utilities
- **src/visualization.py**: Drawing and visualization helpers
- **main.py**: Entry point, CLI, and workflow orchestration

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. 
