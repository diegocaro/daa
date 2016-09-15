# This is the slow solution.
# Time complexity is O(N)
def bruteforce(A):
  N = len(A)
  for i in range(1, N-1):
    if A[i-1] >= A[i] and A[i] <= A[i+1]:
      return i

if __name__=='__main__':
  from timeit import Timer
  from sys import stdin
  
  A = [] # creates an empty array
  for line in stdin:
    num = int(line)
    A.append(num)	
  
  samples = 10
  t = Timer("bruteforce(A)", "from __main__ import bruteforce, A")
  took = t.timeit(samples)/samples
  print( "bruteforce for {} integers took {:.4f} secs".format(len(A), took))