import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
plt.figure(figsize=(10,8))
ax = plt.axes(projection='3d')
x_c = [5,3,0]
y_c= [1,4,17/2]
z_c = [6,1,-13/2]

result, = ax.plot3D(x_c, y_c, z_c,label="Line Passing through the points (5,1,6) and (3,4,1)",color='r',marker='o')
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Z axis')
for x, y, z in zip(x_c, y_c, z_c):
    label = '(%0.2f, %0.2f, %0.2f)' % (x, y, z)
    ax.text(x, y, z, label)
plt.legend(handles=[result])