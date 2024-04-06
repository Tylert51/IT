import math
import pandas as pd
import random
coords = pd.read_csv("3-22/coordinates.csv")


xCoords = coords['xCoords']
yCoords = coords['yCoords']

allClusterPoints = []

def getClusterPoints(n):
    clusterPoints = []

    for i in range (n):
        randIndex = random.randint(0, len(xCoords) - 1)
        x = xCoords[randIndex]
        y = yCoords[randIndex]
        coord = [x, y]

        clusterPoints.append(coord)

        allClusterPoints.append([])

    return clusterPoints


def calcSquaredDistance(x1, y1, x2, y2):
    xDiff = x2 - x1
    yDiff = y2 - y1

    dist = (math.pow(xDiff, 2) + math.pow(yDiff, 2))

    return dist

clusterPoints = getClusterPoints(2)


for i in range (len(xCoords)):
    minIndex = 0
    
    xCoord = xCoords[i]
    yCoord = yCoords[i]

    minDist = calcSquaredDistance(xCoord, yCoord, clusterPoints[0][0], clusterPoints[0][1])

    for c in range (1, len(clusterPoints) ):
        dist = calcSquaredDistance(xCoord, yCoord, clusterPoints[c][0], clusterPoints[c][1])
        if(dist < minDist):
            minDist = dist
            minIndex = c


    allClusterPoints[minIndex].append([xCoord, yCoord])

print(allClusterPoints)


    

        




# for i in range(0, len(xCoords)):
    
#     distA = calcSquaredDistance(ax, ay, xCoords[i], yCoords[i])
#     distB = calcSquaredDistance(bx, by, xCoords[i], yCoords[i])

#     if distA < distB: 
#         aCluster.append(i)
#         aDist += distA
#     else:
#         bCluster.append(i)
#         bDist += distB


# print("\nLatitude 1: ", ax)
# print("Longitude 1: ", ay, "\n")

# print("Latitude 2: ", bx)
# print("Longitude 2: ", by, "\n")

# print("Squared Distance: ", aDist + bDist, "\n")