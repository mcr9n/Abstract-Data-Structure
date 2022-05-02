class Arvore_binaria:
    def __init__(self, dado):
        self.dado = dado
        self.esq = None
        self.dir = None
def inserir(raiz,dado):
    if not raiz:
        return Arvore_binaria(dado)
    else:
        if raiz.dado == dado:
            return raiz
        elif dado < raiz.dado:
            raiz.esq = inserir(raiz.esq, dado)
        else:
            raiz.dir = inserir(raiz.dir, dado)
    
    
    return raiz
    
def altura(raiz):
    if raiz is None or not(raiz.esq or raiz.dir):
        return 0
    return max(altura(raiz.esq), altura(raiz.dir)) + 1

def mostra_2(raiz, prefixo, n):
    if raiz:
        print(prefixo*n, end ='')
        print(raiz.dado)
    n = n + 1
    if raiz.esq:
        mostra_2(raiz.esq, prefixo, n)
    if raiz.dir:
        mostra_2(raiz.dir, prefixo, n)

def mostra(raiz, prefixo):
    mostra_2(raiz, prefixo, 0)

numero_de_valores = int(input())
lista_de_chaves = input().split()
arvore_binaria = Arvore_binaria(int(lista_de_chaves[0]))
for i in range(len(lista_de_chaves)):
    if i>0:
        inserir(arvore_binaria, int(lista_de_chaves[i]))


tamanho = altura(arvore_binaria)
print(tamanho)

