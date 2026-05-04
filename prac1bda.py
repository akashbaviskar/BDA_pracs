#Prac2 Develop a MapReduce program to calculate the frequency of a given word in a given file.
from functools import reduce
from collections import defaultdict
def word_frequency(filename):
    with open(filename, 'r') as f:
        text = f.read()

    words = text.lower().split()

    # MAP phase — each word → (word, 1)
    mapped = list(map(lambda word: (word, 1), words))

    # SHUFFLE phase — group by word
    shuffled = defaultdict(list)
    for word, count in mapped:
        shuffled[word].append(count)

    # REDUCE phase — sum all counts per word
    reduced = {word: reduce(lambda a, b: a + b, counts)
               for word, counts in shuffled.items()}

    return reduced

# --- Create a sample file to test ---
with open("sample.txt", "w") as f:
    f.write("hello world hello python world hello big data big data analytics")

result = word_frequency("sample.txt")

print("=" * 40)
print("       WORD FREQUENCY RESULT")
print("=" * 40)
for word, count in sorted(result.items(), key=lambda x: -x[1]):
    print(f"  {word:<20} : {count}")
print("=" * 40)
#--------x---------------------

from functools import reduce
from collections import defaultdict

text = "hello world hello python world hello"
words = text.lower().split()

# MAP: each word → (word, 1)
mapped = [(word, 1) for word in words]
print("MAP:", mapped)

# SHUFFLE: group counts by word
shuffled = defaultdict(list)
for word, count in mapped:
    shuffled[word].append(count)
print("SHUFFLE:", dict(shuffled))

# REDUCE: sum counts per word
result = {word: reduce(lambda a, b: a + b, counts)
          for word, counts in shuffled.items()}
print("REDUCE:", result)
#------------x------------------------