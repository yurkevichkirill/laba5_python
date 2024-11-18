import numpy as np
from PIL.XpmImagePlugin import xpm_head
from matplotlib import pyplot as plt
from matplotlib.pyplot import ylabel
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(0,10)
y = x
z=2*x + 3*y
fig = plt.figure()
ax=fig.add_subplot(111, projection='3d')
ax.plot(x,y,z, label='parametric curve', alpha=0.6, c='red', fillstyle='right')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()




