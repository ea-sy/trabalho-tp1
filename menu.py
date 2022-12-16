from funcoes import *
from auxilio import *


def menu():
    os.system('cls')
    print('----- SISTEMA DE COMPUTADORES -----')
    print('1 - Cadastrar Computador')
    print('2 - Mostrar todos os Computadores')
    print('3 - Deletar Computador')
    print('4 - Selecionar Computador por ID')
    print('5 - Alterar o Computador')
    print('6 - Sair')
    print('-----------------------------------')
    return int(input('Escolha uma opção: '))

while True:
    opcao = menu()
    if opcao == 1:
        Computador.cadastrarComputador()
    elif opcao == 2:
        Computador.mostrarComputadores()
    elif opcao == 3:
        Computador.deletarComp()
    elif opcao == 4:
        Computador.selecionarID()
    elif opcao == 5:
        Computador.alterarComputador()              
    elif opcao == 6:
        break