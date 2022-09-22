# Arthur Gallotti Silva Conti | RA: 165942
# João Pedro Coelho de Sousa | RA: 174456
# Myrelle Silva Lopes | RA: 242265
import Tabela
import Linha
import ast

class TabelaBD(Tabela.Tabela):
    def __init__(self):
        super().__init__()
        self._dados = []
        self._cabecalho = Linha()
    
    def __init__(self,arquivo):
        super().__init__(arquivo)
        file = open(arquivo,"r")
        valores = file.readlines()
        file.close
        self._cabecalho = Linha()
        self._cabecalho.append(ast.literal_eval(valores[0]))
        self._dados = []
        for c in range(1,len(valores)):
            self._dados.append(ast.literal_eval(valores[c]))
    
    def conta(self,chave):
        x = dict()
        for i in self._dados:
            if i[chave] in x:
                x[i[chave]] = x[i[chave]] +1
            else:
                x[i[chave]] = 1
        return x

candidatos = TabelaBD("candidados_dep_fed.txt")
result = candidatos.conta("Partido")
print(result)