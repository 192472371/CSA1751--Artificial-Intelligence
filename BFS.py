from collections import deque

class Node:
    def _init_(self, d):
        self.data = d
        self.left = None
        self.right = None

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

def bfs(root):
    q = deque([root])
    print("\nBFS Traversal:")
    while q:
        n = q.popleft()
        print(n.data, end=" ")
        if n.left: q.append(n.left)
        if n.right: q.append(n.right)

# -------- Input --------
n = int(input("Enter number of nodes: "))
values = input("Enter node values (level order): ").split()

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

print_tree(root)
bfs(root)
