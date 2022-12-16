import json
import os

nome_arquivo = "computador.json"


def lerArquivo() -> list:
    arq = open(nome_arquivo, 'r', encoding='utf-8')
    data = arq.read()
    if len(data) == 0:
        return []
    return json.loads(data)
    
def salvarArquivo(computador: list):
    arq = open(nome_arquivo, 'w+', encoding='utf-8')
    data = json.dumps(computador, indent=4)
    arq.write(data)
    arq.close()

