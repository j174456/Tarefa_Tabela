from Rota import Rota

# Este é um projeto incremental. A cada aula é pedido mais uma parte.
# Aqui você deve entregar relativo às aulas 8 e 9.
# Em grupo de 3 pessoas. Apenas 1 deve enviar. O nome dos três
# inegrantes deve estar junto com o código fonte.

rota = Rota()
# # tempo em ms
t = 2000
# # Explicação do método abaixo.
rota.espera(t)
# Ao ser chamada, esta função deve fazer uma espera de t milisegundos.
# Você não deve usar sleep. Você deve usar o time.time().
# Além disso, a cada segundo, deve ser impresso uma mensagem conforme
# mostrado abaixo

# Esperando : 0
# Esperando : 1000
# Esperando : 2000
# Esperando : 3000
# Esperando : 4000
# Esperando : 5000
# Esperando : 6000
# Esperando : 7000
# Esperando : 8000
# Esperando : 9000
# Esperando : 10000
# Cada linha deve aparecer no milisegundo correto. No caso, uma nova
# linha a cada 1000 ms. Note que o tempo pode ser maior, ou menor, mas que,
# a cada 1000 ms uma mensagem de espera é impressa na tela.
# Seu código deve ter o seguinte formato. Primeiramente, deve ser lido
# o valor do ms de entrada (tin), através do time.time()
# depois, calcula-se a variação de tempo delta que é
# delta = tempo corrente - tin
# enquanto delta < t
#     mede o delta novamente.
# ao sair do laço, delta vale t.
# note que o delta vai sempre crescendo. Toda a vez que delta
# valer 1000, 2000, 3000, etc, deve ser impressa uma única vez
# a mensagem Esperando: x000ms
# Número esperado de linhas: 8

# #
n = 8
max_coord = 400
rota.randomCoords(n, max_coord)
print(rota)
# # A função acima cria uma sequência de n coordenadas aleatórias
# # dentro de uma rota. Primeiramente, o conjunto de coordenadas é
# # zerado. Após isso, são geradas coordenadas aleatórias. A coordenada
# # gerada é (x,y) onde x é um valor aleatório entre 1 e max_coord e y
# # também é um valor aleatório entre 1 e max_coord.
# # Abaixo o resultado do print(rota)
# # (334, 39)->(288, 128)->(348, 315)->(345, 263)->(241, 316)->(2, 135)->(309, 231)->(107, 341)->(334, 39)
# # Número esperado de linhas: 6
# rota.maximo()
print(rota.maximo())
# # Esta função encontra o valor máximo em x (max_x) para as coordenadas da rota
# # o valor máximo em y (max_y) para as coordenadas da rota. A função devolve a
# # tupla (max_x,max_y)
# # O que foi impresso:
# # (352, 343)
# # Número esperado de linhas: 10

# # imprimir a rota criada.
filename = "rotaA.png"
rota.desenha(filename).show()
# # Esta função deve criar uma imagem de tamanho adequado,
# # um pouco maior que (max_x,max_y) e imprimir uma linha reta
# # entre as coordenadas. Uma linha reta entre a primeira e a segunda
# # coordenada. Uma linha reta entre a segunda e a terceira coordenada e
# # assim sucessivamente até a última coordenada, que deve ser conectada com
# # a primeira. A imagem deve ser um pouco maior que (max_x,max_y) pois deve
# # haver uma pequena margem em branco do lado esquerdo, do lado direito e embaixo.
# # Além disso, na parte debaixo deve estar escrito o comprimento da rota.
# # Tudo deve ser criado como uma Image do pacote PIL (pillow). Ao fim
# # a imagem deve ser salva no arquivo com nome 'filename' passado como parâmetro
# # e devolvida por um return. No caso, foi dado um .show() na imagem que veio
# # do método.

# # Cria um novo conjunto de coordenadas aleatórios e imprime
n = 10
max_coord = 400
rota.randomCoords(n, max_coord)
rota.desenha("rota10.png").show()
# # implementar uma função de otimização
rota.otimiza()
rota.desenha("rota10_Otimizada.png").show()


# # A função rota.otimiza() otimiza a rota. Ela troca os elementos de posição de
# # maneira a reduzir o comprimento. Pode usar
# # a função otimiza que foi disponibilizada na aula passada.
# # Porém o ideal é que ela seja melhorada.


# # Vamos criar uma rota com n coordenadas aleátórias entre 0 e 400.
# def executa(size):
#     rota1 = Rota()
#     rota1.randomCoords(size, 400)
#     rota1.desenha("rota"+str(size)+".png").show()
#     rota1.otimiza()
#     rota1.desenha("rota"+str(size)+"_otimizada.png").show()


# executa(int(input("Digite o número de pontos:")))

# # Veja a rota antes e depois da otimização para valores maiores de n,
# # como 30, 50 ou 100.
# # Baseado na imagem resultante, proponha melhorias para a função rota.otimiza()