import unittest

def sort(A, lo, hi):
  if hi <= lo:
    return
  j = partition(A, lo, hi)
  sort(A, lo, j-1)
  sort(A, j+1, hi)
  
def partition(A, lo, hi):
  i = lo+1
  j = hi
  v = A[lo]
  while True:
    while A[i] < v:
      if i == hi: break
      i = i+1
    while A[j] > v:
      if j == lo: break
      j = j - 1
    if i >= j: break
    A[i], A[j] = A[j], A[i]
  A[j], A[lo] = A[lo], A[j]
  return j

def quicksort(A):
  sort(A, 0, len(A)-1)

class TestQuickSort(unittest.TestCase):
  def test(self):
    A = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    quicksort(A)
    for i in range(1, len(A)):
      if A[i - 1] > A[i]:
        self.fail( "quicksort failed." )
    
    A = list(range(10))
    quicksort(A)
    for i in range(1, len(A)):
      if A[i - 1] > A[i]:
        self.fail( "quicksort failed." )

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
  t = Timer("quicksort(A)", "from __main__ import quicksort, A")
  took = t.timeit(samples) / samples 
  print( "quicksort for {} integers took {:.4f} secs".format(len(A), took))