bits = input("Enter a bit: ")
num = int(input("How many places do you want it to be shifted: "))

def shiftLeft(bits, n):
    for i in range(0, n):
        bits = bits[1:] + bits[0:1]

    print("left shift:", bits)

def shiftRight(bits, n):
    for i in range(0, n):
        bits = bits[len(bits) - 1 : len(bits)] + bits[0 : len(bits) - 1]

    print("right shift:", bits)


shiftLeft(bits, num)
shiftRight(bits, num)

