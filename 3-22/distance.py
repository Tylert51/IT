import math
import pandas as pd

coords = pd.read_csv("3-22/coordinates.csv")

baseX = 40.688889
baseY = -73.976944

xCoords = coords['xCoords']
yCoords = coords['yCoords']

def calcDistance(x1, y1, x2, y2):
    xDiff = x2 - x1
    yDiff = y2 - y1

    dist = (math.pow(xDiff, 2) + math.pow(yDiff, 2))

    return dist

totalDist = 0

for i in range(len(xCoords)):
    
    totalDist += calcDistance(baseX, baseY, float(xCoords[i]), float(yCoords[i]))

print(totalDist)

