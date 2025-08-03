# Pick and Place Robot Arm

## Overview
This project demonstrates a simple AI-driven pick-and-place robot arm
with PID control, inverse kinematics, computer vision and a GUI dashboard.
Everything is written in modular Python for clarity and extensibility.

## Features
- **Simulation** of a 3-link robot arm
- **PID Control** with a controller manager
- **Computer Vision** pipeline and optional YOLOv8 classifier
- **GUI Dashboard** using Streamlit

## Folder Structure
```
pick_and_place_robot/
├── simulator/          # Arm model, kinematics and simulation loop
├── controller/         # PID controllers
├── vision/             # Vision pipeline and object classifier
├── gui/                # Streamlit dashboard and Tkinter monitor
├── data/               # Data samples (empty)
├── models/             # Trained models (empty)
├── run_demo.py         # Main entrypoint
├── requirements.txt    # Python requirements
```

## Installation
```bash
pip install -r requirements.txt
```

## How to Run
```bash
python run_demo.py
```

## Sample Output

![demo screenshot](docs/screenshot_placeholder.png)
