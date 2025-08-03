"""Basic computer vision pipeline using OpenCV."""

from __future__ import annotations

from typing import Optional, Tuple

import cv2
import numpy as np


class VisionPipeline:
    """Detect simple colored shapes in an image."""

    def __init__(self, show_window: bool = True) -> None:
        self.show_window = show_window

    def process_frame(self, frame: np.ndarray) -> Optional[Tuple[str, Tuple[int, int]]]:
        """Detect colored objects in ``frame``.

        Returns a tuple of (label, (x, y)) for the first object found.
        """
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        # Simple color thresholds for red, green, blue
        masks = {
            "red": cv2.inRange(hsv, (0, 70, 50), (10, 255, 255)),
            "green": cv2.inRange(hsv, (50, 70, 50), (70, 255, 255)),
            "blue": cv2.inRange(hsv, (100, 70, 50), (130, 255, 255)),
        }
        for label, mask in masks.items():
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            if contours:
                c = max(contours, key=cv2.contourArea)
                M = cv2.moments(c)
                if M.get("m00"):
                    cx = int(M["m10"] / M["m00"])
                    cy = int(M["m01"] / M["m00"])
                    if self.show_window:
                        cv2.circle(frame, (cx, cy), 5, (255, 255, 255), -1)
                        cv2.putText(frame, label, (cx + 10, cy), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
                        cv2.imshow("Vision", frame)
                        cv2.waitKey(1)
                    return label, (cx, cy)
        if self.show_window:
            cv2.imshow("Vision", frame)
            cv2.waitKey(1)
        return None


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    vp = VisionPipeline()
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        result = vp.process_frame(frame)
        if result:
            print("Detected", result)
    cap.release()
    cv2.destroyAllWindows()