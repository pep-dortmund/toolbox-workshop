with open('text.txt') as f:
    words = f.read().split()

counts = dict()

for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1
        
def get_count(x):
    return x[1]

result = sorted(counts.items(), key=get_count, reverse=True)

for key, count in result[:20]:
    print("{}: {}".format(key, count))
