import unittest
from collections import namedtuple

Activity = namedtuple('Activity', 'start, end')

def selection(S):
  S.sort(key = lambda a: a.end)
  A = [ S[0] ]
  for a in S[1:]:
    if A[-1].end <= a.start:
      A.append(a)
  return A 
  

class ActivityTest(unittest.TestCase):
  def test(self):
    Sp = [ 1, 4, 3, 5, 0, 6, 5, 7, 3, 9, 5, 9, 6, 10, 8, 11, 8, 12, 2, 14, 12, 16 ]
    S = []
    for i in range(len(Sp)//2):
      S.append( Activity(2*i, 2*i+1) )
    
    ans = selection(S)
    if len(ans) != 11:
      self.fail( "selection failed." )
    

if __name__=='__main__':
  from timeit import Timer
  from sys import argv, exit
  
  # run the unittests if no args are provided
  if len(argv) == 1:
    unittest.main()
    exit()
  
  filename = argv[1]
  
  S = [] # creates an empty array
  with open(filename, 'r') as f:
    for line in f:
      s,e = line.split()
      S.append( Activity(start=int(s), end=int(e)) )
  
  samples = 10
  t = Timer("selection(A)", "from __main__ import selection, S")
  took = t.timeit(samples) / samples 
  print( "selection for {} intervals took {:.4f} secs".format(len(S), took))
