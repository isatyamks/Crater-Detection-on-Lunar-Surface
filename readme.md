# Shershaah: Crater Detection on Lunar Surface

Welcome to the Shershaah repository! This project is developed for the Bhartiya Antariksh Hackathon 2024. Our goal is to build an AI/ML model to detect craters on the lunar surface using images from the Orbiter High Resolution Camera (OHRC).

## Project Description

The project aims to automatically detect craters on the Moon's surface utilizing Mask R-CNN, a state-of-the-art deep learning model for object detection and segmentation. The primary data source is the OHRC images, which provide high-resolution imagery essential for accurate crater detection.

## Installation

To get started with this project, follow the instructions below:

1. Clone the repository:
    ```bash
    git clone https://github.com/isatyamks/shershaah.git
    cd shershaah
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the model for detecting craters on lunar images, follow these steps:

1. Prepare your OHRC images and place them in the `datasets/train` directory.
2. Run the detection script:
    ```bash
    samples\crater\inspect_crater_data.ipynb
    ```
3. The results will be saved in the `output` directory with the detected craters highlighted.

## Dependencies

- Python 3.8+
- TensorFlow
- Keras
- OpenCV
- NumPy
- Matplotlib

For a complete list of dependencies, refer to the `requirements.txt` file.


## Contributing

We welcome contributions from the community. If you'd like to contribute, please fork the repository, create a feature branch, and submit a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- The Bhartiya Antariksh Hackathon 2024 organizers for providing this platform.
- Our mentors and peers for their guidance and support.

---

Thank you for visiting our repository. We hope our project contributes to advancements in lunar exploration and AI technology.
