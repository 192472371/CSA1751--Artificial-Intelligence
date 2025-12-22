from collections import deque

def pour(state, i, j, cap):
    state = list(state)
    amount = min(state[i], cap[j] - state[j])
    state[i] -= amount
    state[j] += amount
    return tuple(state)

def three_jug_any_goal(start, cap, goal):
    q = deque()
    visited = set()

    q.append((start, [start]))
    visited.add(start)

    while q:
        state, path = q.popleft()

        # ✅ Goal condition: goal amount in ANY jug
        if goal in state:
            print("Solution path:")
            for s in path:
                print(s)
            print("\nGoal achieved:", state)
            return

        for i in range(3):
            for j in range(3):
                if i != j:
                    new_state = pour(state, i, j, cap)
                    if new_state not in visited:
                        visited.add(new_state)
                        q.append((new_state, path + [new_state]))

    print("No solution possible")
cap = list(map(int, input("Enter capacities of 3 jugs: ").split()))
start = tuple(map(int, input("Enter initial water in jugs: ").split()))
goal = int(input("Enter goal amount: "))

three_jug_any_goal(start, cap, goal)

