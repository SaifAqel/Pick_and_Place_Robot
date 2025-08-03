from __future__ import annotations

import cv2

from simulator.simulation_runner import SimulationRunner
from vision.object_classifier import ObjectClassifier


def main() -> None:
    # Detect an object to pick
    cap = cv2.VideoCapture(0)
    classifier = ObjectClassifier(use_yolo=False)
    ret, frame = cap.read()
    target = (1.0, 0.5)  # fallback target
    if ret:
        detections = classifier.detect_objects(frame)
        if detections:
            _, (x, y) = detections[0]
            target = (x / 100.0, y / 100.0)  # simple mapping for demo
            print(f"Detected target at pixels {(x, y)}, mapped to {target}")
    cap.release()
    cv2.destroyAllWindows()

    sim = SimulationRunner()
    sim.run(target)
    print("Final joint angles:", sim.joint_angles)


if __name__ == "__main__":
    main()