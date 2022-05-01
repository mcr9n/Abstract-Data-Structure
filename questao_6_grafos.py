class Grafo:
    def __init__(self):
        self.dicionario_de_vertices = {}
        

    def add_vertice(self,chave):
        self.dicionario_de_vertices[chave] = []
    def add_aresta(self,f,t):
        self.dicionario_de_vertices[f].append(t)
        
    def add_aresta_direcionada(self,f,t,peso):
        if f not in self.dicionario_de_vertices:
            self.add_vertice(f)
        if t not in self.dicionario_de_vertices:
            self.add_vertice(t)
        self.dicionario_de_vertices[f].append([t,peso])


grafo = Grafo()
numero_de_vertices = int(input())
bah = False
for i in range(numero_de_vertices):
    caracteristicas_vertice = input().split()
    vertice = caracteristicas_vertice[0]
    numero_de_arestas = caracteristicas_vertice[1]
    arestas = caracteristicas_vertice[2:]
    grafo.add_vertice(vertice)
    for j in arestas:
        grafo.add_aresta(vertice, j)

for i in grafo.dicionario_de_vertices:
    for j in grafo.dicionario_de_vertices:
        if j in grafo.dicionario_de_vertices[i] and i in grafo.dicionario_de_vertices[j]:
            bah = True
if bah == False:
    print('... que ama ninguem.')
else:
    print('Hoje tem!')
    
            
        

    