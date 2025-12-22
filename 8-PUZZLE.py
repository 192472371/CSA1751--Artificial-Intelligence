from collections import deque

moves = [(-1,0), (1,0), (0,-1), (0,1)]
move_names = ['Up', 'Down', 'Left', 'Right']

def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

def get_next_states(state):
    next_states = []
    x, y = [(i,j) for i in range(3) for j in range(3) if state[i][j]==0][0]
    for (dx, dy), name in zip(moves, move_names):
        nx, ny = x+dx, y+dy
        if is_valid(nx, ny):
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            next_states.append((tuple(tuple(row) for row in new_state), name))
    return next_states

def bfs_8_puzzle(start, goal):
    start = tuple(tuple(row) for row in start)
    goal = tuple(tuple(row) for row in goal)
    queue = deque([(start, [])])
    visited = set([start])
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        for next_state, move in get_next_states(state):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [move]))
    return None

# ---- Input Start and Goal States ----
print("Enter start state (row-wise, 0 for blank):")
start_state = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(3)]
print("Enter goal state (row-wise, 0 for blank):")
goal_state = [list(map(int, input(f"Row {i+1}: ").split())) for i in range(3)]

solution = bfs_8_puzzle(start_state, goal_state)
if solution:
    print("Moves to solve:", solution)
else:
    print("No solution found")

