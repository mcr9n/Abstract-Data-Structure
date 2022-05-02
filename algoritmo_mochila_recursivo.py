def cria_matriz(n_linhas, n_colunas, valor):
    matriz = [] 
    for i in range(n_linhas):
        matriz.append([]) 
        for j in range(n_colunas):
            matriz[i].append(valor)
    return matriz
def mochilainteira_recursivo(j, v, w, x, matriz):
    print(w)
    print(v)
    if matriz[j][x] == -1:
        if w[j] > x:
            matriz[j][x] = mochilainteira_recursivo(j-1, v, w, x, matriz)
        else:
            usa = v[j - 1] + mochilainteira_recursivo(j-1,v,w,x-w[j], matriz)
            nao_usa = mochilainteira_recursivo(j-1,v,w,x, matriz)
            matriz[j][x] = max(usa, nao_usa)
    return matriz[j][x]
def algoritmo_mochila(n, v, w, y):
    matriz = cria_matriz(n + 1, y + 1, -1)
        
    for x in range(y + 1):
        matriz[0][x] = 0
    for j in range(n + 1):
        matriz[j][0] = 0
    return mochilainteira_recursivo(n, v, w, y, matriz)

algoritmo_mochila(2, [0,2,4], [0,2, 4], 2)
