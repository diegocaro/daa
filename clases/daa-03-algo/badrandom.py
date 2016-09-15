from random import random

# PLEASE, DO NOT USE THIS FUNCTION, IT WILL
# GENERATE DUPLICATED VALUES, SOON OR LATER
def badrandom(N, maxval):
  out = []
  for i in range(N):
    out.append( int(random()*maxval) )
  return out

if __name__=='__main__':
  # Create a list of 10 items randomly chosen
  l1 = badrandom(10, 10)
  print(l1)
  
  N = 1000
  l2 = badrandom(N, N)
  
  import matplotlib.mlab as mlab
  import matplotlib.pyplot as plt
  num_bins = 50
  # the histogram of the data
  n, bins, patches = plt.hist(l2, num_bins, normed=1, facecolor='green', alpha=0.5)
  # add a 'best fit' line
  plt.xlabel('A[i]')
  plt.ylabel('Probability')
  plt.title(r'Histograma de Numeros generados con badrandom()')

  # Tweak spacing to prevent clipping of ylabel
  plt.subplots_adjust(left=0.15)
  plt.show()
