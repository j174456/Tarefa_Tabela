import math
import random
import time
from PIL import Image, ImageDraw
from Coordenada import Coordenada

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
            if delta % 1 == 0:
                print("Esperando : " + str(int(delta*1000)))

    def randomCoords(self, quantidade, intervalo):
        self.coordenadas = []
        newCoor = ()
        for i in range(quantidade):
            newCoor = (random.randrange(1, intervalo), random.randrange(1, intervalo))
            self.addCoord(Coordenada(newCoor))

    def maximo(self):
        max_x = 0
        max_y = 0
        for coordenada in self.coordenadas:
            if max_x == 0 or max_x < coordenada.x:
                max_x = coordenada.x
            if max_y == 0 or max_y < coordenada.y:
                max_y = coordenada.y
        maxCoor = (max_x, max_y)
        return str(maxCoor)

    def desenha(self, filename):
        tamanho =  eval(self.maximo())
        x= int(tamanho[0]*1.10)
        y= int(tamanho[1]*1.10)
        img = Image.new('RGB',(x,y),"white")
        for x in range(0,len(self.coordenadas)):
            if x < len(self.coordenadas)-1:
                shape = [(self.coordenadas[x].x,self.coordenadas[x].y),(self.coordenadas[x+1].x,self.coordenadas[x+1].y)]
                img1 = ImageDraw.Draw(img)  
                img1.line(shape, fill ="black", width = 0)
        shape = [(self.coordenadas[len(self.coordenadas)-1].x,self.coordenadas[len(self.coordenadas)-1].y),(self.coordenadas[0].x,self.coordenadas[0].y)]
        img1 = ImageDraw.Draw(img)  
        img1.line(shape, fill ="black", width = 0)
        img1.text((int(x*0.9),int(y*0.9)), "custo:" + self.comprimento(), fill="black", font=None, anchor=None, spacing=0, align="left")
        img.save("./" + filename)
        return img

    def otimiza(self):
        aux = list()
        for x in self.coordenadas:
            aux.append((x.x,x.y))
        aux.sort()
        self.coordenadas = []
        for x in aux:
            self.addCoord(Coordenada(x))

        
        
