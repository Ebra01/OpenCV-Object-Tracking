# OpenCV Simple Tracking Project

This is a simple OpenCV tracking Project following this: [OpenCV Tutorial](https://www.youtube.com/watch?v=GgGro5IV-cs)

## Credits

Youtube Channel: [PySource](https://www.youtube.com/@pysource-com)

## Installation

To install the required libraries, run the following command:

`
pip install -r requirements.txt
`

## Usage

1. Install the DNN Model used in this project from [HERE](https://pysource.com/2021/10/05/object-tracking-from-scratch-opencv-and-python/)

2. Configure `object_detection.py` to setup the DNN Model:
    ```python
    class ObjectDetection:
      def __init__(self, weights_path="PATH TO WEIGHTS (e.g.: yolov4.weight)", cfg_path="PATH TO CONFIG (e.g. yolov4.cfg)"):
        ...
      def load_class_names(self, classes_path="PATH TO CLASSES FILE (e.g.: classes.txt)"):
        ...
      ...
    ```

3. Open `object_tracking.py` and change the video file `los_angeles.mp4` to your video file: 
    ```python
    cap = cv2.VideoCapture("YOUR VIDEO PATH")
    ```

4. After installing the libraries, and making the required changes, you can run the application using the following command: `python3 object_tracking.py`
    - Press `ESC` to exit the app.