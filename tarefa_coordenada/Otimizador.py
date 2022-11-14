import random
from Rota import Rota
import time
from matplotlib import pyplot
import math

# Ainda não é para entregar. Em grupo de 3 pessoas.
# Vai ser pedido para entregar futuramente, junto
# com o conteúdo da aula 11.


class Otimizador:
    # Este é o construtor do otimizador. Você pode adicionar código aqui
    # se julgar necessário.
    def __init__(self):
        self.plt = pyplot

    # Este método de otimização já está implementado.
    # Toda vez que o comprimento for atualizado para um valor menor, é
    # necessário salvar o comprimento e o tempo gasto na função
    # para fazer o gráfico.
    # Ao final da execução, é necessário usar o matplotlib (pyplot)
    # para gerar o gráfico (comprimento X tempo).
    # Deve ser feito o mesmo para a função de otimização 'aleatório'
    # e 'otimizadorGrupo1'
    # As três séries temporais devem ser salvas em um mesmo gráfico,
    # conforme figuras 'Resultado_10x.py'
    # Seu grupo pode adicionar código nesta função se julgar necessário.
    # O mesmo para os outros dois otimizadores.
    # A linha do gráfico referente ao 'SingleSwap' deve estar em preto.
    # A linha do gráfico referente ao 'Aleatório' deve estar em verde.
    # A linha do gráfico referente ao 'otimizadorGrupo1' deve estar em azul
    # e deve ser mais grossa que a linha dos outros algoritmos.
    # Todas as linhas devem iniciar no tempo zero e terminar no tempo final.
    def singleSwap(self, rota: Rota, time_ms: int):
        # Inicia a partir de uma rota não otimizada
        rota.shuffle()
        # Tempo de entrada na função.
        tin = round(time.time() * 1000)
        # Tempo gasto na função.
        delta_ms = round(time.time() * 1000) - tin
        minComprimento = rota.comprimento()
        while delta_ms < time_ms:
            # atualiza delta
            delta_ms = round(time.time() * 1000) - tin
            size_rota = len(rota.coordenadas)
            pos1 = random.randrange(0, size_rota)
            pos2 = random.randrange(0, size_rota)
            swap(rota, pos1, pos2)
            if rota.comprimento() < minComprimento:
                minComprimento = rota.comprimento()
            else:
                # desfaz o swap
                swap(rota, pos1, pos2)

    def aleatorio(self, rota: Rota, time_ms: int):
        # inicia a partir de uma rota não otimizada
        rota.shuffle()
        tin = round(time.time() * 1000)
        delta_ms = round(time.time() * 1000) - tin
        minComprimento = rota.comprimento()
        while delta_ms < time_ms:
            delta_ms = round(time.time() * 1000) - tin
            rotaAux = rota.copy()
            rotaAux.shuffle()
            if rotaAux.comprimento() < minComprimento:
                rota.coordenadas = rotaAux.coordenadas
                minComprimento = rota.comprimento()

    # Aqui você deve usar sua criatividade e propor um algoritmo de
    # otimização. O algoritmo deixado é apenas um exemplo.
    # Ao fixar um label para o seu grupo
    # dê um nome para o seu grupo que o diferencie dos demais.
    # Veja a Figura Resultado_10x.png. No lugar de 'Algoritmo do Grupo 1'
    # deve estar um nome curto que identifique o seu grupo. O nome deve
    # ser composto de um nome dos integrantes. Exemplo:
    # Rodrigo_Ivan_Celso
    def Arthur_Joaop_Myrelle(self, rota: Rota, time_ms: int):
        # inicia a partir de uma rota não otimizada
        optimizing = True
        optRoute = []
        follow = []
        auxList= rota.coordenadas.copy()
        follow = rota.coordenadas.copy()
        closedIndexes = []
        optRoute.append(auxList[0])
        closedIndexes.append(0)
        closerIndex = 0
        closerDistance = 99999
        tin = round(time.time() * 1000)
        delta_ms = round(time.time() * 1000) - tin
        while optimizing or delta_ms < time_ms:
            delta_ms = round(time.time() * 1000) - tin
            if len(optRoute) == len(rota.coordenadas):
                optimizing = False
            for x in range(0,len(auxList)):
                if x not in closedIndexes:
                    d = math.sqrt((optRoute[-1].x - auxList[x].x)**2 + (optRoute[-1].y - auxList[x].y)**2)
                    if d < closerDistance:
                        closerIndex = x
                        closerDistance = d 
            if 1<len(optRoute) < len(rota.coordenadas):
                print(len(optRoute))
                follow[closerIndex] = auxList[len(optRoute)-1] 
                follow[len(optRoute)-1] = auxList[closerIndex]
            closedIndexes.append(closerIndex)
            optRoute.append(auxList[closerIndex])
            closerDistance = 99999
            
        
        rota.coordenadas = []
        rota.coordenadas.extend(optRoute)
            



    # Esta função deve salvar o gráfico. A função não deve ser alterada.
    # O objetivo final é colocar vários algoritmos vindos de grupos diferentes
    # num mesmo gráfico e depois esta função irá salvar a solução com todos os gráficos.
    def salvaFigura(self, filename):
        self.plt.tight_layout()
        self.plt.legend()
        self.plt.savefig(filename)


def swap(rota: Rota, pos1: int, pos2: int):
    aux = rota.coordenadas[pos1]
    rota.coordenadas[pos1] = rota.coordenadas[pos2]
    rota.coordenadas[pos2] = aux


# Cria uma rota Vazia.
r = Rota()
# Número de coordenadas da rota
size = int(input("Digite o número de vértices:"))
# valor máximo x e y para a coordenada
r.randomCoords(size, 400)
# Cria o otimizador
opt = Otimizador()
# Tempo de otimização em ms
time_ms = int(input("Digite o tempo em ms:"))
# Otimiza por single swap
opt.singleSwap(r, time_ms)
# Otimização aleatório
opt.aleatorio(r, time_ms)
# Otimização feita por seu grupo
opt.Arthur_Joaop_Myrelle(r, time_ms)
opt.salvaFigura("Resultado_" + str(size) + ".png")
