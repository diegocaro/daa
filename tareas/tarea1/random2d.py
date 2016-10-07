import numpy as np
import matplotlib.pyplot as plt

def plot_rand():
    points_rand = np.random.rand(100, 2)   # 30 random points in 2-D
    x_rand = points_rand[:,0]
    y_rand = points_rand[:,1]
    plt.plot(x_rand, y_rand, 'o')
    plt.show()
    
def plot_normal():
    mean = [1, 2]
    cov = [[1, 0], [0, 1]]  # diagonal covariance
    x_normal, y_normal = np.random.multivariate_normal(mean, cov, 100).T
    plt.plot(x_normal, y_normal, 'x')
    plt.show()

plot_rand()
plot_normal()

