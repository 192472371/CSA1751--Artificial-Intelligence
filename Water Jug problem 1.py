from collections import deque

def water_jug(jug1, jug2, target):
    visited = set()
    q = deque()

    # (jug1_amount, jug2_amount, path)
    q.append((0, 0, []))
    visited.add((0, 0))

    while q:
        x, y, path = q.popleft()
        path = path + [(x, y)]

        if x == target or y == target:
            print("Solution path:")
            for step in path:
                print(step)
            return

        # All possible states
        states = [
            (jug1, y),                      # Fill Jug1
            (x, jug2),                      # Fill Jug2
            (0, y),                         # Empty Jug1
            (x, 0),                         # Empty Jug2
            (x - min(x, jug2 - y), y + min(x, jug2 - y)),  # Pour Jug1 -> Jug2
            (x + min(y, jug1 - x), y - min(y, jug1 - x))   # Pour Jug2 -> Jug1
        ]

        for state in states:
            if state not in visited:
                visited.add(state)
                q.append((state[0], state[1], path))

    print("No solution found")

jug1 = int(input("Enter capacity of Jug 1: "))
jug2 = int(input("Enter capacity of Jug 2: "))
target = int(input("Enter target amount: "))

water_jug(jug1, jug2, target)
