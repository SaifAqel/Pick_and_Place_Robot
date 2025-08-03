"""Inverse kinematics utilities for the 3-link arm."""

from __future__ import annotations

from math import acos, atan2, cos, sin, sqrt
from typing import Iterable, List, Optional


class InverseKinematics:
    """Simple IK solver for planar 3-link arm."""

    def __init__(self, l1: float, l2: float, l3: float) -> None:
        self.l1 = l1
        self.l2 = l2
        self.l3 = l3

    def ik_solve(self, x: float, y: float) -> Optional[List[float]]:
        """Solve IK for a target point (x, y).

        Returns a list of three joint angles or ``None`` if unreachable.
        """
        l23 = self.l2 + self.l3
        r = sqrt(x ** 2 + y ** 2)
        if r > self.l1 + l23:
            return None
        # Law of cosines for angle at joint2
        cos_a2 = (r ** 2 - self.l1 ** 2 - l23 ** 2) / (2 * self.l1 * l23)
        cos_a2 = max(-1.0, min(1.0, cos_a2))
        a2 = acos(cos_a2)
        a1 = atan2(y, x) - atan2(l23 * sin(a2), self.l1 + l23 * cos(a2))
        a3 = 0.0  # simple orientation
        return [a1, a2, a3]


if __name__ == "__main__":
    ik = InverseKinematics(1, 0.8, 0.6)
    target = (1.5, 0.5)
    angles = ik.ik_solve(*target)
    print("Angles:", angles)