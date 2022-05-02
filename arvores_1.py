def mostra_2(raiz, prefixo, n):
    if raiz:
        print(prefixo*n, end ='')
        print(raiz.dado)
        n = n + 1
        for j in raiz.filhos:
            mostra_2(j, prefixo, n)

def mostra(raiz, prefixo):
    mostra_2(raiz, prefixo, 0)

class Arvore():
    def __init__(self, dado):
        self.dado = dado
        self.filhos = []
def leia_2(raiz):
    lista_de_filhos = []
    filhos_e_filhos = input().split()
    filhos_e_filhos = [int(i) for i in filhos_e_filhos]
    for j in range(0,len(filhos_e_filhos),2):
        lista_de_filhos.append(Arvore(filhos_e_filhos[j]))
    raiz.filhos = lista_de_filhos
    for i in range(1,len(filhos_e_filhos),2):
        if filhos_e_filhos[i]!= 0:
            raiz.filhos[(i-1)//2] = leia_2(Arvore(filhos_e_filhos[i-1]))
            
    return raiz

def leia():
    raiz_e_filhos = input().split()
    raiz = int(raiz_e_filhos[0])
    filhos = int(raiz_e_filhos[1])
    arvore = Arvore(raiz)
    if filhos != 0:
        raiz = leia_2(arvore)
        return raiz
    else:
        return arvore

raiz = leia()
mostra(raiz, '--')
