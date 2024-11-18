import numpy as np
from PIL.XpmImagePlugin import xpm_head
from matplotlib import pyplot as plt
from matplotlib.pyplot import ylabel
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-5,5,100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)


Z1 = X**0.25 + Y**0.25
fig = plt.figure(figsize=(15, 12))
ax1 = fig.add_subplot(231, projection='3d')
ax1.plot_surface(X, Y, Z1, cmap='viridis')
ax1.set_title('z = x^0.25 + 0.25')
plt.tight_layout()
plt.show()




