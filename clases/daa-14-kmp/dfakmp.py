patron = "01001001"
M = len(patron)
R = "01"

afd = {}
# R es el alfabeto
for c in R: #
    afd[c] = range(M)

afd[patron[0]][0] = 1
X = 0
for j in range(1,M):
    for c in R:
        afd[c][j] = afd[c][X]
    afd[patron[j]][j] = j + 1
    X = afd[patron[j]][X]

print afd