from collections import deque

class Node:
    def __init__(self, d):
        self.data = d
        self.left = None
        self.right = None

# -------- Print Tree Level-wise --------
def print_tree(root):
    q = deque([root])
    print("\nTree Structure (Level-wise):")
    while q:
        size = len(q)
        while size > 0:
            n = q.popleft()
            print(n.data, end=" ")
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
            size -= 1
        print()

# -------- DFS Preorder --------
def preorder(root):
    if root:
        print(root.data, end=" ")
        preorder(root.left)
        preorder(root.right)

# -------- Input --------
n = int(input("Enter number of nodes: "))
values = input("Enter node values (level order): ").split()

# -------- Tree Creation --------
root = Node(values[0])
q = deque([root])
i = 1

while i < n:
    cur = q.popleft()
    cur.left = Node(values[i])
    q.append(cur.left)
    i += 1
    if i < n:
        cur.right = Node(values[i])
        q.append(cur.right)
        i += 1

# -------- Output --------
print_tree(root)

print("\nDFS Preorder Traversal:")
preorder(root)
