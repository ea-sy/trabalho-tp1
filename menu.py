from funcoes import *

while True:
    opcao = menu()
    if opcao == 1:
        cadastrarComputador()
    elif opcao == 2:
        mostrarComputadores()
    elif opcao == 3:
        deletarComp()
    elif opcao == 4:
        selecionarComp()
    elif opcao == 5:
        alterarComputador()
    elif opcao == 6:
        break

