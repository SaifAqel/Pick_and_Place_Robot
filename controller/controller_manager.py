"""Manager for multiple PID controllers."""

from __future__ import annotations

from typing import List

from .pid import PIDController


class ControllerManager:
    """Manage PID controllers for each robot joint."""

    def __init__(self, initial_gains: List[tuple] | None = None) -> None:
        """Create three PID controllers.

        Parameters
        ----------
        initial_gains : list of tuple, optional
            Gains for each joint as (kp, ki, kd). Defaults to (1, 0, 0).
        """
        gains = initial_gains or [(1.0, 0.0, 0.0)] * 3
        self.pids = [PIDController(*g) for g in gains]
        self._outputs = [0.0] * 3

    def update_all(self, errors: List[float], dt: float) -> List[float]:
        """Update all controllers with their respective errors."""
        if len(errors) != len(self.pids):
            raise ValueError("errors length mismatch")
        self._outputs = [pid.update(err, dt) for pid, err in zip(self.pids, errors)]
        return self._outputs

    def tune_joint(self, index: int, kp: float, ki: float, kd: float) -> None:
        """Tune PID gains for a specific joint."""
        self.pids[index].kp = kp
        self.pids[index].ki = ki
        self.pids[index].kd = kd
        self.pids[index].reset()

    def get_outputs(self) -> List[float]:
        """Return last computed outputs."""
        return list(self._outputs)


if __name__ == "__main__":
    # Example usage
    manager = ControllerManager()
    errors = [0.5, -0.2, 0.1]
    dt = 0.05
    outputs = manager.update_all(errors, dt)
    print("Outputs:", outputs)
    manager.tune_joint(0, 2.0, 0.1, 0.05)
    outputs = manager.update_all(errors, dt)
    print("Tuned outputs:", outputs)