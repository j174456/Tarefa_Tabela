from PIL import Image
from sklearn import preprocessing
import random

points = []
states = []
color = dict()

file = open("coordenadas.txt", "r")
documentCoordinates = file.readlines()
file.close()

#-----------------------Define coordinate-------------------------#
for line in documentCoordinates:
  splitLine = line.split(';')
  latitudeLine = (splitLine[3])
  longitudeLine = (splitLine[4].strip()) 

  coordinateLine = [latitudeLine, longitudeLine]
  states += [splitLine[1]]
  
  points.append(coordinateLine)

#-----------------------Normalize coordinates-------------------------#
scaler = preprocessing.MinMaxScaler(feature_range=(0, 1000))
coordinateNormalize = scaler.fit_transform(points)

#-----------------------Generate Random Color-------------------------#
for state in states:
  if state not in color:
    randomColor = (random.choice(range(0, 255)),random.choice(range(0, 255)),random.choice(range(0, 255)))
    color[state] = randomColor

img = Image.new("RGB",(1001,1001),"white")
pixels = img.load()

#-----------------------Create image from coordinate------------------#
for posicao in range(0,len(coordinateNormalize)):
  latitude = coordinateNormalize[posicao][0]
  longitude = coordinateNormalize[posicao][1]
  
  pixels[latitude, longitude] = color[states[posicao]]

rotated = img.rotate(90)
rotated.save("Brasil.png")