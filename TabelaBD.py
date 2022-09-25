# Arthur Gallotti Silva Conti | RA: 165942
# João Pedro Coelho de Sousa | RA: 174456
# Myrelle Silva Lopes | RA: 242265
from os import getgrouplist
import Tabela
from Linha import Linha
import ast

class TabelaBD(Tabela.Tabela):
    # Overload n existe, então fazemos a validação via arquivo None
    # e na sequencia chamo o super para usar da superclasse
    def __init__(self, arquivo = None):
        if arquivo is None:
            super().__init__()
        else :
            super().__init__(arquivo)
    
    def conta(self,chave):
        # X será uma tabel pois o retorno tem que ser uma tabela
        obj = dict()
        table = TabelaBD()
        # usando a mesma lógica de index da tabela, pois i[chave] n pega o texto interno
        # mas com o index pegamos o text interno para passar
        self._index = self.cabecalho.index(chave)
        table.add_cabecalho([chave,"numero"])
        # Precisei alterar de _dados para dados, por ser herança da outra classe             
        for i in self.dados:
            if i[self._index] not in obj:
                obj[i[self._index]] = 1
            else:
                obj[i[self._index]] = obj[i[self._index]] +1
        for key,value in obj.items():
            line = Linha()
            line.append([key,value])
            table.addLinha(line)
        return table
    def writeFile(self, path):
        return super().writeFile(path)
    
    def select(self,chave,valor):
        self._index = self.cabecalho.index(chave)
        table = TabelaBD()
        table.add_cabecalho(self.cabecalho.dados)
        for line in self.dados:
            if line[self._index] == valor:
                table.addLinha(line)
        return table