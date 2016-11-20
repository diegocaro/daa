def levenshtein(s1, s2):
    p1 = len(s1)
    p2 = len(s2)
    matriz = [[0 for _ in range(p2)] for __ in range(p1)]
    for i in range(p1):
        matriz[i][0] = i
    for j in range (p2):
        matriz[0][j] = j
    # calculo de distancia
    for i in range(1,p1):
        for j in range (1,p2):
            aux = 1
            if (s1[i] == s2[j]):
                aux = 0
            matriz[i][j] = min(matriz[i][j-1] + 1,matriz[i-1][j] + 1,
                                matriz[i-1][j-1] + aux)
    return matriz[p1-1][p2-1]

#  Capítulo 6.7 de Algorithm Design de Kleinberg and Tardos.
def Space_Efficient_Alignmen(s1, s2):
    p1 = len(s1)
    p2 = len(s2)
    matriz = [[0 for _ in range(p2)] for __ in range(p1)]
    for i in range(p1):
        matriz[i][0] = i
    for j in range(1,p2):
        matriz[0][1] = j
        for i in range(1, p1):
            aux = 1
            if (s1[i] == s2[j]):
                aux = 0
            matriz[i][1] = min(matriz[i][0] + 1,matriz[i-1][1] + 1,
                            matriz[i-1][0] + aux)

        for i in range(p1):
            matriz[i][0] = matriz[i][1]
    return matriz[p1-1][1]

# usara por defecto la funcion Space_Efficient_Alignmen
def edit_distance(s1, s2, memory_space_efficent = True):
    # Caso borde cuando hay al menos un string vacio
    if (len(s2) == 0):
        return len(s1)
    elif (len(s2) == 0):
        return len(s1)
    s1 = " " + s1
    s2 = " " + s2
    if (memory_space_efficent):
        return Space_Efficient_Alignmen(s1, s2)
    return levenshtein(s1, s2)

def test(flag):
    palabras = [("casa", "cala"), ("levenshtein", "meilenstein"), ("facil","dificil"),
                ("sonny","snowy"), ("",""), ("a", "a"), ("a", "")]
    resultados = [1,4,3,3,0,0,1]
    for i in range (len(palabras)):
        if flag:
            a = edit_distance(palabras[i][0], palabras[i][1])
            if ( a != resultados[i]):
                print("error, resultado esperado: {} \n resultado obtenido: {} ".format(resultados[i], a) )
                return 1
            # else:
            #     print("Test {} pasado.".format(i+1))
        else:
            b = edit_distance(palabras[i][0], palabras[i][1], False)
            if ( b != resultados[i]):
                print("error, resultado esperado: {} \n resultado obtenido: {} ".format(resultados[i], b) )
                return 1
            # else:
            #     print("Test {} pasado.".format(i+1))
    return 0

if __name__ == '__main__':
    from timeit import Timer
    from sys import argv, exit
    samples = 100
    A = True
    t = Timer("test(A)", "from __main__ import test, A")
    took = t.timeit(samples) / samples
    print( "test for {} took {:.8f} secs".format(A, took))
    A = False
    samples = 100
    t = Timer("test(A)", "from __main__ import test, A")
    took = t.timeit(samples) / samples
    print( "test for {} took {:.8f} secs".format(A, took))
