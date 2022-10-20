class Coordenada:
    def __init__(self,*coordenadas):
        #print(str(coordenadas))
        if len(coordenadas) == 0:
            self.x = 0
            self.y = 0
        else:
            self.x = coordenadas[0][0]
            self.y = coordenadas[0][1]
    
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
            