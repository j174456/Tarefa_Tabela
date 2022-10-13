class Coordenada:
    def __init__(self,*coordenadas):
        if coordenadas is None:
            self.x = 0
            self.y = 0
        else:
           self.x = coordenadas[0]
           self.y = coordenadas[1] 