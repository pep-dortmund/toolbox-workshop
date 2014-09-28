with open('text.txt') as f:
    words = f.read().split()

counts = dict()

for word in words:
    # Nehme Häufigkeit des Worts oder 0,
    # wenn das Wort noch nicht verzeichnet ist
    freq = counts.get(word, 0)

    counts[word] = freq + 1

result = sorted(counts.items(), key=lambda x: x[1], reverse=True)

for key, count in result:
    print("{}: {}".format(key, count))
