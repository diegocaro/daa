import unittest

def insertionsort(A):
  N = len(A)
  for j in range(1, N):
    k = A[j]
    i = j - 1
    # Insertar A[j] en el subarreglo ordenado A[0:j-1]
    while i >= 0 and A[i] > k:
      A[i+1] = A[i]
      i = i - 1
    A[i+1] = k

class TestInsertionSort(unittest.TestCase):
  def test(self):
    A = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    insertionsort(A)
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
  t = Timer("insertionsort(A)", "from __main__ import insertionsort, A")
  took = t.timeit(samples) / samples 
  print( "insertionsort for {} integers took {:.4f} secs".format(len(A), took))  