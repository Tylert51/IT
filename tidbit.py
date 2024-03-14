import pandas as pd

def roundN(num, nDecimal):
    return format(num, "." + str(nDecimal) + "f")


months = []
totalBalOwe = []
monthlyInterest = []
monthlyPrincipal = []
monthlyPay = []
balAfterPay = []

m = 1

price = float(input("Enter a purchase price: "))
bal = price

downPay = 0.1 * price
monthlyPayments = 0.05 * (price - downPay)
monthInt = bal * (0.12 / 12)
monthPrin = monthlyPayments - monthInt



while(bal > 0):

    if (m == 1):
        bal = bal - downPay

    
    monthInt = bal * (0.12 / 12)
    bal += monthInt
    totalBalOwe.append("$" + roundN(bal, 2))

    monthlyInterest.append("$" + roundN(monthInt , 2))

    monthPrin = monthlyPayments - monthInt
    monthlyPrincipal.append("$" + roundN(monthPrin, 2))

    monthlyPay.append("$" + roundN(monthlyPayments, 2))

    
    if(float(roundN(bal - monthlyPayments, 2)) <= 0):
        
        monthlyPay.pop()
        monthlyPay.append("$" + roundN(bal, 2))
        monthlyPrincipal.pop()
        monthlyPrincipal.append("$" + roundN(bal - monthInt, 2))

        bal=0
    else:
        bal = bal - monthlyPayments

    balAfterPay.append("$" + roundN(bal, 2))

    months.append(m)
    m+=1


data = {'month': months, 'current total balance owed': totalBalOwe, 'interest owed per month': monthlyInterest, 'monthly principal': monthlyPrincipal, 'monthly pay': monthlyPay, 'balance after pay': balAfterPay}


df = pd.DataFrame(data)


print(df)

