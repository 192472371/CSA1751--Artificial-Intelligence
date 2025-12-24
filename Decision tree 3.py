import math
from collections import Counter

# ---------------- DATASET ----------------
data = [
    ['True', 'Hot',  'High',   'No'],
    ['True', 'Hot',  'Normal', 'No'],
    ['False','Hot',  'High',   'Yes'],
    ['False','Cool', 'Normal', 'Yes'],
    ['False','Cool', 'High',   'No'],
    ['True', 'Cool', 'Normal', 'Yes'],
    ['True', 'Cool', 'High',   'No'],
    ['False','Hot',  'Normal', 'Yes']
]

attributes = ['A1', 'A2', 'A3']

# ---------------- ENTROPY ----------------
def entropy(rows):
    labels = [row[-1] for row in rows]
    counts = Counter(labels)
    ent = 0
    for c in counts.values():
        p = c / len(rows)
        ent -= p * math.log2(p)
    return ent

# ---------------- INFORMATION GAIN ----------------
def information_gain(rows, index):
    total_entropy = entropy(rows)
    values = set(row[index] for row in rows)

    weighted_entropy = 0
    for v in values:
        subset = [row for row in rows if row[index] == v]
        weighted_entropy += (len(subset) / len(rows)) * entropy(subset)

    return total_entropy - weighted_entropy

# ---------------- ID3 ALGORITHM ----------------
def id3(rows, attrs, depth=0):
    labels = [row[-1] for row in rows]

    # All same class → leaf
    if labels.count(labels[0]) == len(labels):
        print(" →", labels[0])
        return

    # Choose best attribute
    gains = [information_gain(rows, i) for i in range(len(attrs))]
    best_index = gains.index(max(gains))
    best_attr = attrs[best_index]

    print("\n" + "│   " * depth + best_attr)

    values = set(row[best_index] for row in rows)

    for v in values:
        print("│   " * depth + "├──", v, end="")
        subset = [row[:best_index] + row[best_index+1:]
                  for row in rows if row[best_index] == v]

        id3(subset, attrs[:best_index] + attrs[best_index+1:], depth + 1)

# ---------------- RUN ----------------
print("\nDecision Tree:\n")
id3(data, attributes)
