lista_de_dados = []
total_dos_pontos = 0
lista_liberadores = []
lista_rebaixados = []
lista_rebaixados_mesmo = []
for i in range(20):
    lista_nome_jogos = input().split(' ')
    nome_do_time = lista_nome_jogos[0]
    lista_jogos = lista_nome_jogos[1:]
    quantidade_de_vitorias = 0
    gols_marcados = 0
    gols_sofridos = 0
    pontos_do_time = 0
    saldo_de_gols = 0
    for j in lista_jogos:
        gols_feitos = j.split('x')
        gols_a_favor = int(gols_feitos[0])
        gols_contra = int(gols_feitos[1])
        if gols_a_favor > gols_contra:
            pontos_do_time += 3
            quantidade_de_vitorias += 1
            saldo_de_gols += gols_a_favor - gols_contra
            gols_marcados += gols_a_favor
            gols_sofridos += gols_contra
        elif gols_a_favor == gols_contra:
            pontos_do_time += 1
            saldo_de_gols += gols_a_favor - gols_contra
            gols_marcados += gols_a_favor
            gols_sofridos += gols_contra
        elif gols_a_favor < gols_contra:
            saldo_de_gols -= gols_contra - gols_a_favor
            gols_marcados += gols_a_favor
            gols_sofridos += gols_contra
    dados_do_time = [pontos_do_time, quantidade_de_vitorias, saldo_de_gols, gols_marcados, gols_sofridos, nome_do_time]
    lista_de_dados.append(dados_do_time)
    
for i in lista_de_dados:
    total_dos_pontos += i[0]
media_dos_pontos = total_dos_pontos / 20
print(f'Media de pontos: {media_dos_pontos:.2f}')
lista_de_dados.sort(key=lambda x: x[5])
lista_de_dados.sort(key=lambda x: x[4])
lista_de_dados.sort(key=lambda x: x[3], reverse = True)
lista_de_dados.sort(key=lambda x: x[2], reverse = True)
lista_de_dados.sort(key=lambda x: x[1], reverse = True)
lista_de_dados.sort(key=lambda x: x[0], reverse = True)
for j in lista_de_dados:
    if len(lista_liberadores)<4:
        lista_liberadores.append(j[5])
    else:
        break

while len(lista_rebaixados)<4:
    lista_rebaixados.append(lista_de_dados.pop())

for j in lista_rebaixados:
    if len(lista_rebaixados_mesmo)<4:
        lista_rebaixados_mesmo.append(j[5])
    else:
        break
print(f'Liberadores: {lista_liberadores[0]}, {lista_liberadores[1]}, {lista_liberadores[2]}, {lista_liberadores[3]}')
print(f'Rebaixados: {lista_rebaixados_mesmo[0]}, {lista_rebaixados_mesmo[1]}, {lista_rebaixados_mesmo[2]}, {lista_rebaixados_mesmo[3]}')