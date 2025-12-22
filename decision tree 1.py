import math
from collections import Counter

def entropy(data):
    total = len(data)
    counts = Counter(row[-1] for row in data)
    ent = 0
    for c in counts.values():
        p = c / total
        ent -= p * math.log2(p)
    return ent

def info_gain(data, attr):
    total_entropy = entropy(data)
    values = set(row[attr] for row in data)
    weighted_entropy = 0

    for v in values:
        subset = [row for row in data if row[attr] == v]
        weighted_entropy += (len(subset) / len(data)) * entropy(subset)

    return total_entropy - weighted_entropy

def id3(data, attributes):
    labels = [row[-1] for row in data]

    if labels.count(labels[0]) == len(labels):
        return labels[0]

    if not attributes:
        return Counter(labels).most_common(1)[0][0]

    gains = [(info_gain(data, a), a) for a in attributes]
    best_attr = max(gains)[1]

    tree = {best_attr: {}}

    for v in set(row[best_attr] for row in data):
        subset = [row for row in data if row[best_attr] == v]
        remaining = [a for a in attributes if a != best_attr]
        tree[best_attr][v] = id3(subset, remaining)

    return tree

def print_tree(tree, indent=""):
    if not isinstance(tree, dict):
        print(indent + "→", tree)
        return

    for attr, branches in tree.items():
        print(indent + f"[Attribute {attr}]")
        for value, subtree in branches.items():
            print(indent + f" ├─ {value}")
            print_tree(subtree, indent + " │  ")
data = [
    ['Sunny','Hot','High','Weak','No'],
    ['Sunny','Hot','High','Strong','No'],
    ['Overcast','Hot','High','Weak','Yes'],
    ['Rain','Mild','High','Weak','Yes'],
    ['Rain','Cool','Normal','Weak','Yes'],
    ['Rain','Cool','Normal','Strong','No'],
    ['Overcast','Cool','Normal','Strong','Yes']
]

attributes = [0,1,2,3]

tree = id3(data, attributes)
print_tree(tree)
