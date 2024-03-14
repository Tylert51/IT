import random

def rollDie(money):
    games = 0
    max = money

    while (money > 0):
        games += 1

        roll1 = random.randint(1,6)
        roll2 = random.randint(1,6)

        print("game " + str(games) + "\nroll 1: " + str(roll1) + "\nroll 2: " + str(roll2))

        if(roll1 + roll2 == 7):
            money +=4
        else:
            money -= 1

        if(money > max):
            max = money

        print("money: $" + str(money) + "\n")

    print("iterations: " + str(games) + "\nmax money: " + str(max))


mon = input("Enter the amount of money you would like to put down: ")
rollDie(int(mon))

