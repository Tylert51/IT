import matplotlib.pyplot as plt

freq = [6, 9, 9, 1]
numFreq = sum(freq)
percent = []

for i in freq:
    percent.append((i / numFreq) * 100)


tv = ["ABC", "CBS", "NBC", "FOX"]
positions = range(len(tv))

plt.bar(positions, percent)
plt.xticks(positions, tv)

plt.title("Percent Distribution")

plt.xlabel("TV Channels")
plt.ylabel("Percent Frequency (%)")

plt.show()