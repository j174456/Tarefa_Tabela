import math
import random
class Rota:
    def __init__(self):
        self.coordenadas = []
    
    def addCoord(self, coordenada):
        self.coordenadas.append(coordenada)
    
    def __str__(self):
        string = ""
        for x in self.coordenadas:
            string += str(x)+ "->"
        string += str(self.coordenadas[0])
        return string
    
    def comprimento(self):
        comprimento = 0
        aux = None
        rota = self.coordenadas.copy()
        rota.append(self.coordenadas[0])
        for x in rota:
            if aux is not None:
                d = math.sqrt((x.x - aux.x)**2 + (x.y - aux.y)**2)
                comprimento += d
            aux = x
         
        return str(comprimento)
    
    def copy(self):
        aux = Rota()
        aux.coordenadas = self.coordenadas.copy()
        return aux

    def shuffle(self):
        random.shuffle(self.coordenadas)

        
        
