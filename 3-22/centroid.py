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

numClusters = int(input("\n\nHow many clusters do you want: "))
clusterPoints = getClusterPoints(numClusters)

centroids = []

def getAllClusterPoints():

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

    for cluster in allClusterPoints:
        xSum = 0
        ySum = 0
        numPts = len(cluster)

        for point in cluster:
            xSum += point[0]
            ySum += point[1]

        centroids.append([xSum/numPts, ySum/numPts])

getAllClusterPoints()

reassignment = True
numLoop = 0

while reassignment == True:

    reassignment = False
    totalDist = 0

    for i in range (len(allClusterPoints)):

        dist = calcSquaredDistance(allClusterPoints[i][0][0], allClusterPoints[i][0][1], centroids[i][0], centroids[i][1])
        totalDist += dist

        for j in range (1, len(allClusterPoints[i])):

            totalDist += calcSquaredDistance(allClusterPoints[i][j][0], allClusterPoints[i][j][1], centroids[i][0], centroids[i][1])

            for k in range (len(centroids)):
                if (k != i):
                    newDist = calcSquaredDistance(allClusterPoints[i][j][0], allClusterPoints[i][j][1], centroids[k][0], centroids[k][1])
                    if (newDist < dist): 
                        reassignment = True
                        break
                    
            if(reassignment):
                break
        if(reassignment):
            break
    
    numLoop += 1
    allClusterPoints = []
    centroids = []
    clusterPoints = getClusterPoints(numClusters)
    getAllClusterPoints()

print("\nNum Iterrations: ", numLoop)
print("\nCentroids: ", centroids)
print("\nSum of squared Distances: ", totalDist, "\n\n")