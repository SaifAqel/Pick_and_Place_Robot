"""PID controller implementation."""

from __future__ import annotations

class PIDController:
    """Simple PID controller."""

    def __init__(self, kp: float, ki: float, kd: float) -> None:
        """Initialize gains and reset state."""
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.reset()

    def reset(self) -> None:
        """Reset integral and derivative state."""
        self.integral = 0.0
        self.last_error = 0.0

    def update(self, error: float, dt: float) -> float:
        """Update the controller.

        Parameters
        ----------
        error: float
            Current error value.
        dt: float
            Time step.

        Returns
        -------
        float
            Control output.
        """
        if dt <= 0:
            raise ValueError("dt must be positive")
        self.integral += error * dt
        derivative = (error - self.last_error) / dt
        self.last_error = error
        output = self.kp * error + self.ki * self.integral + self.kd * derivative
        return output


if __name__ == "__main__":
    # Example usage
    pid = PIDController(1.0, 0.1, 0.05)
    current_error = 5.0
    dt = 0.1
    for _ in range(10):
        control = pid.update(current_error, dt)
        print(f"Control output: {control:.2f}")
        current_error *= 0.8

