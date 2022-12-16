from json import lerArquivo, salvarArquivo
import os
from auxilio import gerarID, listaVazia

nome_arquivo = "computador.json"
lista = None

class Computador:
    __id : str
    __placaVideo : str
    __ram : str
    __processador : str
    __placaMae : str
    __armazenamento : str
    
    def getID(self):
        return self.__id
    
    def setID(self, id):
        self.__id = id
    
    def getplacaVideo(self):
        return self.__placaVideo
    
    def setplacaVideo(self, placaVideo):
        self.__placaVideo = placaVideo

    def getRam(self):
        return self.__ram
    
    def setRam(self, ram):
        self.__ram = ram

    def getProcessador(self):
        return self.__processador
    
    def setProcessador(self, processador):
        self.__processador = processador

    def getPlacamae(self):
        return self.__placaMae
    
    def setPlacamae(self, placaMae):
        self.__placaMae = placaMae
    
    def getArmazenamento(self):
        return self.__armazenamento

    def setArmazenamento(self, armazenamento):
        self.__armazenamento = armazenamento
        

    def cadastrarComputador(self) -> dict:
        print("----- CADASTRO DO COMPUTADOR -----") 
        self.setID(gerarID())
        self.setplacaVideo(input('Deseja Qual a Placa de Vídeo? '))
        self.setRam(input('Quantidade de Memoria RAM? '))
        self.setProcessador(input('Deseja Qual processador? '))
        self.setPlacamae(input('Deseja qual Placa Mãe? '))
        self.setArmazenamento(input('Quantidade de Armazenamento? '))
        print('----------------------------------')
        return

    Computador = lerArquivo()
    Computador.append(self.__dict__)
    salvarArquivo(Computador)

    def alterarComputador(self):
        os.system('cls')
        print("----- EDIÇÂO DO COMPUTADOR -----")
    escolha = int(input("Qual deseja alterar? "))
    for p in lista:
        if p['id'] == escolha:
            p['placaVideo'] = str(input('Deseja Qual a Placa de Vídeo: '))
            p['ram'] = str(input('Quantidade de Memoria RAM: '))
            p['processador'] = str(input('Deseja Qual processador: '))
            p['placaMae'] = str(input('Deseja qual Placa Mãe: '))
            p['armazenamento'] = str(input('Quantidade de Armazenamento: '))
    
    def mostrarComputadores(self):
        Computador = lerArquivo()
        if listaVazia(Computador) != 1:
            for pc in Computador:
                print('----- COMPUTADOR -----')
                print(f'ID: {pc["__id"]}')
                print(f'Placa de video: {pc["__placaVideo"]}')
                print(f'RAM: {pc["__ram"]}')
                print(f'Processador: {pc["__processador"]}')
                print(f'Placa mãe: {pc["__placaMae"]}')
                print(f'Armazenamento: {pc["__armazenamento"]}')
                print("----------------")
        print("Pressione enter para Continuar...")

    def deletarComp(self):
        print("----- EXCLUSÃO DE COMPUTADOR -----")
        call = lerArquivo()
        pos = str(input("Insira o ID do computador que deseja exluir: "))
        for i in call:
            if i['id'] == pos:
                local = call.index(i)
                call.pop(local)
        salvarArquivo(call)
        print("Pressione enter para Continuar...")

    def geradorID():
        data = lerArquivo()
        listId = []
        if len(data) == 0:
            return 1
        else:
            for i in range(len(data)):
                listId.append(data[i]['id'])
            return max(listId)+1

pc = Computador()

        
                
                


        