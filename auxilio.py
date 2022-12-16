from json import lerArquivo

def listaVazia(conteudo):
    if len(conteudo) == 0:
        enterContinuar()
        return 1     

def selecionarID():
    id = int(input("Digite a ID do jogo: "))
    return id 

def gerarID():
    jogos = lerArquivo()
    if len(jogos) == 0:
        return 1
    return jogos[-1]["_Jogos__id"] + 1

def enterContinuar():
    input('Pressione ENTER para continuar...')


