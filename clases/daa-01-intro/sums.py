count = 0
for i in range(N):
  if A[i] == 0:
    count += 1

count = 0
for i in range(N):
  for j in range(N):
    if A[i] + A[j] == 0:
      count += 1
