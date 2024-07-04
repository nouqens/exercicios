from a155a.lib.interface import *
from a155a.lib.arquivo import *

arq = 'pessoas.txt'

if not arqexiste(arq):
    print('Arquivo criado')
    criarArq(arq)

while True:
    r = menu(['Listar Pessoas', 'Cadastrar Pessoas', 'Sair'])
    if r == 1:
        # lista de pessoas cadastradas
        lerArq(arq)
    elif r == 2:
        # cadastrar novo usuario
        cabecalho('Novo cadastro')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)

    elif r== 3:
        print('Finalizando...')
        break
    else:
        print('\033[31mERRO! DIGITE UM NUMERO VALIDO!\033[m')