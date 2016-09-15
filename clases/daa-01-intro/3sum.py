# This is the slow solution.
# Time complexity is O(n^3)
def bruteforce(A):
  N = len(A)
  count = 0
  for i in range(N):
    for j in range(i+1, N): # for from i+1 to N-1
      for k in range(j+1, N):
        if A[i] + A[j] + A[k] == 0:
          count = count+1
  return count

if __name__=='__main__':
  from timeit import Timer
  from sys import stdin
  
  A = [] # creates an empty array
  for line in stdin:
    num = int(line)
    A.append(num)	
  
  samples = 1
  t = Timer("bruteforce(A)", "from __main__ import bruteforce, A")
  took = t.timeit(samples)
  print( "bruteforce for {} integers took {} secs".format(len(A), took))