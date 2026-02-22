import numpy as np
import matplotlib.pyplot as plt

# Parameters
m = 1.0        # mass (kg)
g = 9.81       # gravity (m/s^2)
dt = 0.01      # timestep (s)
t_final = 5.0  # simulation time (s)

# Thrust (change this to test)
T = 12  # Newtons

# State variables
z = 0.0   # position
v = 0.0   # velocity

# Storage
z_list = []
v_list = []
t_list = []

# Simulation loop
t = 0.0
while t < t_final:
    # Acceleration
    a = (T - m*g) / m
    
    # Integrate
    v = v + a * dt
    z = z + v * dt
    
    # Store
    z_list.append(z)
    v_list.append(v)
    t_list.append(t)
    
    t += dt

# Plot
plt.figure()
plt.plot(t_list, z_list)
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.title("Vertical Motion of Quadcopter")
plt.show()