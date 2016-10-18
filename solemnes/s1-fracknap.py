def fracknap(A, W):
  # ordenar por el mejor precio por kg, de mayor a menor
  A.sort(key = lambda x: x[1]/x[0], reverse=True)
  ans = []
  tw = 0
  for w, p in A:
    if tw + w > W:
      avail = W - tw
      frac = avail/w
      ans.append(( w*frac , p*frac))
      break
    ans.append((w, p))
    tw += w
  
  gain = sum([p for w,p in ans ] )
  return gain, ans

if __name__=='__main__':
  t = [ (20, 100), (30, 120), (10, 60)]
  w = 50
  gain, ans = fracknap(t, w)
  print("motin:", gain, "items robados:", ans)