import pandas as pd

sat = pd.read_excel("SAT/satScores.xlsx")

mean = sat['SAT Scores'].mean()
mode = sat['SAT Scores'].mode()
median = sat['SAT Scores'].median()
maximum = sat['SAT Scores'].max()
minimum = sat['SAT Scores'].min()



print("Mean: " + str(mean))
print("Median: " + str(median))
print("Mode: " + str(mode[0]))
print("Range: " + str(maximum - minimum))

