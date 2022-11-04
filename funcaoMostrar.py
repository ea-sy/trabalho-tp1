import json
import os
#nome do arquivo
nome_arquivo = "computador.json"

def lerArquivo() -> list:
    arq = open(nome_arquivo, 'r', encoding='utf-8')
            # ler e retronar com str
    data = arq.read()
                # load = carregar
                # load(S) = str
    return json.loads(data)

# Salvar os arquivos no json
def salvarArquivo(computador: list):
    arq = open(nome_arquivo, 'w+', encoding='utf-8')
                #dumps = armazena os objetos em um arquivo
    data = json.dumps(computador, indent=4)
    arq.write(data)
    arq.close()

# Programa principal
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
    input('Pressione ENTER para continuar...')