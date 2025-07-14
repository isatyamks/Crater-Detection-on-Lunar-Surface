# Crater Detection on Lunar Surface

![Project Banner](docs/banner.png)

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

## Overview

This project provides an end-to-end pipeline for detecting craters on lunar surface images and videos using a YOLOv8 deep learning model. It also identifies the safest landing zones by analyzing crater density.

- **Modular, easy-to-understand codebase**
- **Video and image inference**
- **Safe landing zone detection**
- **Explainable Jupyter notebook**
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
│   └── main.py
│
├── notebooks/
│   └── crater_detection_explained.ipynb
│
├── data/
│   └── ... (model weights, datasets)
│
├── images/
│   └── example_detection.jpg
│   └── safe_landing_zone.jpg
│
├── videos/
│   └── example_detection.mp4
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
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
   - Place your YOLOv8 weights in `data/runs/detect/crater_model/weights/best.pt`.

## Usage

### Video Inference
```bash
python src/main.py --input_video path/to/video.mp4 --output_video path/to/output.mp4
```

### Image Inference
```bash
python src/main.py --input_image path/to/image.png --output_image path/to/output.jpg
```

### CLI Options
- `--input_video`: Path to input video
- `--output_video`: Path to save annotated video
- `--input_image`: Path to input image
- `--output_image`: Path to save annotated image
- `--conf`: Confidence threshold (default: 0.5)
- `--window_size`: Safe zone window size (default: 100,100)
- `--stride`: Sliding window stride (default: 20)

## Example Results

### Crater Detection (Image)
![Detection Example](images/example_detection.jpg)

### Safe Landing Zone (Video)
![Landing Zone Example](images/safe_landing_zone.jpg)

### Video Output
![Video Example](videos/example_detection.mp4)

## Code Explanation
- **src/config.py**: Configuration and argument parsing
- **src/model.py**: Model loading and inference
- **src/detection.py**: Crater detection logic
- **src/video_utils.py**: Video reading/writing utilities
- **src/image_utils.py**: Image reading/writing utilities
- **src/visualization.py**: Drawing and visualization helpers
- **src/main.py**: Entry point, CLI, and workflow orchestration

## Jupyter Notebook
See [`notebooks/crater_detection_explained.ipynb`](notebooks/crater_detection_explained.ipynb) for a step-by-step explanation and visualization of the detection pipeline.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. 