import numpy as np
import matplotlib.pyplot as plt
import os

# =============================
# Ensure plots folder exists
# =============================
os.makedirs("plots", exist_ok=True)

# =============================
# Physical parameters
# =============================
Ixx = 0.02   # moment of inertia roll
Iyy = 0.02   # moment of inertia pitch

tau_roll = 0.01   # constant roll torque
tau_pitch = -0.008  # constant pitch torque

dt = 0.01
t_final = 5.0

# =============================
# State variables
# =============================
roll = 0.0
pitch = 0.0

omega_roll = 0.0
omega_pitch = 0.0

roll_list = []
pitch_list = []
t_list = []

# =============================
# Simulation loop
# =============================
t = 0.0
while t < t_final:
    # Angular acceleration
    alpha_roll = tau_roll / Ixx
    alpha_pitch = tau_pitch / Iyy

    # Integrate angular velocity
    omega_roll += alpha_roll * dt
    omega_pitch += alpha_pitch * dt

    # Integrate angle
    roll += omega_roll * dt
    pitch += omega_pitch * dt

    roll_list.append(roll)
    pitch_list.append(pitch)
    t_list.append(t)

    t += dt

# =============================
# Convert to degrees for plotting
# =============================
roll_deg = np.rad2deg(roll_list)
pitch_deg = np.rad2deg(pitch_list)

# =============================
# Plot roll & pitch
# =============================
plt.figure(figsize=(7,4))
plt.plot(t_list, roll_deg, label="Roll (deg)")
plt.plot(t_list, pitch_deg, label="Pitch (deg)")
plt.xlabel("Time (s)")
plt.ylabel("Angle (deg)")
plt.title("Quadcopter Attitude Dynamics")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.6)

plt.savefig("plots/attitude_angles.png", dpi=300, bbox_inches="tight")
plt.show()

print("Saved → plots/attitude_angles.png")