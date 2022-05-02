class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
j = 0
w = 1
n = 0
numero_de_wookies = int(input())
lista_de_cargas = [int(u) for u in input().split()]
fila_de_wookies = Queue()
dicionario_de_pilhas = {}
lista_de_sobras = []
lista_de_pesos = []
j = False
if numero_de_wookies != 0:
    for i in range(numero_de_wookies):
        fila_de_wookies.enqueue(i+1)
        dicionario_de_pilhas[i+1] = []
    while j != len(lista_de_cargas):
        if w == numero_de_wookies:
            if dicionario_de_pilhas[w] == []:
                dicionario_de_pilhas[w].append(lista_de_cargas[j])
                j += 1
            elif dicionario_de_pilhas[w][len(dicionario_de_pilhas[w]) - 1] >= lista_de_cargas[j]:
                dicionario_de_pilhas[w].append(lista_de_cargas[j])
                j += 1
            elif dicionario_de_pilhas[w][len(dicionario_de_pilhas[w]) - 1] < lista_de_cargas[j]:
                w = 1
                n += 1
                if n == 3:
                    lista_de_sobras.append(lista_de_cargas[j])
                    j += 1
                    n = 1
        elif dicionario_de_pilhas[w] == []:
            dicionario_de_pilhas[w].append(lista_de_cargas[j])
            j += 1
            w += 1
        elif dicionario_de_pilhas[w][len(dicionario_de_pilhas[w]) - 1] < lista_de_cargas[j]:
            w += 1
            
        else:
            
            dicionario_de_pilhas[w].append(lista_de_cargas[j])
            j += 1
            w = 1
else:
    print('Os Wookies foram para o lado sombrio da força!')
    lista_de_sobras = lista_de_cargas
for j in dicionario_de_pilhas:
    lista_de_pesos.append(dicionario_de_pilhas[j])
    lista_de_pesos.sort(key=lambda x: sum(x), reverse = True)
for i in lista_de_pesos:
    print(i, end = ' ')
    j = True
if j == True:
    print()
if lista_de_sobras == []:
    print('A força está com os Wookies!')
else:
    for j in lista_de_sobras:
        print(j, end = ' ')
    
    
    


    
