import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import os

# =============================
# Ensure plots folder exists
# =============================
os.makedirs("plots", exist_ok=True)

# =============================
# Physics Parameters
# =============================
m = 1.0
g = np.array([0.0, 0.0, -9.81])
T_mag = 12.0

# Tilt angles (degrees → radians)
roll = np.deg2rad(10)
pitch = np.deg2rad(15)

# Thrust vector (tilted)
Tx = T_mag * np.sin(pitch)
Ty = -T_mag * np.sin(roll)
Tz = T_mag * np.cos(roll) * np.cos(pitch)
T = np.array([Tx, Ty, Tz])

# =============================
# Simulation
# =============================
dt = 0.02
t_final = 5.0

pos = np.array([0.0, 0.0, 0.0])
vel = np.array([0.0, 0.0, 0.0])

traj = []

t = 0.0
while t < t_final:
    a = T/m + g
    vel += a * dt
    pos += vel * dt
    traj.append(pos.copy())
    t += dt

traj = np.array(traj)

# =============================
# 3D Animation
# =============================
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

# Axis limits
ax.set_xlim(0, np.max(traj[:,0]) * 1.1)
ax.set_ylim(np.min(traj[:,1]) * 1.1, np.max(traj[:,1]) * 1.1)
ax.set_zlim(0, np.max(traj[:,2]) * 1.1)

ax.set_xlabel("X (m)")
ax.set_ylabel("Y (m)")
ax.set_zlabel("Z (m)")
ax.set_title("3D Quadcopter Trajectory")

line, = ax.plot([], [], [], lw=2)
point, = ax.plot([], [], [], "o")

# =============================
# Animation Update Function
# =============================
def update(frame):
    line.set_data(traj[:frame, 0], traj[:frame, 1])
    line.set_3d_properties(traj[:frame, 2])

    point.set_data([traj[frame, 0]], [traj[frame, 1]])
    point.set_3d_properties([traj[frame, 2]])

    return line, point

# =============================
# Create Animation
# =============================
ani = FuncAnimation(
    fig,
    update,
    frames=len(traj),
    interval=30,
    blit=False
)

# =============================
# Save GIF
# =============================
ani.save("plots/quadcopter_3d.gif", dpi=200)

plt.show()

print("Animation saved → plots/quadcopter_3d.gif")