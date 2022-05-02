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

''' Primeira Tarefa - Decodificação da Lista de Missões '''
def adicionar_alfabeto(d, alfabeto):
    for i in alfabeto:
        d.add_front(i)
    
    
    return None

def decifrar(d, texto_cifrado, chave):
    alfabeto = d.__str__()
    texto_decodificado = ''
    for i in range(chave):
        cabeca = d.remove_rear()
        d.add_front(cabeca)
    alfabeto_cifrado = d.__str__()
    texto_cifrado_lista = list(texto_cifrado)
    for i in texto_cifrado:
        if i in alfabeto_cifrado:
            indice_letra = alfabeto_cifrado.index(i) 
            letra_decodificada = alfabeto_cifrado[(indice_letra - chave)%len(alfabeto_cifrado)]
            texto_decodificado += letra_decodificada
        else:
            texto_decodificado += i


    for i in range(chave):
        cauda = d.remove_front()
        d.add_rear(cauda)

        
    
    return texto_decodificado

''' Segunda Tarefa - Selecionar Subconjunto de Missões '''
def selecionar_subconjunto_missoes():
    tempo_disponivel = int(input())
    m_booleano = int(input())     #indica se a saida vai ser ordenada pelo parametro O
    parametro_o = int(input())   #a saída do conjunto s deve estar ordenada segundo o parâmetro O se m == 1
    alfabeto = input()
    chave = int(input())
    numero_de_missoes = int(input())
    tempo_restante = tempo_disponivel
    valor_total = 0
    lista_de_duracoes = [0]
    lista_de_duracoes_ordenada = []
    lista_de_valores = [0]
    lista_de_valores_ordenada = []
    lista_de_nomes = [0]
    lista_de_nomes_ordenada = []
    lista_de_dificuldades = [0]
    lista_de_dificuldades_ordenada = []
    missoes_recomendadas = []
    def cria_matriz(n_linhas, n_colunas, valor):
        matriz = [] 
        for i in range(n_linhas):
            matriz.append([]) 
            for j in range(n_colunas):
                matriz[i].append(valor)
        return matriz
    def mochilainteira_recursivo(j, v, w, x, matriz):
        
        if matriz[j][x] == -1:
            if w[j] > x:
                matriz[j][x] = mochilainteira_recursivo(j-1, v, w, x, matriz)
            else:
                usa = v[j] + mochilainteira_recursivo(j-1,v,w,x-w[j], matriz)
                nao_usa = mochilainteira_recursivo(j-1,v,w,x, matriz)
                matriz[j][x] = max(usa, nao_usa)
        
        return matriz[j][x]
    def algoritmo_mochila(n, v, w, y):
        matriz = cria_matriz(n + 1, y + 1, -1)
        
        for x in range(y + 1):
            matriz[0][x] = 0
        for j in range(n + 1):
            matriz[j][0] = 0
        resultado_final = mochilainteira_recursivo(n, v, w, y, matriz)
        s = []
        x = y
        j = n
        while j >= 1:
            if matriz[j][x] == matriz[j-1][x-w[j]]+ v[j]:
                s.append(j)
                x = x - w[j]
            j = j - 1
        return s
        
           
    
    for i in range(numero_de_missoes):
        texto_cifrado = input()
        texto_cifrado.join('')
        d = Deque()
        adicionar_alfabeto(d, alfabeto)
        texto_decodificado = decifrar(d, texto_cifrado, chave)
        lista_texto_decodificado = texto_decodificado.split(',')
    
        nome_da_missao = lista_texto_decodificado[0][1:]
        lista_de_nomes.append(nome_da_missao)
        duracao = int(lista_texto_decodificado[1])
        lista_de_duracoes.append(duracao)
        valor = int(lista_texto_decodificado[2])
        lista_de_valores.append(valor)
        dificuldade = lista_texto_decodificado[3][:len(texto_decodificado[3]) - 2]
        lista_de_dificuldades.append(dificuldade)
    solucao_otima = algoritmo_mochila(numero_de_missoes, lista_de_valores, lista_de_duracoes, tempo_disponivel)
    lista_de_solucoes = []
    for i in solucao_otima:
        valor_total += lista_de_valores[i]
        tempo_restante -= lista_de_duracoes[i]
        solucao = [lista_de_nomes[i], lista_de_duracoes[i], lista_de_valores[i], lista_de_dificuldades[i]]
        lista_de_solucoes.append(solucao)
    if m_booleano == 1:
        if parametro_o == 0:
            lista_de_solucoes.sort(key=lambda x: x[3])
            lista_de_solucoes.sort(key=lambda x: x[2])
            lista_de_solucoes.sort(key=lambda x: x[1])
            lista_de_solucoes.sort(key=lambda x: x[0])
            for i in lista_de_solucoes:
                print(f'{i[0]}, {i[1]}, {i[2]}, {i[3]}')
        if parametro_o == 1:
            lista_de_solucoes.sort(key=lambda x: x[3])
            lista_de_solucoes.sort(key=lambda x: x[2])
            lista_de_solucoes.sort(key=lambda x: x[0])
            lista_de_solucoes.sort(key=lambda x: x[1])
            for i in lista_de_solucoes:
                print(f'{i[0]}, {i[1]}, {i[2]}, {i[3]}')
        if parametro_o == 2:
            lista_de_solucoes.sort(key=lambda x: x[3])
            lista_de_solucoes.sort(key=lambda x: x[1])
            lista_de_solucoes.sort(key=lambda x: x[0])
            lista_de_solucoes.sort(key=lambda x: x[2])
            for i in lista_de_solucoes:
                print(f'{i[0]}, {i[1]}, {i[2]}, {i[3]}')
        if parametro_o == 3:
            lista_de_solucoes.sort(key=lambda x: x[2])
            lista_de_solucoes.sort(key=lambda x: x[1])
            lista_de_solucoes.sort(key=lambda x: x[0])
            lista_de_solucoes.sort(key=lambda x: x[3])
            for i in lista_de_solucoes:
                print(f'{i[0]}, {i[1]}, {i[2]}, {i[3]}')
            
            
    
    print(f'Tempo restante: {tempo_restante}')
    print(f'Valor: {valor_total}')
    
            
    return None

selecionar_subconjunto_missoes()

