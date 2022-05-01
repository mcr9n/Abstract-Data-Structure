raiz_original_mesmo = 0
def comprime_2(raiz, numero_de_rotacoes, n):
    global raiz_original_mesmo
    if raiz:
        if raiz.esq:
            if numero_de_rotacoes!=0:
                raiz = rotaciona_direita(raiz)
                if n == 0:
                    raiz_original_mesmo = raiz
                n = n + 1
                comprime_2(raiz.esq, numero_de_rotacoes - 1,n)
    return
def comprime(raiz,numero_de_rotacoes):
    global raiz_original_mesmo
    comprime_2(raiz, numero_de_rotacoes, 0)
    return raiz_original_mesmo