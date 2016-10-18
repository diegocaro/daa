from math import log

# for counting the number of calls to equiv()
calls = 0 
def equiv(t1, t2):
  global calls
  calls += 1
  return t1 == t2

def tarjetas(A):
  if len(A) == 1:
    return A
  
  if len(A) == 2:
    if equiv(A[0], A[1]):
      return list(A[0])
    else:
      return A
  
  mid = len(A)//2
  B1 = tarjetas(A[:mid])
  B2 = tarjetas(A[mid:])
  
  # Combinar soluciones
  C = []
  if len(B1) == 1:
    for b in B2:
      if equiv(B1[0], b) == False:
        C.append(b)
  elif len(B2) == 1:
    for b in B1:
      if equiv(B2[0], b) == False:
        C.append(b)
  else:
    C.extend(B1)
    C.extend(B2)
  return C

def answer(A):
  ans = tarjetas(A)
  return  len(ans) < len(A)//2

if __name__=='__main__':
  t = list("abbbcbad")
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  t = list("abbbcbad"*1000)
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  
  calls = 0
  t = list("abcdefgh")
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  calls = 0
  t = list("abcdefgh"*1000)
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))