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

tau_roll = 0.01
tau_pitch = -0.008

T_mag = 12.0

dt = 0.01
t_final = 5.0

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

    # ---- Attitude dynamics ----
    alpha_roll = tau_roll / Ixx
    alpha_pitch = tau_pitch / Iyy

    omega_roll += alpha_roll * dt
    omega_pitch += alpha_pitch * dt

    roll += omega_roll * dt
    pitch += omega_pitch * dt

    # ---- Thrust vector from orientation ----
    Tx = T_mag * np.sin(pitch)
    Ty = -T_mag * np.sin(roll)
    Tz = T_mag * np.cos(roll) * np.cos(pitch)
    T = np.array([Tx, Ty, Tz])

    # ---- Translational dynamics ----
    a = T/m + g
    vel += a * dt
    pos += vel * dt

    traj.append(pos.copy())
    t += dt

traj = np.array(traj)

# =============================
# 3D plot
# =============================
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot(traj[:,0], traj[:,1], traj[:,2])
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("Z (m)")
ax.set_title("Coupled Quadcopter Dynamics")

plt.savefig("plots/coupled_trajectory.png", dpi=300, bbox_inches="tight")
plt.show()

print("Saved → plots/coupled_trajectory.png")