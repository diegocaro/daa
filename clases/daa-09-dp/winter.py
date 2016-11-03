# Based on Victor Faradazdagi article and code
# Available at http://farazdagi.com/blog/2013/weighted-interval-scheduling/ 

import unittest
from collections import namedtuple
from bisect import bisect_right
Act = namedtuple('Act', 's, f, w')

def calculateP(I):
    # get the previous compatible interval
    # extract start and finish times
    start = [i.s for i in I]
    finish = [i.f for i in I]
    p = []
    for j in range(len(I)):
        # rightmost interval f_i <= s_j
        i = bisect_right(finish, start[j]) - 1  
        p.append(i)
    return p

def compute_opt(j, I, p):
    if j <= 0: return 0
    return max( I[j].w + compute_opt(p[j], I, p), compute_opt(j-1, I, p))

def select(I):
    I.sort(key = lambda a: a.f)
    p = calculateP(I)
    opt = compute_opt(len(I)-1, I, p)
    print("opt = ", opt)

def compute_opt_mem(j, I, p, MEM):
    if j <= 0: return 0
    if MEM[j] != False: return MEM[j]
    MEM[j] = max( I[j].w + compute_opt_mem(p[j], I, p, MEM), \
                  compute_opt_mem(j-1, I, p, MEM))
    return MEM[j]

def select_memo(I):
    MEM = [False for _ in I]
    I.sort(key = lambda a: a.f)
    p = calculateP(I)
    opt = compute_opt_mem(len(I)-1, I, p, MEM)
    print("opt_memo = ", opt)

def select_memo_for(I):
    MEM = [0 for _ in I]
    I.sort(key = lambda a: a.f)
    p = calculateP(I)
    for j in range(1, len(I)):
        MEM[j] = max(I[j].w + MEM[p[j]], MEM[j-1])
    print("opt_for_mem = ", MEM[len(I)-1])


class ActivityTest(unittest.TestCase):
  def test(self):
      I = [ Act(1, 4, 2), Act(3,5,1), Act(0,6,3), Act(4,7,1), \
            Act(3,8,1), Act(5,9,1), Act(6,10,10), Act(8, 11, 9)]
      select(I)
      select_memo(I)
      #select_memo_for(I)
      pass
    

if __name__=='__main__':
  from timeit import Timer
  from sys import argv, exit
  
  # run the unittests if no args are provided
  if len(argv) == 1:
    unittest.main()
    exit()
