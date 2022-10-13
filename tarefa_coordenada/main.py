import random

from Coordenada import Coordenada
from Rota import Rota


# Crie uma classe coordenada. Esta classe possui internamente
# dois valores inteiros (x,y). Veja os exemplos abaixo:
cord1 = Coordenada()
print(cord1)
# Com este construtor é criada uma coordenada na posicão (0,0).
# o valor impresso no print é (0,0).
#
cord1 = Coordenada((5, 5))
print(cord1)
# Neste caso é criada uma coordenada na posição (5,5).
# Se for passado mais de um elemento no construtor, deve ser
# subir uma exceção: número de parâmetros errado. Veja o exemplo abaixo:
try:
    cord1 = Coordenada(5, 5)
except Exception as e:
    print(e)

# O que é impresso:
# Numero de argumentos errado: 2
# Toda vez que houver um erro, deve ser lançada uma exceção
# Se o argumento passado não for uma tupla, também deve ser lançada uma exceção:
try:
    cord1 = Coordenada([5, 5])
except Exception as e:
    print(e)
# deve ser impresso
# Parâmetro não é uma tupla
# A tupla deve possuir dois elementos. e os elementos devem
# ser números
try:
    cord1 = Coordenada((2, 2, 2))
except Exception as e:
    print(e)
# Exceção
# Numero de coordenadas inválido:3
try:
    cord1 = Coordenada((2, "a"))
except Exception as e:
    print(e)
# Exceção
# Elemento da tupla não é int or float

# Crie um método distância que recebe como parâmetro outra coordenada.
# Você deve calcular a distância euclidiana entre as duas coordeandas.

cord1 = Coordenada((0, 0))
cord2 = Coordenada((3, 4))
print(cord1)
print(cord2)
print(cord1.distancia(cord2))
# valos impresso
# (0, 0)
# (3, 4)
# 5.0

cord1 = Coordenada((0.1, 0.1))
cord2 = Coordenada((3.1, 4.2))
print(cord1)
print(cord2)
print(cord1.distancia(cord2))
# valor impresso
# (0.1, 0.1)
# (3.1, 4.2)
# 5.0803543183522155a

#Você deve criar uma classe Rota composta por uma lista de coordenadas.
rota1: Rota = Rota()
rota1.addCoord(Coordenada((0, 0)))
rota1.addCoord(Coordenada((0, 4)))
rota1.addCoord(Coordenada((3, 4)))
print(rota1)

# o que deve ser impresso:
# (0, 0)->(0, 4)->(3, 4)->(0, 0)
# Note que a primeira coordenada é impressa duas vezes.
# Isso quer dizer que a rota começa na primeira coordenada,
# passa nas demais, depois retorna para a primeira coordenada. Isso é uma
# rota fechada. Apesar disso, o número de coordenadas é 3.

# a proxima função diz o comprimento da rota. Ela é composta das somas das distâncias
# entre as coordenadas.
# No exemplo anterior é a disância entre as coordenadas abaixo:
# (0, 0)->(0, 4)->(3, 4)->(0, 0)
print(rota1.comprimento())

# neste caso deve ser impresso 12 que representa a soma dos três lados
# dos triangulo, um com tamanho 3, outro com 4 e o último com 5.





# Você deve criar um método clone que tira uma cópia da rota.
rota2 = rota1.copy()
rota1.addCoord(Coordenada((3, 3)))
print(rota1)
print(rota2)
# Será impresso:
# (0, 0)->(0, 4)->(3, 4)->(3, 3)->(0, 0)
# (0, 0)->(0, 4)->(3, 4)->(0, 0)

# Você deve criar um método que emabaralha as coordenads da rota
rota1.shuffle()
print(rota1)

# Agora vamos criar uma rota com 50 coordenadas aleátórias entre 0 e 100.

rota1 = Rota()
for i in range(50):
    x = random.randrange(1, 100)
    y = random.randrange(1, 100)
    cord = Coordenada((x, y))
    rota1.addCoord(cord)
print(rota1.comprimento())



# A seguinte função otimiza (reduz) o comprimento da rota.
print("---Otimiza----")
mudou  = True
while(mudou):
    mudou = False
    for i in range(100000):
        rotaAux = rota1.copy()
        rotaAux.shuffle()
        if rotaAux.comprimento()<rota1.comprimento():
            rota1 = rotaAux
            print(rota1.comprimento())
            mudou = True


# Você deve melhorar esta função. Fazer otimizar mais rápido.
