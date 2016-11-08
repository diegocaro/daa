def buscar(patron, texto):
    M = len(patron)
    N = len(texto)
    i = 0; j = 0
    while i < N and j < M:
        j = afd[texto[i]][j]
        i += 1
    if j == M: return i-M #encontrado (:
    else: return N #no encontrado :(
    
print buscar("hola", "mundholaa")