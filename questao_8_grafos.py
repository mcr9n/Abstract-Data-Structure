class Grafo:
    def __init__(self):
        self.dicionario_de_vertices = {}
        

    def add_vertice(self,chave):
        self.dicionario_de_vertices[chave] = {}
    def add_aresta(self,f,t, peso):
        self.dicionario_de_vertices[f][t] = peso
        
    def add_aresta_direcionada(self,f,t,peso):
        if f not in self.dicionario_de_vertices:
            self.add_vertice(f)
        if t not in self.dicionario_de_vertices:
            self.add_vertice(t)
        self.dicionario_de_vertices[f].append([t,peso])


grafo = Grafo()
numero_de_vertices = int(input())
for i in range(numero_de_vertices):
    caracteristicas_vertice = input().split()
    vertice = caracteristicas_vertice[0]
    numero_de_arestas = caracteristicas_vertice[1]
    arestas = caracteristicas_vertice[2:]
    grafo.add_vertice(vertice)
    for j in range(len(arestas)):
        if j % 2 == 0:
            grafo.add_aresta(vertice,arestas[j+1],int(arestas[j]))
menores_distancias = {}
distancias_necessarias = []
print(grafo.dicionario_de_vertices)

            
            
        
for w in menores_distancias:
    for j in menores_distancias:
        if j in menores_distancias[w] and w in menores_distancias[j]:
            menores_distancias[j] = []
print(menores_distancias)
for i in menores_distancias:
    if menores_distancias[i] != []:
        distancias_necessarias.append(menores_distancias[i][0])
preco = sum(distancias_necessarias) * 3.14
print(preco)
        