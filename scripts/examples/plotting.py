# Import packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from matplotlib.animation import FuncAnimation


plt.rcParams.update(
    {
        "text.usetex": True,
        "font.family": "serif",
        "savefig.format": "pdf",
        "figure.constrained_layout.use": True,
    }
)


x = np.linspace(0, 10, 100)
y = x**2
z = lambda t: y + t

# Create figure
fig = plt.figure()
fig.set_figwidth(12)
fig.set_figheight(5)

ax = fig.add_subplot(111)
ax.grid(visible=True)
ax.plot(x, y)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
ax.legend(["$y = x^2$"])

fig.savefig("plotting.pdf", dpi=300)
fig.savefig("plotting.png", dpi=300)


fig2 = plt.figure()
fig2.set_figwidth(12)
fig2.set_figheight(12)
grid = GridSpec(3, 1, figure=fig2)

ax1 = fig2.add_subplot(grid[0])
ax1.grid(visible=True)
ax1.plot(x, y)
ax1.set_xlabel("$x$")
ax1.set_ylabel("$y$")
ax1.legend(["$y = x^2$"])

ax2 = fig2.add_subplot(grid[1:])
ax2.grid(visible=True)
(P,) = ax2.plot(x, y)
ax2.set_xlabel("$x$")
ax2.set_ylabel("$z$")
ax2.legend(["$z(x, t) = x^2 + t$"])


def update(frame):
    ax2.set_title(f"$t = {frame:.2f}$")
    P.set_ydata(z(frame))
    return (P,)


ani = FuncAnimation(fig2, update, frames=np.linspace(0, 1, 10), blit=True, cache_frame_data=True)

ani.save("plotting_anim.gif")
