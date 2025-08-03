"""Simple 3-link robot arm model."""

from __future__ import annotations

from math import cos, sin
from typing import Iterable, Tuple

import matplotlib.pyplot as plt


class ArmModel:
    """Planar 3-link robotic arm."""

    def __init__(self, l1: float = 1.0, l2: float = 1.0, l3: float = 1.0) -> None:
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def get_end_effector_position(self, joint_angles: Iterable[float]) -> Tuple[float, float]:
        """Compute (x, y) of the end effector."""
        theta1, theta2, theta3 = joint_angles
        x1 = self.l1 * cos(theta1)
        y1 = self.l1 * sin(theta1)
        x2 = x1 + self.l2 * cos(theta1 + theta2)
        y2 = y1 + self.l2 * sin(theta1 + theta2)
        x3 = x2 + self.l3 * cos(theta1 + theta2 + theta3)
        y3 = y2 + self.l3 * sin(theta1 + theta2 + theta3)
        return x3, y3

    def _joint_positions(self, joint_angles: Iterable[float]):
        theta1, theta2, theta3 = joint_angles
        x0, y0 = 0.0, 0.0
        x1 = self.l1 * cos(theta1)
        y1 = self.l1 * sin(theta1)
        x2 = x1 + self.l2 * cos(theta1 + theta2)
        y2 = y1 + self.l2 * sin(theta1 + theta2)
        x3 = x2 + self.l3 * cos(theta1 + theta2 + theta3)
        y3 = y2 + self.l3 * sin(theta1 + theta2 + theta3)
        return [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]

    def draw_arm(self, joint_angles: Iterable[float]) -> None:
        """Plot the arm using matplotlib."""
        pts = self._joint_positions(joint_angles)
        xs, ys = zip(*pts)
        plt.figure()
        plt.plot(xs, ys, marker="o")
        plt.xlim(-sum([self.l1, self.l2, self.l3]), sum([self.l1, self.l2, self.l3]))
        plt.ylim(-sum([self.l1, self.l2, self.l3]), sum([self.l1, self.l2, self.l3]))
        plt.gca().set_aspect('equal')
        plt.title("Robot Arm")
        plt.show()


if __name__ == "__main__":
    arm = ArmModel(1, 0.8, 0.6)
    angles = [0.5, 0.5, -0.2]
    print("End effector:", arm.get_end_effector_position(angles))
    arm.draw_arm(angles)