from dados import *
from engine import *
from interface import *
from time import sleep
from os import system

valaposta = [0.50, 1.00, 2.00, 4.00, 5.00, 10.00, 20.00, 50.00, 100.00]


#Verificação do arquivo que ira conter o dinheiro do jogador.
a = arquivo_existe('carteira.txt')
if a == False:
    criar_arquivo('carteira.txt')

dinheiro_inicio = 0


# Colocar o dinheiro salvo no arquivo dentro da variável do dinheiro no jogo.
with open('carteira.txt', 'r')as arc:
    for valor in arc:
        dinheiro_inicio = float(valor)

dinheiro_fim = dinheiro_inicio

notf('CAÇA NIQUEL DO CHRONODD')
notf(f'Voçê possui R${dinheiro_fim:.2f}')

#Adicionando dinheiro a carteira.
b = soun('Quer adicionar dinheiro a carteira? ')

if b == 'S':
    x()
    dinheiro_fim = adicionar_dinheiro(dinheiro_fim)
    with open('carteira.txt', 'w') as arc:
        arc.write(str(dinheiro_fim).replace(',', '.'))

dinheiro_inicio = dinheiro_fim

while True:
    x()
    c = menu(dinheiro_fim)
    

    if c == 0:
        x()
        with open('carteira.txt', 'w') as arc:
            arc.write(str(dinheiro_fim).replace(',', '.'))
        break

    elif valaposta[c] > dinheiro_fim:
        x()
        notf('\033[31mVocê não possui o dinheiro suficiente para essa aposta\033[m')
        notf('FIM DE JOGO')
        with open('carteira.txt', 'w') as arc:
            arc.write(str(dinheiro_fim).replace(',', '.'))
        break


    else:
        x()
        dinheiro_fim -=  valaposta[c]
        dinheiro_fim = roleta(dinheiro_fim, valaposta[c])
        sleep(2)

notf(f'Você começou com R${dinheiro_inicio:.2f}')
notf(f'Você terminou com R${dinheiro_fim:.2f}')
print()

notf('ATÉ LOGO ^-^')
