import numpy as np
from matplotlib import pyplot as plt

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

Z1 = X**0.25 + Y**0.25
Z2 = X**2 - Y**2
Z3 = 2*X + 3*Y
Z4 = X**2 - Y**2
Z5 = 2 + 2*X + 2*Y - X**2 - Y

fig = plt.figure(figsize=(15, 12))
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_surface(X, Y, Z1)
ax2 = fig.add_subplot(232, projection='3d')
ax2.plot_surface(X, Y, Z2)
ax3 = fig.add_subplot(233, projection='3d')
ax3.plot_surface(X, Y, Z3)
ax4 = fig.add_subplot(234, projection='3d')
ax4.plot_surface(X, Y, Z4)
ax5 = fig.add_subplot(235, projection='3d')
ax5.plot_surface(X, Y, Z5)

plt.tight_layout()
plt.show()