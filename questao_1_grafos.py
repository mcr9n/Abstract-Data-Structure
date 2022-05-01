class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f in self.vertList and t in self.vertList:
            self.vertList[f].addNeighbor(self.vertList[t], weight)
            self.vertList[t].addNeighbor(self.vertList[f], weight)
    def removeEdge(self,f,t,weight=0):
        if f in self.vertList and t in self.vertList:
            self.vertList[f].connectedTo.pop(self.vertList[t])
            self.vertList[t].connectedTo.pop(self.vertList[f])
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())


quantidade_de_operacoes = int(input())
grafo = Graph()
lista_de_operacoes = []
for i in range(quantidade_de_operacoes):
    operacao = input().split()
    lista_de_operacoes.append(operacao)
for operacao in lista_de_operacoes:    
    if operacao[0] == 'IV':
        grafo.addVertex(operacao[1])
for operacao in lista_de_operacoes:
    if operacao[0] == 'RV':
        if operacao[1] in grafo.vertList:
            grafo.vertList.pop(operacao[1])
for operacao in lista_de_operacoes:        
    if operacao[0] == 'IA':
        grafo.addEdge(operacao[1],operacao[2],1)
for operacao in lista_de_operacoes:        
    if operacao[0] == 'RA':
        grafo.removeEdge(operacao[1],operacao[2],1)
lista_de_arestas = []
for v in grafo:
    lista_de_arestas.append(len(v.getConnections()))
if lista_de_arestas == []:
    print(0)
else:
    print(min(lista_de_arestas))