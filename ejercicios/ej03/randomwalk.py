from random import randint, shuffle
from itertools import accumulate

def randomwalk(N):
    W = [ randint(-1, 1) for _ in range(N)]
    A = list(accumulate(W))
    return A

def randperm(N):
    R = list(range(N))
    shuffle(R)
    return R

if __name__=='__main__':
    import matplotlib.pyplot as plt
    
    N = 1000
    xdata = list(range(N))
    
    rwalk = randomwalk(N)
    rperm = randperm(N)
    
    plt.figure(1)
    plt.subplot(211)
    plt.ylabel('random walk')
    plt.plot(xdata, rwalk, 'ro')

    plt.subplot(212)
    plt.ylabel('random permutation')
    plt.plot(xdata, rperm, 'bo')
    plt.show()
    
    