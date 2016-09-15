class TestInsertionSort(unittest.TestCase):
  def test(self):
    A = [8, 5, 3, 1, 9, 6, 0, 7, 4, 2, 5]
    insertionsort(A)
    for i in range(1, len(A)):
      if A[i - 1] > A[i]:
        self.fail( "insertionsort failed." )

if __name__=='__main__':
  unittest.main()