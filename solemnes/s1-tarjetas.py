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
    C.append(B1[0])
    for b in B2:
      if equiv(B1[0], b):
        C.append(b)
  elif len(B2) == 1:
    C.append(B2[0])
    for b in B1:
      if equiv(B2[0], b):
        C.append(b)
  if len(C) > len(B1+B2)/2: 
    return [C[0]]
  else:
    return A

def answer(A):
  global calls
  calls = 0
  ans = tarjetas(A)
  if len(A) <= 10: 
    print(A)
    print(ans)
  return  len(ans) == 1

if __name__=='__main__':
  t = list("bbbbbbbb")
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  t = list("abbbdbbb")
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  t = list("abababbb")
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  t = list("bbbdabcb")
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  t = list("bbdabbcb")
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  t = list("abababab")
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  t = list("abcdefgh")
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  t = list("xyzbbbbc")
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  t = list("aaffccdd")
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  t = list("abababbb"*1)
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  t = list("abababab"*1)
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))
  
  t = list("abcdefgh"*1)
  print(answer(t))
  print("calls:", calls, " theory worst case:", int(len(t) * log(len(t),2)))