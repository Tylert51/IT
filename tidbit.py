import pandas as pd

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



while(bal >= 0):

    if (m == 1):
        bal = bal - downPay

    totalBalOwe.append(bal)
    
    monthInt = bal * (0.12 / 12)
    monthlyInterest.append(monthInt)

    monthPrin = monthlyPayments - monthInt
    monthlyPrincipal.append(monthPrin)

    monthlyPay.append(monthlyPayments)

    bal = round(bal - monthlyPayments, 2)
    balAfterPay.append(bal)

    months.append(m)
    m+=1


data = {'month': months, 'current total balance owed': totalBalOwe, 'interest owed per month': monthlyInterest, 'monthly principal': monthlyPrincipal, 'monthly pay': monthlyPay, 'balance after pay': balAfterPay}


df = pd.DataFrame(data)


print(df)











