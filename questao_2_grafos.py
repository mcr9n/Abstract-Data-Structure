class Vertex:
    def __init__(self,key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])
    def lista_de_conexoes(self):
        lista_de_conexoes = [x.id for x in self.connectedTo]
        return lista_de_conexoes
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
    
    #def ligacoes(self, key):
        
    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)
        #self.vertList[t].addNeighbor(self.vertList[f], weight)
    def removeEdge(self,f,t,weight=0):
        if f in self.vertList and t in self.vertList:
            self.vertList[f].connectedTo.pop(self.vertList[t])
            self.vertList[t].connectedTo.pop(self.vertList[f])
    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

numero_de_vertices = int(input())
if numero_de_vertices == 0:
    print('Ue? Ue? Ue?')
else:
    numero_de_vertices_iguais = False
    arestas_diferentes = False
    grafo_1 = Graph()
    for i in range(numero_de_vertices):
        vertice = input().split()
        grafo_1.addVertex(vertice[0])
        for j in vertice[2:]:
            grafo_1.addEdge(vertice[0], j,0)
    nada = input()
    numero_de_vertices_2 = int(input())
    if numero_de_vertices_2 == 0:
        print('Sub-sub!')
    else:
        grafo_2 = Graph()
        for i in range(numero_de_vertices_2):
            vertice = input().split()
            grafo_2.addVertex(vertice[0])
            for j in vertice[2:]:
                grafo_2.addEdge(vertice[0], j,0)

        if set(grafo_2.getVertices()).intersection(grafo_1.getVertices()):
            numero_de_vertices_iguais = True
            
        for v in grafo_1:
            for j in grafo_2:
                if j.id == v.id:
                    if not set(j.lista_de_conexoes()).intersection(v.lista_de_conexoes()) == set(j.lista_de_conexoes()):
                        arestas_diferentes = True

                        
                
        if numero_de_vertices_iguais == True and arestas_diferentes == False:
            print('Sub-sub!')
        else:
            print('Ue? Ue? Ue?')
            

        
    