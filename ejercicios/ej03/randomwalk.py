from random import randint
from itertools import accumulate

def randomwalk(N):
    W = [ randint(-1, 1) for _ in range(N)]
    A = list(accumulate(W))
    return A

if __name__=='__main__':
    import matplotlib.pyplot as plt
    serie = randomwalk(10000)
    plt.plot(serie)
    plt.ylabel('some numbers')
    plt.show()