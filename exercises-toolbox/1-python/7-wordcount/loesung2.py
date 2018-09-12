with open('text.txt') as f:
    words = f.read().split()

counts = dict()

for word in words:
    # Nehme Häufigkeit des Worts oder 0,
    # wenn das Wort noch nicht verzeichnet ist
    freq = counts.get(word, 0)

    counts[word] = freq + 1

result = sorted(counts, key=counts.get, reverse=True)

for key in result[:20]:
    print("{}: {}".format(key, counts[key]))
