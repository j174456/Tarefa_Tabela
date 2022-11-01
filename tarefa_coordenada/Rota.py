import math
import random
import time
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

    def espera(self, tempo):
        tempo = tempo/1000
        start = time.time()
        delta = 0
        while (delta < tempo):
            delta = time.time() - start
    # acrescentar print de segundo

    def randomCoords(self, quantidade, intervalo):
        self.coordenadas = []
        newCoor = ()
        for i in range(quantidade):
            newCoor = (random.randrange(1, intervalo), random.randrange(1, intervalo))
            self.addCoord(newCoor)

    def maximo(self):
        max_x = 0
        max_y = 0
        for coordenada in self.coordenadas:
            if max_x == 0 or max_x < coordenada[0]:
                max_x = coordenada[0]
            if max_y == 0 or max_y < coordenada[1]:
                max_y = coordenada[1]
        maxCoor = (max_x, max_y)
        return str(maxCoor)

    def desenha(self, nome):
        pass

    def otimiza(self):
        pass

        
        
