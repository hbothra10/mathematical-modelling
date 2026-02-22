🚁 Quadcopter Dynamics and Control Simulation
📌 Overview

This project presents a physics-based mathematical model and simulation of a quadcopter UAV.
It implements rigid-body translational and rotational dynamics to reproduce realistic drone motion under thrust, gravity, and attitude changes.

The simulator evolves from a minimal 1D vertical model to a full 3D rigid-body quadcopter with coupled attitude–translation dynamics and visualization.

🎯 Objectives

Model quadcopter motion using first-principles physics

Simulate thrust-driven flight in 3D

Implement attitude dynamics (roll, pitch)

Couple orientation with translational motion

Visualize UAV trajectories and animations

Build a research-grade UAV simulation foundation

🧩 Model Components
1️⃣ Vertical Dynamics
𝐹
=
𝑇
−
𝑚
𝑔
F=T−mg

Simulates ascent, hover, and descent behavior.

2️⃣ 3D Translational Dynamics
𝑎
⃗
=
𝑇
⃗
/
𝑚
+
𝑔
⃗
a
=
T
/m+
g
	​


Tilted thrust produces horizontal motion.

3️⃣ Attitude Dynamics
𝜏
=
𝐼
𝛼
τ=Iα

Torques generate roll and pitch evolution.

4️⃣ Coupled Motion

Changing orientation rotates thrust vector, producing realistic UAV trajectories.

5️⃣ Visualization

2D plots

3D trajectories

Animated flight motion

📊 Features

Physics-based quadcopter model

Time-integrated rigid-body simulation

Tilt-dependent thrust direction

3D trajectory generation

GIF animation export

Modular simulation structure

🧪 Example Simulation

Tilted thrust produces forward acceleration and curved ascent trajectory consistent with quadcopter flight mechanics.

🛠️ Tools

Python

NumPy

Matplotlib

🚀 Future Extensions

Full quadcopter motor torque model

Hover stabilization control

Trajectory tracking

Swarm simulation

🎓 Context

This project is part of a broader study of UAV dynamics, control, and autonomous aerial systems, progressing toward research-level quadcopter modeling and simulation.

👩‍💻 Author

Harshita Bothra
B.Tech Robotics and Automation
2026
