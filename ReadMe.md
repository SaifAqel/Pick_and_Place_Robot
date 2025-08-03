# Pick and Place Robot Arm

##  Overview
A modular, Python-based simulation of an AI-driven 3-link pick-and-place robot arm. This project integrates **PID control**, **inverse kinematics**, **real-time computer vision**, and a **Streamlit dashboard** for visualization and control.

##  Key Features
-  **3-Link Robot Arm Simulation** — Forward and inverse kinematics.
-  **PID Controller Manager** — Adjustable for precise motion control.
-  **Computer Vision Pipeline** — Basic detection + optional YOLOv8 integration.
-  **Interactive GUI** — Built with Streamlit (plus optional Tkinter monitor).

##  Project Structure
```
pick_and_place_robot/
├── simulator/          # Arm model, kinematics, and simulation logic
├── controller/         # PID controller implementation
├── vision/             # Object detection and vision processing
├── gui/                # Streamlit UI and optional Tkinter monitor
├── data/               # Sample or test data
├── models/             # Trained model files 
├── run_demo.py         # Entry point to run the full system
├── requirements.txt    # Dependency list
```

##  Installation
Install the required dependencies:
```bash
pip install -r requirements.txt
```

##  Run the Demo
Launch the full system simulation:
```bash
python run_demo.py
```

##  How It Works
1. **Object Detection**: Captures video using OpenCV. If YOLOv8 is enabled, it performs real-time object classification.
2. **Coordinate Mapping**: The detected object's image coordinates are mapped to real-world positions relative to the robot arm.
3. **Inverse Kinematics**: The simulator computes the joint angles required to move the arm's end effector to the target position.
4. **PID Control**: Each joint is driven using a PID controller to smoothly reach the desired angle.
5. **Visualization**: The Streamlit GUI displays the arm status, logs, and detected objects, allowing for interactive monitoring.

##  Author
**Saif Aqel**  






