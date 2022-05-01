class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir
def altura_2(raiz):
    if raiz is None:
        return 0
    return max(altura_2(raiz.esq), altura_2(raiz.dir)) + 1
def desbalanceamento(raiz):
    # Uma árvore binária vazia é balanceada.
    if raiz is None:
        return True

    altura_esq = altura_2(raiz.esq)
    altura_dir = altura_2(raiz.dir)
    
    return altura_esq - altura_dir
def mostra(raiz):
    if raiz:
        print('(', end = '')

        print(raiz.dado, end = ' ')

        mostra(raiz.esq)

        print('', end = ' ')

        mostra(raiz.dir)

        print(')', end = '')

    else:
        print('()',end = '')
def preordem(raiz):
    if raiz:
        raiz.dado = desbalanceamento(raiz)
        preordem(raiz.esq)
        preordem(raiz.dir)
    

arvore = str(input())
contador_parentese_esq = 0
contador_parentese_dir = 0
primeiro = True
esquerda_ja_foi = False
raiz = None
def monta_arvore(raiz, contador_parentese_esq, contador_parentese_dir, primeiro, esquerda_ja_foi, arvore):
    for i in range(len(arvore)):
        if arvore[i] == ' ':
            continue
        elif arvore[i] != '(' and arvore[i] != ')' and contador_parentese_esq == contador_parentese_dir+1:
            raiz = ArvoreBinaria(arvore[i])
        elif arvore[i] != '(' and arvore[i] != ')' and contador_parentese_esq == contador_parentese_dir+2 and contador_parentese_esq == 2:
            raiz.esq = monta_arvore(raiz.esq, 0, 0, True, False, arvore[i-1:])
            esquerda_ja_foi = True
        elif arvore[i] != '(' and arvore[i] != ')' and contador_parentese_esq == contador_parentese_dir+2:
            raiz.dir = monta_arvore(raiz.dir, 0, 0, True, False, arvore[i-1:])
            esquerda_ja_foi = False
        elif arvore[i] == ')' and contador_parentese_esq == contador_parentese_dir+1:
            contador_parentese_esq = 0
            contador_parentese_dir = 0
            return raiz
        elif arvore[i] == '(':
            contador_parentese_esq += 1
            
        elif arvore[i] == ')':
            contador_parentese_dir += 1
raiz = monta_arvore(raiz, contador_parentese_esq, contador_parentese_dir, primeiro, esquerda_ja_foi, arvore)
preordem(raiz)
mostra(raiz)

