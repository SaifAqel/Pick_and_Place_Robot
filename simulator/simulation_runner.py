"""Run a simple pick-and-place simulation."""

from __future__ import annotations

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation


from simulator.arm_model import ArmModel
from simulator.kinematics import InverseKinematics
from controller.controller_manager import ControllerManager

class SimulationRunner:
    """Coordinate the arm model, IK, and controllers."""

    def __init__(self, arm: ArmModel | None = None) -> None:
        self.arm = arm or ArmModel()
        self.ik = InverseKinematics(self.arm.l1, self.arm.l2, self.arm.l3)
        self.controllers = ControllerManager()
        self.joint_angles = np.zeros(3)
        self.history = []

    def run(self, target: tuple[float, float], steps: int = 100, dt: float = 0.05) -> None:
        """Run the simulation towards the ``target`` point."""
        target_angles = self.ik.ik_solve(*target)
        if target_angles is None:
            print("Target unreachable", target)
            return
        target_angles = np.array(target_angles)
        for _ in range(steps):
            errors = target_angles - self.joint_angles
            outputs = self.controllers.update_all(errors.tolist(), dt)
            self.joint_angles += np.array(outputs) * dt
            ee_pos = self.arm.get_end_effector_position(self.joint_angles)
            self.history.append((*self.joint_angles, *ee_pos))
        self._plot()
    def _plot(self) -> None:
         if not self.history:
            return
            data = np.array(self.history)
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.set_aspect("equal")
            ax.set_xlim(-2, 2)
            ax.set_ylim(-2, 2)
            ax.set_title("Pick and Place Arm Animation")

            # Plot base and target point
            arm_line, = ax.plot([], [], 'o-', lw=4, label="Arm")
            ee_trace, = ax.plot([], [], 'r--', lw=1, alpha=0.5, label="EE path")

            x_traj, y_traj = [], []
    def update(i):
            theta1, theta2, theta3 = data[i, :3]
            x0, y0 = 0, 0
            x1 = self.arm.l1 * np.cos(theta1)
            y1 = self.arm.l1 * np.sin(theta1)
            x2 = x1 + self.arm.l2 * np.cos(theta1 + theta2)
            y2 = y1 + self.arm.l2 * np.sin(theta1 + theta2)
            x3 = x2 + self.arm.l3 * np.cos(theta1 + theta2 + theta3)
            y3 = y2 + self.arm.l3 * np.sin(theta1 + theta2 + theta3)

            x_traj.append(x3)
            y_traj.append(y3)

            arm_line.set_data([x0, x1, x2, x3], [y0, y1, y2, y3])
            ee_trace.set_data(x_traj, y_traj)
            return arm_line, ee_trace

    ani = animation.FuncAnimation(fig, update, frames=len(data), interval=50, blit=True, repeat=False)
    ax.legend()
    plt.show()



if __name__ == "__main__":
    sim = SimulationRunner()
    sim.run((1.5, 0.5))