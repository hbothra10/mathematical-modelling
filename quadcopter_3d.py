import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 1.0
g = np.array([0, 0, -9.81])
T_mag = 12

# Tilt angles (radians)
roll = np.deg2rad(10)
pitch = np.deg2rad(15)

# Thrust direction vector
Tx = T_mag * np.sin(pitch)
Ty = -T_mag * np.sin(roll)
Tz = T_mag * np.cos(roll) * np.cos(pitch)

T = np.array([Tx, Ty, Tz])

# State
pos = np.array([0.0, 0.0, 0.0])
vel = np.array([0.0, 0.0, 0.0])

dt = 0.01
t_final = 5

traj = []

t = 0
while t < t_final:
    a = T/m + g
    vel += a*dt
    pos += vel*dt
    traj.append(pos.copy())
    t += dt

traj = np.array(traj)

# Plot
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot(traj[:,0], traj[:,1], traj[:,2])
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
plt.show()