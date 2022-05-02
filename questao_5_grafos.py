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
    for j in arestas:
        grafo.add_aresta(vertice, j, 1)
amigos_de_mussum = []
novos_amigos = []
for amigo_de_mussum in grafo.dicionario_de_vertices['Mussum']:
    amigos_de_mussum.append(amigo_de_mussum[0])


for j in grafo.dicionario_de_vertices:
    if j not in amigos_de_mussum:
        pontos_de_amigo = 0
        for w in grafo.dicionario_de_vertices[j]:
            if w[0] in amigos_de_mussum:
                pontos_de_amigo += 1
        if pontos_de_amigo >= 3:
            novos_amigos.append(j)
for i in novos_amigos:
    if i == 'Mussum':
        novos_amigos.remove(i)
if novos_amigos == []:
    print('Cacildis! Cade elis?')
else:
    novos_amigos = sorted(novos_amigos)
    for i in novos_amigos:
        print(i)

            