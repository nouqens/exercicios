from a155a.lib.interface import *
def arqexiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True

def criarArq(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')

def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('ERRO AO LER O ARQUIVO!')
    else:
        cabecalho('Pessoas Cadastradas')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}\t{dado[1]:>3} anos')
    finally:
        a.close()
def cadastrar(arq, nome = 'Desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever no arquivo!')
        else:
            print(f'Novo registro de {nome}!')
            a.close()

