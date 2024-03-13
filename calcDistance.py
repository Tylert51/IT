import math

def calcDistance(pt1, pt2): 
    sum = 0

    for i in range(len(pt1)):
        sum += (float(pt2[i]) - float(pt1[i])) ** 2

    return math.sqrt(sum)



