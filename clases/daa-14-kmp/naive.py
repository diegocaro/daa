def buscar(patron, texto):
    M = len(patron)
    N = len(texto)
    for i in range(N-M):
        j = 0
        while j < M:
            if texto[i+j] != patron[j]: 
                break
            j += 1
        #encontrado (:
        if j == M: return i
    #no encontrado :(
    return N 

print buscar("hola", "mundholaa")