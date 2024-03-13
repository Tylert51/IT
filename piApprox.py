import math

def estimatePi(iterations):
    sum = 0
    for i in range(1, iterations + 1):
        sum += (  (1 / ((2 * i) - 1) )  *  math.pow( (-1), i + 1 )  )
        

    print(sum)
    
estimatePi(4)
print( 1 - (1 / 3) + (1 / 5) - (1 / 7) )
