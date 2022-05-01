class Deque:
    def __init__(self):
        self.__items = []

    def is_empty(self):
        return self.__items == []

    def add_front(self, item):
        self.__items.append(item)

    def add_rear(self, item):
        self.__items.insert(0, item)

    def remove_rear(self):
        return self.__items.pop(0)

    def remove_front(self):
        return self.__items.pop()

    def size(self):
        return len(self.__items)

    def __str__(self):
        sdeque = ''
        for i in self.__items:
            sdeque += i
        return sdeque
def adicionar_alfabeto(deque, alfabeto):
    for i in alfabeto:
        deque.add_front(i.lower())
    
    
    return None

def decifrar(deque, texto_cifrado, chave):
    texto_decodificado = ''
    deque_antigo = deque
    for i in range(chave):
        cabeca = deque.remove_rear()
        deque.add_front(cabeca)
    alfabeto_cifrado = deque.__str__()
    texto_cifrado = texto_cifrado.lower()
    texto_cifrado_lista = list(texto_cifrado)
    for i in texto_cifrado:
        if i in alfabeto_cifrado:
            indice_letra = alfabeto_cifrado.index(i) 
            letra_decodificada = alfabeto_cifrado[(indice_letra - chave)%len(alfabeto_cifrado)]
            texto_decodificado += letra_decodificada
        else:
            texto_decodificado += i
    return texto_decodificado

d = Deque()
alfabeto = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
texto_cifrado = 'WKLVCLVCWKHCZDA'
adicionar_alfabeto(d, alfabeto)
texto_decodificado = decifrar(d, texto_cifrado, 3)
print(texto_decodificado)

