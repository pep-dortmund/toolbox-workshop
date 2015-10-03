from collections import Counter

with open('text.txt') as f:
    words = f.read().split()

counts = Counter(words)

for key, count in counts.most_common(20):
    print("{}: {}".format(key, count))
