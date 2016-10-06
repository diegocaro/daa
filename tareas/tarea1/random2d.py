import numpy as np
import matplotlib.pyplot as plt

points = np.random.rand(30, 2)   # 30 random points in 2-D
plt.plot(points[:,0], points[:,1], 'o')
plt.show()