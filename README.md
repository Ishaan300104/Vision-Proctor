# Vision-Proctor
Vision-Proctor is a webcam-based proctoring system that utilizes YOLOv5 to identify potential cheating behavior during online examinations. By analyzing live video feeds, it ensures a secure and fair testing environment for students. The system detects suspicious behavior if a person is laughing, speaking or covering his/her mouth during the test.

## Table of Contents
- Project Overview
- Installation
- Usage
- Repo Structure
- Dependencies
- Metrics
- Demo
- Acknowledgments

## Project Overview
Vision-Proctor uses YOLOv5 for object detection and behavioral analysis to monitor test-takers. It processes webcam video streams in real-time to detect activities that might indicate cheating, which may help organizations in conducting fair and secure online examinations.

## Installation
To install and set up the project:

### Clone the repository:

```bash
git clone https://github.com/Ishaan300104/Vision-Proctor.git
cd Vision-Proctor
```

Install the necessary dependencies using requirements.txt or set up the environment using the commands listed in the Dependencies section below.

### Download the YOLOv5 repository and labelImg for image labeling.

```bash
git clone https://github.com/ultralytics/yolov5.git
git clone https://github.com/HumanSignal/labelImg.git
```
Make sure your system supports video capture and the necessary packages are installed.

### Usage
Generate Training Data: Use the capture-data.py script to capture images for training (or just use the code provided in the `main.ipynb` file for hassle-free data generation!)

```python
python capture-data.py
```

### Label Data: Use the labelImg tool to label the captured images. This will generate YOLO-readable labels.

  - Use command prompt to navigate to labelImg directory inside the project directory
  - Open labelImg using the code `python labelImg.py`
  - Choose output directory to the labels folder where you want to save the labels
  - Change the labelling format from 'PascalVOC' to 'YOLO'
  - Crop each image and label it accordingly

### Train the YOLOv5 Model:

Navigate to the cloned yolov5 repository and run the training script:
```python
!cd yolov5 && python train.py --img 640 --batch 16 --epochs 100 --data data.yaml --weights yolov5s.pt
```

### Run the Proctoring System:

Open the `main.ipynb` Jupyter notebook provided in the repository to see the full step-by-step implementation of the proctoring system.

The notebook contains code for:

- Loading the YOLOv5 model and the necessary video input.
- Processing the video stream for suspicious activity.
- Outputting a video with detected behaviors and flags.

To run the notebook, ensure you have Jupyter installed:
``` bash
pip install notebook
```

Open the notebook and run all cells in the notebook to start processing your input videos. After running, you'll get the output video demonstrating the flagged behavior.


## Repo Structure
```
Vision-Proctor/
├── README.md               # Project documentation
├── Metrics and performance graphs/ # Performance graphs
│   ├── Training metrics.png        # Training performance graph
│   ├── Validation metrics.png      # Validation performance graph
│   ├── Overall metrics - Precision, Recall, mAP.png   # Overall metrics graph
|   └── visualization_code.py       # Code used for plotting
├── data/
│   ├── images/             # Training images
│   └── labels/             # YOLO format labels
├── demo-video/
│   ├── input-video.mp4           # Input video for demonstration
│   └── output-video.mp4          # Output video after proctoring analysis
├── labelImg/               # Cloned repo for image labeling
├── yolov5/                 # Cloned YOLOv5 repository by ultralytics
├── capture-data.py         # Script to capture images for training
└── main.ipynb              # Jupyter notebook for step-by-step setup
```


## Dependencies
Ensure you have the following installed:

- Python 3
- OpenCV
- PyTorch
- YOLOv5 (clone from YOLOv5 repo)
- LabelImg (clone from labelImg repo)

Install the dependencies:

``` bash
pip install -r yolov5/requirements.txt
pip install opencv-python
```

## Metrics

Below are some key metrics obtained during the training and validation phases:

- Training Performance: box loss, obj loss, cls loss

- Validation Performance: box loss, obj loss, cls loss

- Overall Model Metrics: precision, recall, mAP

## Demo
You can find a sample demonstration of the proctoring system in the demo-video folder. The input and output videos demonstrate the system's ability to monitor and flag potential cheating behaviors.

## Acknowledgments
- The [YOLOv5 repository](https://github.com/ultralytics/yolov5) by ultralytics is used for object detection
- The [labelImg repository](https://github.com/HumanSignal/labelImg)
 is used to label images and generate YOLO-readable annotations
