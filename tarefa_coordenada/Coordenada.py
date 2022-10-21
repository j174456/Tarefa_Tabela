from math import dist


class Coordenada:
    def __init__(self, *coordenada):
        args = []

        if len(coordenada) > 1:
            raise TypeError('Número de parâmetros errado.')
        for valor in coordenada:
            for item in valor:
                args.append(item)

        if len(coordenada) == 0:
            self.x = 0
            self.y = 0
        else:
            if len(args) > 2:
                raise TypeError('Numero de argumentos errado: ' + str(len(args)))
            elif (type(args[0]) is not int and type(args[0]) is not float) or (
                    type(args[1]) is not int and type(args[1]) is not float):
                raise TypeError('Elemento da tupla não é int ou float')
            elif type(coordenada[0]) is not tuple:
                raise TypeError('Parâmetro não é uma tupla')
            else:
                self.x = args[0]
                self.y = args[1]

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

    def get_coord(self):
        return self.x, self.y

    def distancia(self, coord):
        return dist(self.get_coord(), coord.get_coord())
