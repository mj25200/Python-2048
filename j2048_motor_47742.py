from random import random
from random import choice


def get_2ou4():
    dois_ou_quatro = None
    if random() > 0.1:
        dois_ou_quatro = 2
    else:
        dois_ou_quatro = 4
    return dois_ou_quatro

def get_posicoes_vazias(grelha):
    posicoes_vazias = []
    
    for linha in range(4):
        for coluna in range (4):
            if grelha[linha][coluna] == 0:
                posicoes_vazias.append([linha, coluna])
    return posicoes_vazias

def inserir_2ou4(grelha):
    dois_ou_quatro = get_2ou4()
    posicoes_vazias = get_posicoes_vazias(grelha)
    posicao_vazia = choice(posicoes_vazias)
    linha = posicao_vazia[0]
    coluna = posicao_vazia[1]
    grelha[linha][coluna] = dois_ou_quatro
    
    
                

def novo_jogo():
    grelha = [[0, 0, 0, 0],
              [0, 0, 0 ,0],
              [0, 0, 0 ,0],
              [0, 0, 0 ,0]]
    fim = False 
    vitoria = False
    pontos = 0
    inserir_2ou4(grelha)
    inserir_2ou4(grelha)
    jogo = (grelha, fim, vitoria, pontos)
    return jogo

def direita():
    print('direita')

def mover_esquerda(uma_lista):
    nova_lista=[]
    for k in range(len(uma_lista)):
        if uma_lista[k] !=0:
            nova_lista.append(uma_lista[k])
    while len(nova_lista) != len(uma_lista):
        nova_lista.append(0)
    return nova_lista

def somar_esquerda(uma_lista):
    nova_lista = []
    pontos = 0
    k = 0
    while k < len(uma_lista) - 1:
        if uma_lista[k] == uma_lista [k+1]:
            nova_lista.append(uma_lista[k] + uma_lista[k+1])
            pontos = pontos + uma_lista[k] + uma_lista[k+1]
            k = k + 2
        else:
            nova_lista.append(uma_lista[k])
            k = k + 1
    if k == len(uma_lista) - 1:
        nova_lista.append(uma_lista[k])
    while len(nova_lista) != len(uma_lista):
        nova_lista.append(0)
    return (nova_lista, pontos)

def atualizar_grelha(grelha_inicial, grelha):
    sao_iguais = True
    for linha in range(len(grelha_inicial)):
        for coluna in range(len(grelha_inicial[linha])):
            if grelha_inicial [linha][coluna] != grelha[linha][coluna]:
                sao_iguais = False
    if not sao_iguais:
        inserir_2ou4(grelha)
                                                               
def get_vitoria(grelha):
    ganhou = False
    for linha in range(len(grelha)):
        for coluna in range(len(grelha[linha])):
            if grelha[linha][coluna] == 2048:
                ganhou = True
    return ganhou

def ha_iguais_adjacentes(grelha):
    ha_iguais = False
    for linha in range(len(grelha)):
        for coluna in range(len(grelha[linha])-1):
            if grelha[linha][coluna] != 0 and grelha[linha][coluna] == grelha[linha][coluna + 1]:
                ha_iguais = True
    for linha in range(len(grelha) -1):
        for coluna in range(len(grelha[linha])):
            if grelha[linha][coluna] != 0 and grelha[linha][coluna] == grelha[linha + 1][coluna]:
                ha_iguais = True
    return ha_iguais

def get_fim(grelha):
    fim = False
    if len(get_posicoes_vazias(grelha)) == 0 and not ha_iguais_adjacentes(grelha):
        fim = True
    return fim


def esquerda(jogo):
    grelha = jogo[0]
    fim = jogo[1]
    vitoria = jogo[2]
    pontos = jogo[3]
    nova_grelha = []
    for linha in grelha:
        nova_linha_1 = mover_esquerda(linha)
        nova_linha_2 = somar_esquerda(nova_linha_1) [0]
        nova_grelha.append(nova_linha_2)
        pontos = pontos + somar_esquerda(nova_linha_1)[1]
    atualizar_grelha(grelha, nova_grelha)
    fim = get_fim(nova_grelha)
    vitoria = get_vitoria(nova_grelha)
    jogo_actualizado = (nova_grelha, fim, vitoria, pontos)
    return jogo_actualizado


##
def reverte_linhas (grelha):
    nova_grelha = []
    for linha in range(len(grelha)):
        nova_linha = []
        for coluna in range(len(grelha[linha])):
            nova_linha.append(grelha[linha][-1 - coluna])
        nova_grelha.append(nova_linha)
    return nova_grelha

#teste do reverte_linhas        
#grelha = [[1, 2, 3, 4],[5, 6, 7, 8]]
#print(reverte_linhas(grelha))

##
def trocar_linhas_com_colunas(grelha):
    nova_grelha = []
    for coluna in range(len(grelha[0])):
        nova_linha = []
        for linha in range(len(grelha)):
            nova_linha.append(grelha[linha][coluna])
        nova_grelha.append(nova_linha)
    return nova_grelha


#teste do trocar_linhas_com_colunas         
#grelha = [[1, 2, 3, 4],[5, 6, 7, 8]]
#print(trocar_linhas_com_colunas(grelha))

##
def direita(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_revertida = reverte_linhas(grelha)
    jogo_revertido = (grelha_revertida, fim, vitoria, pontos)
    jogo_revertido_atualizado = esquerda(jogo_revertido)
    (grelha, fim, vitoria, pontos) = jogo_revertido_atualizado
    grelha_revertida = reverte_linhas(grelha)
    jogo_atualizado = (grelha_revertida, fim, vitoria, pontos)
    return jogo_atualizado

def acima(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    jogo_transposto_atualizado = esquerda(jogo_transposto)
    (grelha, fim, vitoria, pontos) = jogo_transposto_atualizado
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_atualizado = (grelha_transposta, fim, vitoria, pontos)
    return jogo_atualizado

def abaixo(jogo):
    (grelha, fim, vitoria, pontos) = jogo
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_transposto = (grelha_transposta, fim, vitoria, pontos)
    jogo_transposto_atualizado = direita(jogo_transposto)
    (grelha, fim, vitoria, pontos) = jogo_transposto_atualizado
    grelha_transposta = trocar_linhas_com_colunas(grelha)
    jogo_atualizado = (grelha_transposta, fim, vitoria, pontos)
    return jogo_atualizado
           


def valor(jogo, linha, coluna):
    grelha = jogo[0]
    return grelha [linha][coluna]
    

def terminou(jogo):
    fim = jogo[1]
    return fim

def ganhou_ou_perdeu(jogo):
    vitoria = jogo[2]
    return vitoria

def pontuacao(jogo):
    pontos = jogo[3]
    return pontos


#print(novo_jogo())
