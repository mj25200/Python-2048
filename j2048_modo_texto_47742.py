
from j2048_motor_47742 import novo_jogo
from j2048_motor_47742 import terminou
from j2048_motor_47742 import esquerda
from j2048_motor_47742 import direita
from j2048_motor_47742 import acima
from j2048_motor_47742 import abaixo
from j2048_motor_47742 import valor
from j2048_motor_47742 import pontuacao

from j2048_gestor_47742 import le_identificacao
from j2048_gestor_47742 import inicializa_semente
from j2048_gestor_47742 import regista_grelha_inicial
from j2048_gestor_47742 import regista_jogada
from j2048_gestor_47742 import regista_pontos
from j2048_gestor_47742 import escreve_registo





print('jogo 2048')
print('use as teclas wasd para jogar')
print('use a tecla n para iniciar um novo jogo')
print('use a tela q para para terminar')
print('boa sorte!')

def print_2048(jogo):
    print('pontos = ' + str(jogo[3]))
    grelha_texto = ''
    for linha in range (4):
       for  coluna in range(4):
           grelha_texto = grelha_texto + str(jogo[0] [linha] [coluna]) + '\t'
       grelha_texto = grelha_texto + '\n'
    print(grelha_texto)


le_identificacao()
inicializa_semente(None)

jogo = novo_jogo()
print_2048(jogo)

regista_grelha_inicial(valor(jogo, 0, 0), valor(jogo, 0, 1), valor(jogo, 0, 2), valor(jogo, 0, 3),
                       valor(jogo, 1, 0), valor(jogo, 1, 1), valor(jogo, 1, 2), valor(jogo, 1, 3),
                       valor(jogo, 2, 0), valor(jogo, 2, 1), valor(jogo, 2, 2), valor(jogo, 2, 3),
                       valor(jogo, 3, 0), valor(jogo, 3, 1), valor(jogo, 3, 2), valor(jogo, 3, 3))

tecla = None
while tecla != 'q' and not terminou(jogo):
    tecla = input()
    if tecla == 'n':
        regista_pontos(pontuacao(jogo))
        mensagem_cloud = escreve_registo()
        print(mensagem_cloud)
        inicializa_semente(None)
        jogo = novo_jogo()
        regista_grelha_inicial(valor(jogo, 0, 0), valor(jogo, 0, 1), valor(jogo, 0, 2), valor(jogo, 0, 3),
                       valor(jogo, 1, 0), valor(jogo, 1, 1), valor(jogo, 1, 2), valor(jogo, 1, 3),
                       valor(jogo, 2, 0), valor(jogo, 2, 1), valor(jogo, 2, 2), valor(jogo, 2, 3),
                       valor(jogo, 3, 0), valor(jogo, 3, 1), valor(jogo, 3, 2), valor(jogo, 3, 3))
    elif tecla == 'a':
        jogo = esquerda(jogo)
        regista_jogada(tecla)
    elif tecla == 'd':
        jogo = direita(jogo)
        regista_jogada(tecla)
    elif tecla == 'w':
        jogo = acima(jogo)
        regista_jogada(tecla)
    elif tecla == 's':
        jogo = abaixo(jogo)
        regista_jogada(tecla)
    print_2048(jogo)


    
regista_pontos(pontuacao(jogo))
mensagem_cloud = escreve_registo()
print(mensagem_cloud)
print('FIM')

