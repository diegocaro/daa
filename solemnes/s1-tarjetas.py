from math import log
import unittest

# for counting the number of calls to equiv()
calls = 0 
def equiv(t1, t2):
  global calls
  calls += 1
  return t1 == t2

def tarjetas(A):
  if len(A) == 1:
    return A
  
  if len(A) == 2:
    if equiv(A[0], A[1]):
      return list(A[0])
    else:
      return A
  
  mid = len(A)//2
  B1 = tarjetas(A[:mid])
  B2 = tarjetas(A[mid:])
  if len(B1) == 1:
    c = 0
    for t in A:
      if equiv(B1[0], t): c += 1
    if c > len(A)/2:
      return B1
  if len(B2) == 1:
    c = 0
    for t in A:
      if equiv(B2[0], t): c += 1
    if c > len(A)/2:
      return B2
  return A
  

def answer(A):
  global calls
  calls = 0
  ans = tarjetas(A)
  return len(ans) < len(A)/2

class TestInsertionSort(unittest.TestCase):
  def testTrue(self):
    cases = ["abababbb", "abaabbbb", "bbbbbbbb", "abbbdbbb", "abababbb", "bbdabbcb"]
    for case in cases:
      t = list(case)
      if False == answer(t):
        print("input: ", t)
        self.fail( "algorithm failed" )
        
  def testFalse(self):
    cases = ["abcdefgh", "abababab", "xyzbbbbc", "aaffccdd"]
    for case in cases:
      t = list(case)
      if True == answer(t):
        self.fail( "algorithm failed" )
  
if __name__=='__main__':
  unittest.main()