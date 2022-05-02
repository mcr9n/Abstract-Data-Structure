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
    def add_aresta_direcionada(self,f,t):
        if f not in self.dicionario_de_vertices:
            self.add_vertice(f)
        if t not in self.dicionario_de_vertices:
            self.add_vertice(t)
        self.dicionario_de_vertices[f].append(t)
def encontra_caminho(grafo, comeco, fim, caminho=[]):
    caminho = caminho + [comeco]
    if comeco == fim:
        return caminho
    if not grafo.dicionario_de_vertices[comeco]:
        return []
    for v in grafo.dicionario_de_vertices[comeco]:
        if v not in caminho:
            novo_caminho = encontra_caminho(grafo, v, fim, caminho)
            if novo_caminho: return novo_caminho
    return []
        
numero_de_vertices = int(input())
grafo = Grafo()
for i in range(numero_de_vertices):
    vertice_e_arestas = input().split()
    vertice = vertice_e_arestas[0]
    arestas = vertice_e_arestas[2:]
    grafo.add_vertice(vertice)
    for i in arestas:
        grafo.add_aresta_direcionada(vertice, i)
eu_e_mussum = input().split()
eu = eu_e_mussum[0]
mussum = eu_e_mussum[1]
distancia_minha = len(encontra_caminho(grafo, eu, mussum, []))
distancia_mussum = len(encontra_caminho(grafo, mussum, eu, []))
if distancia_minha == 0 and distancia_mussum == 0:
    print('Forevis alonis...')
elif distancia_minha == 0:
    print(distancia_mussum - 2)
elif distancia_mussum == 0:
    print(distancia_minha - 2)
else:
    if distancia_minha < distancia_mussum: 
        print(distancia_minha - 2)
    elif distancia_mussum < distancia_minha:
        print(distancia_mussum - 2)
    else:
        print(distancia_minha - 2)

    