import calcDistance

with open("coords.txt") as file:
    for coord in file:
        

        arr = coord.split(", ")

        print(calcDistance.calcDistance(arr, [2,5]))


