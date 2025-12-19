import heapq

# ---------- A* FUNCTION ----------
def astar(graph, heuristic, start, goal):
    open_list = []
    closed = set()

    # (f, g, node)
    heapq.heappush(open_list, (heuristic[start], 0, start))

    print("\nA* Traversal Order:")

    while open_list:
        f, g, current = heapq.heappop(open_list)
        print(current, end=" ")

        if current == goal:
            print("\nGoal reached!")
            print("Total cost:", g)
            return

        if current in closed:
            continue

        closed.add(current)

        for neighbor, cost in graph.get(current, []):
            if neighbor not in closed:
                g_new = g + cost
                f_new = g_new + heuristic[neighbor]
                heapq.heappush(open_list, (f_new, g_new, neighbor))

    print("\nGoal not reachable")


# ---------- INPUT GRAPH ----------
graph = {}
heuristic = {}

n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ").strip()
    neighbors = input(
        f"Enter neighbors of {node} with cost (example: B,2 C,4): "
    ).strip().split()

    graph[node] = []
    for item in neighbors:
        if item:
            neigh, cost = item.split(',')
            graph[node].append((neigh, int(cost)))

# ---------- INPUT HEURISTIC ----------
print("\nEnter heuristic values:")
for _ in range(n):
    node = input("Node: ").strip()
    h = int(input(f"Heuristic value of {node}: "))
    heuristic[node] = h

# ---------- START & GOAL ----------
start = input("\nEnter start node: ").strip()
goal = input("Enter goal node: ").strip()

# ---------- CALL A* ----------
astar(graph, heuristic, start, goal)

