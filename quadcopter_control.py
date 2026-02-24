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
L = 0.2

dt = 0.01
t_final = 5.0

# =============================
# Base motor thrust (hover)
# =============================
T_hover = m * 9.81 / 4

# =============================
# Controller gains
# =============================
k_roll = 0.8
k_pitch = 0.8

# =============================
# State variables
# =============================
pos = np.array([0.0, 0.0, 0.0])
vel = np.array([0.0, 0.0, 0.0])

roll = 0.2     # initial tilt (rad)
pitch = -0.15

omega_roll = 0.0
omega_pitch = 0.0

traj = []

# =============================
# Simulation loop
# =============================
t = 0.0
while t < t_final:

    # ---- Controller torques ----
    tau_roll = -k_roll * roll
    tau_pitch = -k_pitch * pitch

    # ---- Motor thrust adjustments ----
    dT_roll = tau_roll / L
    dT_pitch = tau_pitch / L

    T1 = T_hover - dT_pitch
    T3 = T_hover + dT_pitch
    T2 = T_hover + dT_roll
    T4 = T_hover - dT_roll

    T_total = T1 + T2 + T3 + T4

    # ---- Attitude dynamics ----
    alpha_roll = tau_roll / Ixx
    alpha_pitch = tau_pitch / Iyy

    omega_roll += alpha_roll * dt
    omega_pitch += alpha_pitch * dt

    roll += omega_roll * dt
    pitch += omega_pitch * dt

    # ---- Thrust vector ----
    Tx = T_total * np.sin(pitch)
    Ty = -T_total * np.sin(roll)
    Tz = T_total * np.cos(roll) * np.cos(pitch)
    T = np.array([Tx, Ty, Tz])

    # ---- Translation ----
    a = T/m + g
    vel += a * dt
    pos += vel * dt

    traj.append(pos.copy())
    t += dt

traj = np.array(traj)

# =============================
# Plot trajectory
# =============================
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.plot(traj[:,0], traj[:,1], traj[:,2])
ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("Z (m)")
ax.set_title("Stabilized Quadcopter Dynamics")

plt.savefig("plots/stabilized_trajectory.png", dpi=300, bbox_inches="tight")
plt.show()

print("Saved → plots/stabilized_trajectory.png")