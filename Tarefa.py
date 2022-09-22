from Tabela import Tabela
from TabelaBD import TabelaBD
from Linha import Linha

# Fazer em grupo de 3 pessoas. Uma pessoa apenas deve enviar o trabalho no
# moodle. O nome dos três integrantes deve estar dentro de do arquivo Tarefa.py

# A tarefa desta semana é uma continuação da implementação da tabela.
# Primeiramente deve existir um construtor da classe Tabela com
# zero ou um argumentos. Se for executado
teste = Tabela()
# deve ser criada uma tabela vazia.
# por outro lado, se for passado no construtor o nome de um arquivo,
# a tabela deve ser carregada deste arquivo.
# Veja o exemplo:
teste = Tabela("carros.txt")
print(teste)
# O arquivo carros.txt que possui a tabela vai ser dado para você.
# Veja abaixo o formato do arquivo.
# ['placa','ano','marca','modelo']
# ['PAF1A79',2020,'volkswagem','gol']
# ['OWH2Z46',2017,'volkswagem','polo']
# ['IRD3T61',2016,'volkswagem','gol']
# ['XTP8W51',2020,'chevrolet','onix']
# . . ..
#
# A primeira linha possui o cabeçalho da tabela, e as próximas linhas
# contêm os registros da tabela. O seu construtor deve funcionar nestes dois
# casos.
#
#
# Agora você deve criar um método em Tabela que salva a tabela em um arquivo.
teste.writeFile("saida.txt")

# Este método cria um arquivo contendo os dados da tabela. Ele deve funcionar de maneira
# a que os dados escritos no arquivo possam novamente subir para uma tabela, conforme
# mostrado abaixo:

teste = Tabela("saida.txt")
print(teste)

# Seu grupo também ira receber um arquivo contendo uma tabela com os candidatos
# a deputado federal por São Paulo.
#
# Você deve criar agora uma classe TabelaBD dentro de um arquivo TabelaBD.py.
# Esta classe herda Tabela.
# O comando abaixo carrega a tabela de um arquivo.
candidatos = TabelaBD("candidados_dep_fed.txt")
#
# O proximo método criado dentro de TabelaBD faz a contagem. O método
# recebe como parâmetro o nome do cabeçalho de uma coluna, neste caso,
# partido. O método conta quantas vezes um determinado valor aparece
# na coluna partido. Veja o resultado abaixo:
result = candidatos.conta("Partido")
print(result)

# ['Partido', 'numero']
# ----------------------
# ['UP', 1]
# ['PC do B', 2]
# ['Agir', 5]
# ['Cidadania', 9]
# ['PCB', 9]
# ['PSTU', 9]
# ['PCO', 10]
# ['PV', 12]
# ['Rede', 21]
# ['PMB', 25]
# ['DC', 34]
# ['PSOL', 39]
# ['PDT', 48]
# ['PSDB', 49]
# ['PMN', 50]
# ['PSD', 51]
# ['Solidariedade', 54]
# ['PT', 58]
# ['Novo', 63]
# ['PSC', 64]
# ['MDB', 66]
# ['AGIR', 66]
# ['PROS', 66]
# ['União', 69]
# ['Republicanos', 69]
# ['PRTB', 69]
# ['PSB', 70]
# ['Patriota', 71]
# ['PL', 71]
# ['PP', 71]
# ['Avante', 74]
# ['Podemos', 74]
# ['PTB', 75]
#
#  Alguns detalhes sobre o método conta. O resultado de conta é uma tabela,
# logo, também pode ser escrita em um arquivo.
result.writeFile("CandidatosPorPartido.txt")
#
# A tabela possui uma coluna chamada, onde cada ítem distinto aparece uma
# única vez. A outra coluna chama-se número. Esta coluna possui o número de
# repetições de cada ítem. A tabela está ordenada em ordem crescente do número.
#
# Veja que, uma vez implementado, o método pode ser chamado novamente em outros
# contextos.


carros = TabelaBD("carros.txt")

# Na chamada abaixo, a função faz a contagem dos carros de cada ano.
result = carros.conta("ano")
result.ordena_por("ano")
print(result)

# ['ano', 'numero']
# ------------------
# [2015, 5]
# [2016, 11]
# [2017, 12]
# [2018, 7]
# [2019, 7]
# [2020, 8]

# Na chamada abaixo, a função faz a contagem dos carros por marca
result = carros.conta("marca")
print(result)
# ['marca', 'numero']
# --------------------
# ['volkswagem', 14]
# ['fiat', 16]
# ['chevrolet', 20]
#
# Já na chamada abaixo, a função faz a contagem dos carros por modelo
result = carros.conta("modelo")
print(result)

# ['modelo', 'numero']
# ---------------------
# ['cruze', 3]
# ['pulse', 3]
# ['polo', 4]
# ['jetta', 4]
# ['gol', 6]
# ['argo', 6]
# ['camaro', 6]
# ['moby', 7]
# ['onix', 11]

# O proximo método a ser implementado na classe TabelaBD é o método select.
# Este método recebe o cabeçalho de uma coluna e um valor. O resultado são
# todas as linhas em que a coluna escolhida tenha o valor dado. O resultado
# também é uma tabela.
# No exemplo abaixo, são selecionados todos os carros cujo ano seja 2015.
result = carros.select("ano", 2015)
print(result)
#
# Veja o resultado abaixo
# ['placa', 'ano', 'marca', 'modelo']
# ------------------------------------
# ['QNS7Y56', 2015, 'fiat', 'argo']
# ['HNX7T11', 2015, 'chevrolet', 'onix']
# ['IIO2T74', 2015, 'chevrolet', 'onix']
# ['RMB9U12', 2015, 'chevrolet', 'camaro']
# ['AUS1U85', 2015, 'fiat', 'pulse']
#
# No exemplo a seguir, são selecionados todas as linhas em cadidatos,
# cujo partido seja igual a PR.
result = candidatos.select("Partido", "PV")
print(result)
# Veja o resultado abaixo:
# ['Nome', 'Partido', 'Número']
# ------------------------------
# ['Adalberto Maluf', 'PV', 4344]
# ['Henri Esses', 'PV', 4318]
# ['Julio Ferraz', 'PV', 4300]
# ['Márcia Rebeschini', 'PV', 4377]
# ['Mônica Buava Mandato Animal', 'PV', 4366]
# ['Patricia Vedrano', 'PV', 4310]
# ['Piauilino', 'PV', 4355]
# ['Raulf Naure', 'PV', 4388]
# ['Regina Gonçalves', 'PV', 4343]
# ['Ricardo Melenchon Viva Verde', 'PV', 4334]
# ['Thame', 'PV', 4342]
# ['Veterinário Wilson Grassi', 'PV', 4330]
#
# O comando abaixo salva o resultado em um arquivo e depois carrega novamnte

result.writeFile("candidatosPV.txt")
candidatosPV = TabelaBD("candidatosPV.txt")
print(candidatosPV)
