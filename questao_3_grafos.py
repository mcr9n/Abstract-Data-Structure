   
class Grafo:
    def __init__(self):
        self.dicionario_de_vertices = {}
        

    def add_vertice(self,chave):
        self.dicionario_de_vertices[chave] = []
    def add_aresta(self,f,t,peso):
        if f not in self.dicionario_de_vertices:
            self.add_vertice(f)
        if t not in self.dicionario_de_vertices:
            self.add_vertice(t)
        self.dicionario_de_vertices[f].append([t,peso])
        self.dicionario_de_vertices[t].append([f,peso])
    def add_aresta_direcionada(self,f,t,peso):
        if f not in self.dicionario_de_vertices:
            self.add_vertice(f)
        if t not in self.dicionario_de_vertices:
            self.add_vertice(t)
        self.dicionario_de_vertices[f].append([t,peso])


caracteristicas_do_grafo = input().split()
grafo = Grafo()
numero_de_vertices = int(caracteristicas_do_grafo[0])
numero_de_arestas = int(caracteristicas_do_grafo[1])
direcionamento = caracteristicas_do_grafo[2]
if direcionamento == 'N':
    for i in range(numero_de_arestas):
        aresta = input().split()
        f = int(aresta[0])
        t = int(aresta[1])
        peso = int(aresta[2])
        grafo.add_aresta(f, t, peso)
    matriz = []
    for i in range(numero_de_vertices):
        matriz.append([])
        for j in range(numero_de_vertices):
            matriz[i].append(0)
    for w in grafo.dicionario_de_vertices:
        for i in grafo.dicionario_de_vertices[w]:
            matriz[w-1][i[0] - 1] = i[1]
    for linha in matriz:
        for val in linha:
            print('{:4}'.format(val), end = '')
        print()
if direcionamento == 'D':
    for i in range(numero_de_arestas):
        aresta = input().split()
        f = int(aresta[0])
        t = int(aresta[1])
        peso = int(aresta[2])
        grafo.add_aresta_direcionada(f, t, peso)
    matriz = []
    for i in range(numero_de_vertices):
        matriz.append([])
        for j in range(numero_de_vertices):
            matriz[i].append(0)
    for w in grafo.dicionario_de_vertices:
        for i in grafo.dicionario_de_vertices[w]:
            matriz[w-1][i[0] - 1] = i[1]
    for linha in matriz:
        for val in linha:
            print('{:4}'.format(val), end = '')
        print()


        
    
    
