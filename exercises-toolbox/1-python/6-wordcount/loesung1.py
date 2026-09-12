# begin solution
# open the file and write the content, split into words, into the variable words
with open("text.txt") as f:
    words = f.read().split()

counts = dict()  # define an empty dictionary

# loop over all words, add an entry if it isn't in the dict,
# otherwise add 1 to the counter
for word in words:
    if word in counts:
        counts[word] += 1
    else:
        counts[word] = 1


# define a function to get the value for each key
def get_count(x):
    return x[1]


# sort the words by their values,
# reverse the order to have the words with highest count first
result = sorted(counts.items(), key=get_count, reverse=True)

# iterate over the first 20 entries
for key, count in result[:20]:
    print(f"{key}: {count}")
# end solution
