# Vision-Proctor
Vision-Proctor is a webcam-based proctoring system that utilizes YOLOv5 to identify potential cheating behavior during online examinations. By analyzing live video feeds, it ensures a secure and fair testing environment for students. The system detects suspicious behavior and flags possible cheating attempts for review.

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
Vision-Proctor uses YOLOv5 for object detection and behavioral analysis to monitor test-takers. It processes webcam video streams in real-time to detect activities that might indicate cheating, helping organizations conduct fair and secure online examinations.

## Installation
To install and set up the project:

1. Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/Vision-Proctor.git
cd Vision-Proctor
Install the necessary dependencies using requirements.txt or set up the environment using the commands listed in the Dependencies section below.

2. Download the YOLOv5 repository and labelImg for image labeling.

Make sure your system supports video capture and the necessary packages are installed.

3. Usage
Generate Training Data:

Use the capture-data.py script to capture images for training:
bash
Copy code
python capture-data.py
Label Data:

4. Use the labelImg tool to label the captured images. This will generate YOLO-readable labels.
5. Train the YOLOv5 Model:

Navigate to the cloned yolov5 repository and run the training script:
bash
Copy code
python train.py --img 640 --batch 16 --epochs 100 --data data.yaml --weights yolov5s.pt
Run the Proctoring System:

6. Open the main.ipynb Jupyter notebook provided in the repository to see the full step-by-step implementation of the proctoring system.

The notebook contains code for:

Loading the YOLOv5 model and the necessary video input.
Processing the video stream for suspicious activity.
Outputting a video with detected behaviors and flags.
To run the notebook:

Ensure you have Jupyter installed:
bash
Copy code
pip install notebook
Open the notebook:
bash
Copy code
jupyter notebook main.ipynb
Run all cells in the notebook to start processing your input videos. After running, you'll get the output video demonstrating the flagged behavior.


Repo Structure

Vision-Proctor/
├── README.md               # Project documentation
├── .gitignore              # Ignored files and directories
├── Metrics/                # Performance graphs
│   ├── training.png        # Training performance graph
│   ├── validation.png      # Validation performance graph
│   └── overall-metrics.png # Overall metrics graph
├── data/
│   ├── images/             # Training images
│   └── labels/             # YOLO format labels
├── demo-video/
│   ├── input.mp4           # Input video for demonstration
│   └── output.mp4          # Output video after proctoring analysis
├── labelImg/               # Cloned repo for image labeling
├── yolov5/                 # Cloned YOLOv5 repository by ultralytics
├── capture-data.py         # Script to capture images for training
└── main.ipynb              # Jupyter notebook for step-by-step proctoring system setup


# Dependencies
Ensure you have the following installed:

- Python 3.8+
- OpenCV
- PyTorch
- YOLOv5 (clone from YOLOv5 repo)
- LabelImg (clone from labelImg repo)

Install the dependencies:

bash
Copy code
pip install -r yolov5/requirements.txt
pip install opencv-python
Metrics

# Below are some key metrics obtained during the training and validation phases:

Training Performance:

Validation Performance:

Overall Model Metrics:

# Demo
You can find a sample demonstration of the proctoring system in the demo-video folder. The input and output videos demonstrate the system's ability to monitor and flag potential cheating behaviors.

# Acknowledgments
The YOLOv5 repository by ultralytics is used for object detection.
The labelImg tool is used to label images and generate YOLO-readable annotations.
