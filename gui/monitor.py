"""Basic Tkinter monitor for joint angles."""

from __future__ import annotations

import tkinter as tk
from typing import List


class AngleMonitor(tk.Tk):
    def __init__(self, angles: List[float]) -> None:
        super().__init__()
        self.title("Joint Monitor")
        self.labels = []
        for i, a in enumerate(angles):
            label = tk.Label(self, text=f"Joint {i+1}: {a:.2f}")
            label.pack()
            self.labels.append(label)
        self.after(100, self.update_labels)
        self.angles = angles

    def update_labels(self) -> None:
        for i, label in enumerate(self.labels):
            label.config(text=f"Joint {i+1}: {self.angles[i]:.2f}")
        self.after(100, self.update_labels)


if __name__ == "__main__":
    angles = [0.0, 0.0, 0.0]
    app = AngleMonitor(angles)
    app.mainloop()