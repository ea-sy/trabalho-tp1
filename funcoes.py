import os
import json

nome_arquivo = "computador.json"

def lerArquivo() -> list:
    arq = open(nome_arquivo, 'r', encoding='utf-8')
    data = arq.read()
                # read = retorna str
                # load = carregar
                # load(S) = str
    return json.loads(data)

def salvarArquivo(computador: list) -> list:
    arq = open(nome_arquivo, 'w+', encoding='utf-8')
        # open = abre e printa o conteudo
    data = json.dumps(computador, indent=4)
    arq.write(data)
        # write = substitui conteudo exitente no arquivo
    arq.close()

def cadastrarComputador() -> dict:
    pc = {} # dic vazio
    #chaves 
    pc['id'] = geradorID()
    pc['placaVideo'] = str(input('Deseja Qual a Placa de Vídeo? '))
    pc['ram'] = str(input('Quantidade de Memoria RAM? '))
    pc['processador'] = str(input('Deseja Qual processador? '))
    pc['placaMae'] = str(input('Deseja qual Placa Mãe? '))
    pc['armazenamento'] = str(input('Quantidade de Armazenamento? '))

    computador = lerArquivo()
    computador.append(pc)
              #append = add isso em pc
    salvarArquivo(computador)

def menu():
    os.system('cls')
    print(10 * '-=-')
    print('1 - Cadastrar Computador')
    print('2 - Mostrar todos os Computadores')
    print('3 - Deletar Computador')
    print('4 - Selecionar Computador por ID')
    print('5 - Alterar o Computador')
    print('6 - Sair')
    print(10 * '-=-')
    return int(input('Escolha uma opção: '))

def mostrarComputadores():
    os.system('cls')
    print(10 * '-=-')
    computador = lerArquivo()
    for pc in computador:
        print(f'ID: {pc["id"]}')
        print(f'Placa de video: {pc["placaVideo"]}')
        print(f'RAM: {pc["ram"]}')
        print(f'Processador: {pc["processador"]}')
        print(f'Placa mãe: {pc["placaMae"]}')
        print(f'Armazenamento: {pc["armazenamento"]}')
        print(10 * '-=-')
    continuar()

def continuar():
    input('Pressione ENTER para continuar...')

def deletarComp():
    call = lerArquivo()
    pos = str(input("Insira o ID do computador que deseja exluir: "))
    for i in call:
        if i['id'] == pos:
            local = call.index(i)
                        # index = retorna a posição na primeira ocorrencia do valor, no caso o ID.
            call.pop(local)
            # pop = remove o elemento da posição especificada
    salvarArquivo(call)
    continuar()

def alterarComputador():
    lista = lerArquivo()
    escolha = int(input("Qual deseja alterar? "))
    for p in lista:
        if p['id'] == escolha:
            p['placaVideo'] = str(input('Deseja Qual a Placa de Vídeo: '))
            p['ram'] = str(input('Quantidade de Memoria RAM: '))
            p['processador'] = str(input('Deseja Qual processador: '))
            p['placaMae'] = str(input('Deseja qual Placa Mãe: '))
            p['armazenamento'] = str(input('Quantidade de Armazenamento: ')) 
    salvarArquivo(lista)
    continuar()
    
    

def selecionarComp():
    lista = lerArquivo()
    componente = int(input("Informe o ID do Computador: "))
    for i in lista:
        if i["id"] == componente:
            print(f'Computador selecionado: {i}')
    continuar()

def geradorID():
    data = lerArquivo()
    listId = []
    if len(data) == 0:
        return 1
    else:
        for i in range(len(data)):
            listId.append(data[i]['id'])
        return max(listId)+1

    
            
            


    