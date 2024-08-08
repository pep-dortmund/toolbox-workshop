# begin solution
with open("text.txt") as f:
    words = f.read().split()

counts = dict()

for word in words:
    # Nehme Häufigkeit des Worts oder 0,
    # wenn das Wort noch nicht verzeichnet ist
    freq = counts.get(word, 0)

    counts[word] = freq + 1


def get_count(x):
    return x[1]


result = sorted(counts.items(), key=get_count, reverse=True)

for key, count in result[:20]:
    print(f"{key}: {count}")
# end solution
