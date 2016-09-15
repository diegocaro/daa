import unittest
from random import randint

def knuthshuffle(A):
  N = len(A)
  for i in range(N):
    # swap a element A[r] in A[0:i], and swap with A[i]
    r = randint(0, i)
    A[i], A[r] = A[r], A[i]
        
class TestKnuthShuffle(unittest.TestCase):
  def test(self):
    A = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    B = list(A)
    knuthshuffle(B)
    print("A:", A)
    print("B:", B)
    self.assertNotEqual(A, B)
    
if __name__=='__main__':
  unittest.main()
