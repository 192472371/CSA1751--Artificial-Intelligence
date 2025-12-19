import heapq

def gbfs(graph, heuristic, start, goal):
    open_list = []
    closed = set()

    # (heuristic, node)
    heapq.heappush(open_list, (heuristic[start], start))

    print("\nGBFS Traversal Order:")

    while open_list:
        h, current = heapq.heappop(open_list)
        print(current, end=" ")

        if current == goal:
            print("\nGoal reached!")
            return

        if current in closed:
            continue

        closed.add(current)

        for neighbor, _ in graph.get(current, []):
            if neighbor not in closed:
                heapq.heappush(open_list, (heuristic[neighbor], neighbor))

    print("\nGoal not reachable")
graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ").strip()
    edges = input(
        f"Enter neighbors of {node} with cost (example: B,2 C,4): "
    ).strip().split()

    graph[node] = []
    for e in edges:
        if e:
            neigh, cost = e.split(',')
            graph[node].append((neigh, int(cost)))

print("\nEnter heuristic values:")
for _ in range(n):
    node = input("Node: ").strip()
    h = int(input(f"Heuristic value of {node}: "))
    heuristic[node] = h

start = input("\nEnter start node: ").strip()
goal = input("Enter goal node: ").strip()

gbfs(graph, heuristic, start, goal)
