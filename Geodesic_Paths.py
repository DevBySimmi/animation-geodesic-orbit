import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Straight vertical line
x = np.ones(200) * 10
y = np.linspace(0, 140, 200)

# Figure
fig, ax = plt.subplots(figsize=(7,7))

ax.set_title("Animated Geodesic Orbit")
ax.set_xlabel("x")
ax.set_ylabel("y")

ax.set_xlim(-20, 20)
ax.set_ylim(-10, 150)

ax.grid()
ax.set_aspect('equal')

# Mass center
ax.scatter(0, 0, color='black', s=120, label='Mass Center')

# Animated line
line, = ax.plot([], [], color='red', lw=2)

# Moving dot
particle, = ax.plot([], [], 'bo', markersize=8)

ax.legend()

# Animation update
def update(frame):

    # Line gradually draw hogi
    line.set_data(x[:frame], y[:frame])

    # Dot move karega
    particle.set_data([x[frame]], [y[frame]])

    return line, particle

# Animation
ani = FuncAnimation(
    fig,
    update,
    frames=len(x),
    interval=20,
    blit=True
)

plt.show()