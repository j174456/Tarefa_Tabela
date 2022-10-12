from PIL import Image
from sklearn import preprocessing
import pandas as pd

img = Image.new("RGB",(1001,1001),"white")
img.save("Brasil.png")

def criarmatriz():
  file = open("coordenadas.txt","r")
  coordenadas = file.read().splitlines()
  file.close()

  for x in range(0,len(coordenadas)):
    coordenadas[x] = coordenadas[x].split(';')
    coordenadas[x][3]= float(coordenadas[x][3])
    coordenadas[x][4]= float(coordenadas[x][4])
  return coordenadas

coordenadaDaLinha = []
pontos=[]

for linha in criarmatriz():
  coordenadaDaLinha = [linha[3], linha[4]]
  pontos.append(coordenadaDaLinha)

scaler = preprocessing.MinMaxScaler(feature_range=(0, 1000))
normalizado = scaler.fit_transform(pontos)
print(str(normalizado))

img = Image.new("RGB",(1001,1001),"white")
pixeis = img.load()
R = 132
G = 245
B = 66

cor = (R,G,B)

for posicao in range(0,len(normalizado)):
  latitude = abs(normalizado[posicao][0])
  longitude = abs(normalizado[posicao][1])
  pixeis[latitude, longitude] = cor

img.save("Brasil.png")