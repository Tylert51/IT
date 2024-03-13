num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def gcd(a, b):
    if(a > b):
        return gcd(b, a)
    elif a == b:
        return a
    elif a == 0:
        return b
    else:
        remainder = b % a
        print("remainder of " + str(b) + " % " + str(a) + " is " + str(remainder))
        return gcd(remainder, a)
    

print("gcd is " + str(gcd(num1, num2)))

