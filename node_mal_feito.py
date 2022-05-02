class Node:

    def __init__(self,initdata, tempo, link):
        self.data = initdata
        self.next = None
        self.tempo = tempo
        self.before = None
        if int(link) != 0:
            x = self
            for i in range(int(link)):
                x = x.before
            self.link = x
        else:
            self.link = None
        self.indice = None
        

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext
    def setTempo(self,tempo):
        self.tempo = tempo

entrada = input().split()
if entrada[0] != 'f':
    i = 0
    no = Node(entrada[1], i, entrada[2])
    i += 1
    while entrada[0] != 'f':
        if entrada[0] == 'i':
            no_proximo = Node(entrada[1], i, entrada[2])
            no.next = no_proximo
            no_proximo.before = no
            no = no_proximo
            i += 1
    
        elif entrada[0] == 'r':
            no_remover = no
            while no_remover.before.data != entrada[1]:
                if no_remover.link.data == entrada[1]:
                    no_remover.link = None
                no_remover = no_remover.before
                
            no_remover.before.before.next = no_remover
            no_remover.before = no_remover.before.before
            
            
        
        entrada = input().split()
    no_ultimo = no
    while no_ultimo.before != None:
        no_ultimo = no_ultimo.before
    x = 0
    no_ultimo.indice = x
    while no_ultimo.next != None:
        no_ultimo.indice = x
        x += 1
        if no_ultimo.link != None:
            print(f'[{no_ultimo.data}, {no_ultimo.tempo}, {no_ultimo.link.indice}] ', end = '')
        
        else:
            print(f'[{no_ultimo.data}, {no_ultimo.tempo}] ', end = '')