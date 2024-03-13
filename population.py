import math

def population (initial, gRate, growthTime, time): 
    print( initial * math.pow(gRate, (time / growthTime)))

population(500, 2, 6, 12)