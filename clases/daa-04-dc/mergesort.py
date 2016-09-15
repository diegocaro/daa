import unittest

aux = []

def merge(A, lo, mid, hi):
  """
  Merge A[lo:mid] with A[mid+1:hi+1]
  """
  i = lo
  j = mid + 1
  #aux = list(A)
  aux[lo:hi+1] = A[lo:hi+1]
  for k in range(lo, hi+1):
    if i > mid:
      A[k] = aux[j]
      j += 1
    elif j > hi:
      A[k] = aux[i]
      i += 1
    elif aux[j] < aux[i]:
      A[k] = aux[j]
      j += 1
    else:
      A[k] = aux[i]
      i += 1

def sort(A, lo, hi):
  if hi <= lo: return
  mid = lo + (hi - lo)//2
  sort(A, lo, mid)
  sort(A, mid+1, hi)
  merge(A, lo, mid, hi)
  
def mergesort(A):
  sort(A, 0, len(A)-1)


class TestMergeSort(unittest.TestCase):
  def test(self):
    A = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    mergesort(A)
    for i in range(1, len(A)):
      if A[i - 1] > A[i]:
        self.fail( "insertionsort failed." )

if __name__=='__main__':
  from timeit import Timer
  from sys import argv, exit
  
  # run the unittests if no args are provided
  if len(argv) == 1:
    unittest.main()
    exit()
  
  filename = argv[1]
  
  A = [] # creates an empty array
  with open(filename, 'r') as f:
    for line in f:
      A.append(int(line))
  
  samples = 10
  t = Timer("mergesort(A)", "from __main__ import mergesort, A")
  took = t.timeit(samples) / samples 
  print( "mergesort for {} integers took {:.4f} secs".format(len(A), took))