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
def preordem(raiz):
    if raiz:
        print(raiz.dado, end = ' ')
        preordem(raiz.esq)
        preordem(raiz.dir)
def emordem(raiz):
    if raiz:
        emordem(raiz.esq)
        print(raiz.dado, end = ' ')
        emordem(raiz.dir)
def posordem(raiz):
    if raiz:
        posordem(raiz.esq)
        posordem(raiz.dir)
        print(raiz.dado, end = ' ')
n = 0
arvore_binaria = None
while True:
    comando = str(input())
    if comando == 'in':
        emordem(arvore_binaria)
        print()
    elif comando == 'pre':
        preordem(arvore_binaria)
        print()
    elif comando == 'pos':
        posordem(arvore_binaria)
        print()
    elif comando == 'quack':
        break
    else:
        if n == 0:
            arvore_binaria = Arvore_binaria(int(comando))
            n = 1
        else:
            inserir(arvore_binaria, int(comando))