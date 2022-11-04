import json
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
def cadastrarComputador() -> dict:
    pc = {}
    pc['id'] = str(input('ID do computador: '))
    pc['placaVideo'] = str(input('Deseja Qual a Placa de Vídeo: '))
    pc['ram'] = str(input('Quantidade de Memoria RAM: '))
    pc['processador'] = str(input('Deseja Qual processador: '))
    pc['placaMae'] = str(input('Deseja qual Placa Mãe: '))
    pc['armazenamento'] = str(input('Quantidade de Armazenamento: '))

    computador = lerArquivo()
    computador.append(pc)
    salvarArquivo(computador)