"""Object detection wrapper using simple rules or YOLOv8."""

from __future__ import annotations

from typing import List, Tuple

import cv2

try:
    from ultralytics import YOLO
    _YOLO_AVAILABLE = True
except Exception:  # pragma: no cover - ultralytics may not be installed
    _YOLO_AVAILABLE = False

import numpy as np

from .vision_pipeline import VisionPipeline


class ObjectClassifier:
    """Detect objects in frames."""

    def __init__(self, use_yolo: bool = False, model_path: str | None = None) -> None:
        self.use_yolo = use_yolo and _YOLO_AVAILABLE
        if self.use_yolo:
            self.model = YOLO(model_path or "yolov8n.pt")
        else:
            self.pipeline = VisionPipeline(show_window=False)

    def detect_objects(self, frame: np.ndarray) -> List[Tuple[str, Tuple[int, int]]]:
        """Return a list of detected object labels and centers."""
        results: List[Tuple[str, Tuple[int, int]]] = []
        if self.use_yolo:
            for r in self.model(frame)[0].boxes.data.tolist():
                x1, y1, x2, y2, conf, cls = r
                cx = int((x1 + x2) / 2)
                cy = int((y1 + y2) / 2)
                label = str(int(cls))
                results.append((label, (cx, cy)))
        else:
            det = self.pipeline.process_frame(frame)
            if det:
                results.append(det)
        return results


if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    clf = ObjectClassifier(use_yolo=False)
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        objs = clf.detect_objects(frame)
        if objs:
            print("Objects:", objs)
    cap.release()

    cv2.destroyAllWindows()