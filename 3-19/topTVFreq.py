import matplotlib.pyplot as plt

freq = [6, 9, 9, 1]
tv = ["ABC", "CBS", "NBC", "FOX"]
positions = range(len(tv))

plt.bar(positions, freq)
plt.xticks(positions, tv)

plt.title("Frequency Distribution")

plt.xlabel("TV Channels")
plt.ylabel("Frequencies")

plt.show()