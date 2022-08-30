from dados import *
from os import system


def notf(txt):
    l = '-'*40
    print(f'{l:^47}')
    print(f'{txt:^45}')
    print(f'{l:^47}')

def menu(di):
    #Exibir o menu na tela.
    lst = ['SAIR', 'R$0,50', 'R$1,00', 'R$2,00', 'R$5,00', 'R$10,00', 'R$20,00', 'R$50,00', 'R$100,00']
    print()
    notf(f'Você possui R${di:.2f}')
    notf('Quanto quer apostar?')

    for posicao, item in enumerate (lst):
            print(f'{posicao:<3} --------  {item:<10}')

    #Pegar a opção escolhida pelo usuário.
    while True:
        a = nint('Qual sua opção: ')
        if a < 0 or a > 9:
            print('\033[31mERRO! Por favor, digite uma opção válida\033[m')
            continue
        else:
            return a
            break



def x():
    #Limpa o terminal.
    system('clear')
