import unittest
from bisect import bisect


def rank(A, x):
    'Number of items less or equal than x.'
    i = bisect(A, x)
    if i:
        return i-1
    return -1

def cachier_greedy(x, M):
  M.sort()
  A = [] 
  while x > 0:
    k = rank(M, x)
    if k == -1:
      # no hay solucion
      return list()
    else:
      x = x - M[k]
      A.append(k)
  return A
  
class CointTest(unittest.TestCase):
  def test(self):
    M = [ 1, 5, 10, 50, 100, 500 ]
    
    ans = cachier_greedy(26, M)
    coins = [M[i] for i in ans]
    print("Ans for $26: are coins", coins)
    if len(ans) != 4 or ans != [2, 2, 1, 0]:
      self.fail( "method failed failed." )
    
if __name__=='__main__':
  from sys import exit
  unittest.main()
  exit()
  