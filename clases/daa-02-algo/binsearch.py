import unittest

# recursive version
def binsearchR(A, key, lo, hi):
  if lo > hi:
    return -1 #not found 
  
  mid = lo + (hi - lo)//2
  if A[mid] < key:
    return binsearchR(A, key, mid+1, hi)
  elif A[mid] > key:
    return binsearchR(A, key, lo, mid-1)
  else:
    return mid

# interface for binsearchR
def binary_searchR(A, key):
  return binsearchR(A, key, 0, len(A) -1)


# iterative version
def binary_search(A, key):
  pos = -1
  
  lo = 0
  hi = len(A) -1
  
  while lo <= hi:
    mid = lo + (hi-lo)//2
    if A[mid] < key:
      lo = mid+1
    elif A[mid] > key:
      hi = mid-1
    else:
      pos = mid
      break
  
  return pos
  

class TestBinarySearch(unittest.TestCase):
  def test_binary_searchR(self):
    A = [-1, 1, 3, 4, 9, 12, 23, 90]
    found = binary_searchR(A, 3)
    self.assertEqual(found, 2)
    
    notfound = binary_searchR(A, 99)
    self.assertEqual(notfound, -1)

  def test_binary_search(self):
    A = [-1, 1, 3, 4, 9, 12, 23, 90]
    found = binary_search(A, 3)
    self.assertEqual(found, 2)
    
    notfound = binary_search(A, 99)
    self.assertEqual(notfound, -1)


if __name__=='__main__':
  unittest.main()
