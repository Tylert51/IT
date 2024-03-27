import math
import pandas as pd
import random
coords = pd.read_csv("3-22/coordinates.csv")


xCoords = coords['xCoords']
yCoords = coords['yCoords']

randIndex = random.randint(0, len(xCoords) - 1)
ax = xCoords[randIndex]
ay = yCoords[randIndex]

randIndex = random.randint(0, len(xCoords) - 1)
bx = xCoords[randIndex]
by = yCoords[randIndex]

aCluster = []
bCluster = []

def calcSquaredDistance(x1, y1, x2, y2):
    xDiff = x2 - x1
    yDiff = y2 - y1

    dist = (math.pow(xDiff, 2) + math.pow(yDiff, 2))

    return dist

aDist = 0
bDist = 0

for i in range(0, len(xCoords)):
    
    distA = calcSquaredDistance(ax, ay, xCoords[i], yCoords[i])
    distB = calcSquaredDistance(bx, by, xCoords[i], yCoords[i])

    if distA < distB: 
        aCluster.append(i)
        aDist += distA
    else:
        bCluster.append(i)
        bDist += distB


print("\nLatitude 1: ", ax)
print("Longitude 1: ", ay, "\n")

print("Latitude 2: ", bx)
print("Longitude 2: ", by, "\n")

print("Squared Distance: ", aDist + bDist, "\n")





