def fib1(n):
  if n == 0: return 0
  if n == 1: return 1
  return fib1(n-1) + fib1(n-2)

def fib2(n):
  if n == 0: return 0
  f = [0 for i in range(n+1)]
  f[0] = 0
  f[1] = 1
  for i in range(2,n+1):
    f[i] = f[i-1] + f[i-2]
  return f[n]

if __name__=='__main__':
  from timeit import Timer
  N = 30
  samples = 1000
  
  for n in range(N):    
    t = Timer("fib1({})".format(n), \
              "from __main__ import fib1")
    print( "fib1({}) took {} secs".\
            format(n, t.timeit(samples)))
            
  for n in range(N):    
    t = Timer("fib2({})".format(n), \
              "from __main__ import fib2")
    print( "fib2({}) took {} secs".\
            format(n, t.timeit(samples)))