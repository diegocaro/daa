def buscar(patron, texto):
    M = len(patron)
    N = len(texto)
    i = 0; j = 0
    while i < N and j < M:
        if texto[i] == patron[j]:
            j += 1
        else:
            # desplazamiento explicito
            i -= j; j = 0 
        i += 1

    if j == M: return i-M #encontrado (:
    else: return N #no encontrado :(
    
print buscar("hola", "mundholaa")