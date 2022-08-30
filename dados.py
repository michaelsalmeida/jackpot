


def soun (txt):
    # Ler e validar input de resposta s(sim) ou n(não).
    while True:
        a = str(input(f'{txt}: ')).strip().upper()
        if a not in 'SN':
            print('\033[31mERRO! Por favor, digite S ou N\033[m')

        else:
            return a
            break



def nint (txt):
    # Ler e validar respostas só com números inteiros.
    while True:
            try:
                a = int(input(txt))

            except:
                print('\033[31mERRO! Por favor, digite um número inteiro\033[m')
                continue

            else:
                return a
                break

def nfloat (txt):
    # Ler e validar respostas só com números reais.
    while True:
            try:
                a = float(input(txt))

            except:
                print('\033[31mERRO! Por favor, digite um número inteiro\033[m')
                continue

            else:
                return a
                break



def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')

    except:
        print('\033[31mArquivo NÃO encontrado. Criando o arquivo\033[m')
        return False

    else:
        print('\033[32mArquivo encontrado\033[m')
        return True


def criar_arquivo(nome):
    try:
        a = open(nome,'wt+')

    except:
        print('\033[31mERRO AO CRIAR O ARQUIVO\033[m')

    else:
        print('\033[32mARQUIVO CRIADO COM SUCESSO\033[m')


def adicionar_dinheiro(din):
    a = nfloat('Quanto quer adicionar na carteira?: ')

    # Colocando o valor modificado no arquivo .txt
    with open('carteira.txt', 'w') as arc:
        arc.write(str(din + a))
    print(f'\033[32m{a:.2f} adicionado com sucesso a sua carteira.\033[m')

    b = din + a
    return b

