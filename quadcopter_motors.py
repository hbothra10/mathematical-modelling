import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

os.makedirs("plots", exist_ok=True)

# =============================
# Physical parameters
# =============================
m = 1.0
g = np.array([0, 0, -9.81])

Ixx = 0.02
Iyy = 0.02

L = 0.2  # arm length (m)

dt = 0.01
t_final = 5.0

# =============================
# Motor thrusts (N)
# =============================
T1 = 3.2
T2 = 3.0
T3 = 2.8
T4 = 3.0

# Total thrust
T_total = T1 + T2 + T3 + T4

# Torques from thrust differences
tau_roll = L * (T2 - T4)
tau_pitch = L * (T3 - T1)

# =============================
# State variables
# =============================
pos = np.array([0.0, 0.0, 0.0])
vel = np.array([0.0, 0.0, 0.0])

roll = 0.0
pitch = 0.0
omega_roll = 0.0
omega_pitch = 0.0

traj = []

# =============================
# Simulation loop
# =============================
t = 0.0
while t < t_final:

    # Attitude dynamics
    alpha_roll = tau_roll / Ixx
    alpha_pitch = tau_pitch / Iyy

    omega_roll += alpha_roll * dt
    omega_pitch += alpha_pitch * dt

    roll += omega_roll * dt
    pitch += omega_pitch * dt

    # Thrust vector from orientation
    Tx = T_total * np.sin(pitch)
    Ty = -T_total * np.sin(roll)
    Tz = T_total * np.cos(roll) * np.cos(pitch)
    T = np.array([Tx, Ty, Tz])

    # Translation
    a = T/m + g
    vel += a * dt
    pos += vel * dt

    traj.append(pos.copy())
    t += dt

traj = np.array(traj)

# =============================
# Plot
# =============================
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot(traj[:,0], traj[:,1], traj[:,2])
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("Z (m)")
ax.set_title("Motor-Based Quadcopter Dynamics")

plt.savefig("plots/motor_dynamics.png", dpi=300, bbox_inches="tight")
plt.show()

print("Saved → plots/motor_dynamics.png")