from random import randint
from time import sleep
from interface import *


def roleta(dinhe, aposta):
    sorteio= [[], [], []]
    dindin = dinhe
    vlc = [1, 2, 3, 4, 5] #valor linhas e colunas
    vd = [2, 3, 4, 5, 10] #valor diagonais
    vw = [20, 40, 60, 80, 100] #valor pelo 'w' na tela
    goun = 0
    # Sortear os números e inseri-los na tupla.

    for n in range(0, 3):
        sorteio[0].append(randint(1, 5))
        sorteio[1].append(randint(1, 5))
        sorteio[2].append(randint(1, 5))

    # Exibir os números sorteados na tela.

    for c in range(0, 3):
        print()
        sleep(0.5)
        for l in range(0, 3):
            print(f'    [{sorteio[c][l]:^5}]     ', flush=False, end='')

    # Processa e devolve o resultado do jogo gerado.

    # coluna da esquerda
    if sorteio[0][0] == sorteio[1][0] == sorteio[2][0]:
        goun += 1
        ganhou = aposta * vlc[sorteio[0][0] - 1]
        dindin += aposta * vlc[sorteio[0][0] - 1]
        print()
        print()
        notf(f'voce ganhou R${ganhou:.2f} coluna da esquerda')

    #coluna do meio.
    if sorteio[0][1] == sorteio[1][1] == sorteio[2][1]:
        goun += 1
        ganhou = aposta * vlc[sorteio[0][1] - 1]
        dindin += aposta * vlc[sorteio[0][1] - 1]
        print()
        print()
        notf(f'voce ganhou R${ganhou:.2f} coluna do meio')

    #coluna da direita
    if sorteio[0][2] == sorteio[1][2] == sorteio[2][2]:
        goun += 1
        ganhou = aposta * vlc[sorteio[0][2] - 1]
        dindin += aposta * vlc[sorteio[0][2] - 1]
        print()
        print()
        notf(f'voce ganhou R${ganhou:.2f} coluna da direita')

    #linha de cima
    if sorteio[0][0] == sorteio[0][1] == sorteio[0][2]:
        goun += 1
        ganhou = aposta * vlc[sorteio[0][0] - 1]
        dindin += aposta * vlc[sorteio[0][0] - 1]
        print()
        print()
        notf(f'voce ganhou R${ganhou:.2f} linha de cima')


    #linha do meio
    if sorteio[1][0] == sorteio[1][1] == sorteio[1][2]:
        goun += 1
        ganhou = aposta * vlc[sorteio[1][0] - 1]
        dindin += aposta * vlc[sorteio[1][0] - 1]
        print()
        print()
        notf(f'voce ganhou R${ganhou:.2f} linha do meio')


    #linha de baixo
    if sorteio[2][0] == sorteio[2][1] == sorteio[2][2]:
        goun += 1
        ganhou = aposta * vlc[sorteio[2][0] - 1]
        dindin += aposta * vlc[sorteio[2][0] - 1]
        print()
        print()
        notf(f'voce ganhou R${ganhou:.2f} linha de baixo')


    #diagonal \
    if sorteio[0][0] == sorteio[1][1] == sorteio[2][2]:
        goun += 1
        ganhou = aposta * vd[sorteio[0][0] - 1]
        dindin += aposta * vd[sorteio[0][0] - 1]
        print()
        print()
        notf(f'voce ganhou R${ganhou:.2f} diagonal')


    #diagonal /
    if sorteio[0][2] == sorteio[1][1] == sorteio[2][0]:
        goun += 1
        ganhou = aposta * vd[sorteio[0][2] - 1]
        dindin += aposta * vd[sorteio[0][2] - 1]
        print()
        print()
        notf(f'voce ganhou R${ganhou:.2f} diagonal')


    # fez um "w"
    if sorteio[0][0] == sorteio[1][0] == sorteio[2][0] == sorteio[1][1] == sorteio[2][2] == sorteio[1][2] == sorteio[0][2]:
        goun += 1
        ganhou = aposta * vw[sorteio[0][0] - 1]
        dindin += aposta * vw[sorteio[0][0] - 1]
        print()
        print()
        notf(f'voce ganhou R${ganhou:.2f} vitória "w" ')

    
    if goun == 0:
        notf('Você não ganhou nada')
    return dindin

