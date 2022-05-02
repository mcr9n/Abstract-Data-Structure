class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()
    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)
        self.size = self.size + 1

    def _put(self,key,val,currentNode):
        if key < currentNode.key:
            if currentNode.hasLeftChild():
                   self._put(key,val,currentNode.leftChild)
            else:
                   currentNode.leftChild = TreeNode(key,val,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                   self._put(key,val,currentNode.rightChild)
            else:
                   currentNode.rightChild = TreeNode(key,val,parent=currentNode)
class TreeNode:
    def __init__(self,key,val,left=None, right=None, parent=None):
        self.key = key
        self.payload = val
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.rightChild or self.leftChild)

    def hasAnyChildren(self):
        return self.rightChild or self.leftChild

    def hasBothChildren(self):
        return self.rightChild and self.leftChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self

def altura_2(raiz):
    if raiz is None:
        return -1
    return max(altura_2(raiz.leftChild), altura_2(raiz.rightChild)) + 1
def altura(raiz):
    altura = altura_2(raiz)
    if altura == -1:
        return 0
    else:
        return altura
def mostra_2(raiz, prefixo, n):
    if raiz:
        print(prefixo*n, end ='')
        print(raiz.key)
    n = n + 1
    if raiz.leftChild:
        mostra_2(raiz.leftChild, prefixo, n)
    if raiz.rightChild:
        mostra_2(raiz.rightChild, prefixo, n)

def mostra(raiz, prefixo):
    mostra_2(raiz, prefixo, 0)

numero_de_valores = int(input())
lista_de_chaves = input().split()
arvore_binaria = BinarySearchTree()
for i in lista_de_chaves:
    arvore_binaria.put(i,0)

mostra(arvore_binaria.root,'--')            
tamanho = altura(arvore_binaria.root)
print(tamanho)

    