import math
from collections import Counter

# -------- DATASET --------
data = [
    ['Sunny', 'Hot', 'High', 'Weak', 'No'],
    ['Sunny', 'Hot', 'High', 'Strong', 'No'],
    ['Overcast', 'Hot', 'High', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Cool', 'Normal', 'Strong', 'No'],
    ['Overcast', 'Cool', 'Normal', 'Strong', 'Yes'],
    ['Sunny', 'Mild', 'High', 'Weak', 'No'],
    ['Sunny', 'Cool', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'Normal', 'Weak', 'Yes'],
    ['Sunny', 'Mild', 'Normal', 'Strong', 'Yes'],
    ['Overcast', 'Mild', 'High', 'Strong', 'Yes'],
    ['Overcast', 'Hot', 'Normal', 'Weak', 'Yes'],
    ['Rain', 'Mild', 'High', 'Strong', 'No']
]

attributes = ['Outlook', 'Temperature', 'Humidity', 'Wind']

# -------- ENTROPY --------
def entropy(data):
    labels = [row[-1] for row in data]
    counts = Counter(labels)
    ent = 0
    for c in counts.values():
        p = c / len(data)
        ent -= p * math.log2(p)
    return ent

# -------- INFORMATION GAIN --------
def info_gain(data, index):
    total = entropy(data)
    values = set(row[index] for row in data)
    weighted = 0
    for v in values:
        subset = [row for row in data if row[index] == v]
        weighted += (len(subset) / len(data)) * entropy(subset)
    return total - weighted

# -------- ID3 WITH TREE PRINT --------
def id3(data, attrs, prefix=""):
    labels = [row[-1] for row in data]

    # Leaf node
    if labels.count(labels[0]) == len(labels):
        print(prefix + labels[0])
        return

    if not attrs:
        # If no attributes left, return majority
        majority = Counter(labels).most_common(1)[0][0]
        print(prefix + majority)
        return

    # Best attribute
    gains = [(info_gain(data, i), i) for i in range(len(attrs))]
    _, best = max(gains)

    print(prefix + attrs[best])
    values = sorted(set(row[best] for row in data))  # sort for consistent output

    for i, val in enumerate(values):
        subset = [row[:best] + row[best+1:] for row in data if row[best] == val]
        sub_attrs = attrs[:best] + attrs[best+1:]
        branch = "└── " if i == len(values)-1 else "├── "
        if subset:
            print(prefix + branch + f"{val}", end="")
            # Only print arrow if it’s a leaf
            if len(set(row[-1] for row in subset)) == 1:
                print(f" → {subset[0][-1]}")
            else:
                print()
                id3(subset, sub_attrs, prefix + ("    " if i == len(values)-1 else "│   "))

# -------- RUN --------
print("\nDecision Tree:\n")
id3(data, attributes)
