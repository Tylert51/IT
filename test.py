import pandas as pd
months = []
totalBalOwe = []
m = 1


price = float(input("Enter a purchase price: "))


for x in range(100):
   months.append(m)
   m += 1


bal = (0.9*price)
totalBalOwe.append(bal)
for x in range(1,100):
   if months[x] % 12 == 0:
       bal += (1.12*bal) - (0.05 * bal)
       totalBalOwe.append(bal)
   else:
       bal -= (0.05 * bal)
       totalBalOwe.append(bal)


interest = []


for x in range(100):
   interest.append(totalBalOwe[x] * .01)


data = {'month': months, 'current total balance owed': totalBalOwe, 'interest owed per month': interest}


df = pd.DataFrame(data)


print(df)
