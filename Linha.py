# Arthur Gallotti Silva Conti | RA: 165942
# João Pedro Coelho de Sousa | RA: 174456
# Myrelle Silva Lopes | RA: 242265


class Linha:

    def __init__(self):
        self.dados = []

    def append(self, valor):
        if type(valor) is not list:
            self.dados.append(valor)
        else:
            self.dados.extend(valor)

    def __str__(self):
        return f"{self.dados}({str(len(self.dados))})"
    
    def __len__(self):
        return len(self.dados)
    
    def index(self,value):
        return self.dados.index(value)
    
    def __getitem__(self,key):
        return self.dados[key]
