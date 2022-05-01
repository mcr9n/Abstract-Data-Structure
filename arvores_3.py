class ArvoreBinaria():
    def __init__(self, dado, esq = None, dir = None):
        self.dado = dado
        self.esq = esq
        self.dir = dir
valores_de_j = []
def constituiArvoreBinariaDeBusca_2(raiz):
    global valores_de_j
    if raiz:
        if raiz.esq:
            if raiz.dado < raiz.esq.dado:
                valores_de_j.append(False)
            
            
        if raiz.dir:
            if raiz.dado > raiz.dir.dado:
                valores_de_j.append(False)
                
            
        constituiArvoreBinariaDeBusca_2(raiz.esq)
        constituiArvoreBinariaDeBusca_2(raiz.dir)
def constituiArvoreBinariaDeBusca(raiz):
    global valores_de_j
    constituiArvoreBinariaDeBusca_2(raiz)
    if valores_de_j == []:
        return True
    else:
        valores_de_j = []
        return False
    
    
    


raiz = ArvoreBinaria(2, ArvoreBinaria(1), None)
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2, ArvoreBinaria(3), None)
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2, None, ArvoreBinaria(1))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2, None, ArvoreBinaria(3))
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2)
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2, ArvoreBinaria(0), None)
print(constituiArvoreBinariaDeBusca(raiz))
raiz = ArvoreBinaria(2, None, ArvoreBinaria(0))
print(constituiArvoreBinariaDeBusca(raiz))