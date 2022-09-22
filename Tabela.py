# Arthur Gallotti Silva Conti | RA: 165942
# João Pedro Coelho de Sousa | RA: 174456
# Myrelle Silva Lopes | RA: 242265

import ast
from Linha import Linha

class Tabela:
    def __init__(self):
        self.dados = []
        self.cabecalho = Linha()
    
    def __init__(self,arquivo):
        file = open(arquivo,"r")
        valores = file.readlines()
        file.close
        self.cabecalho = Linha()
        self.cabecalho.append(ast.literal_eval(valores[0]))
        self.dados = []
        for c in range(1,len(valores)):
            self.dados.append(ast.literal_eval(valores[c]))
        

    def add_cabecalho(self, lista):
        self.cabecalho.append(lista)

    def addLinha(self, linha):
        # print(f"Linha:{linha}\nSize:{len(self.cabecalho)}\ndados:{self.dados}")
        if len(linha) == len(self.cabecalho):
            self.dados.append(linha)
        else:
            print("Tamanhos incompatíveis")


    def __str__(self):
        string = str(self.cabecalho.dados) + "\n" 
        string += "---------------------------------------\n"
        for i in range(0,len(self.dados)):
            string += str(self.dados[i]) + "\n"
        return string
  
    def ordena_por(self, valor):
        self._index = self.cabecalho.index(valor)
        self.dados.sort(key=self.ordenando_por)
    
    def ordenando_por(self,dados):
        return dados[self._index]

    def writeFile(self,path):
        self.addItem(self.cabecalho.dados,path)
        for linha in self.dados:
            self.addItem(str(linha),path)

    def addItem(self,item,path):
        file = open(path,"a")
        file.write(str(item)+"\n")
        file.close()


#teste = Tabela("carros.txt")
#print(teste)

#teste.writeFile("saida.txt")

#teste = Tabela("saida.txt")
#print(teste)