from math import log2

def T(n):
  if n <= 1: return 1
  return 2 * T(n//2) + n


for n in range(2,30):
  N = 2**n
  print(N, T(N), int(N*log2(N)))

  