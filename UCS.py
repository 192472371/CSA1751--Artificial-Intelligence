import heapq

def ucs(graph, start, goal):
    pq = []
    visited = set()

    heapq.heappush(pq, (0, start))

    while pq:
        cost, node = heapq.heappop(pq)

        if node == goal:
            print("Goal reached with cost:", cost)
            return

        if node not in visited:
            visited.add(node)

            for neigh, wt in graph.get(node, []):
                if neigh not in visited:
                    heapq.heappush(pq, (cost + wt, neigh))

    print("Goal not reachable")
graph = {}
n = int(input("Enter number of nodes: "))

for _ in range(n):
    node = input("Enter node: ").strip()
    edges = input(f"Enter neighbors of {node} with cost (ex: B,2 C,1): ").split()
    
    graph[node] = []
    for e in edges:
        if e:
            neigh, cost = e.split(',')
            graph[node].append((neigh, int(cost)))

start = input("Enter start node: ").strip()
goal = input("Enter goal node: ").strip()

ucs(graph, start, goal)
