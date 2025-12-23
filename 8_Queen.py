N = 8
board = [-1] * N   # board[row] = column of queen
solutions = 0

def is_safe(row, col):
    for i in range(row):
        # Same column or diagonal
        if board[i] == col or \
           abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve(row):
    global solutions

    if row == N:
        solutions += 1
        print_solution()
        return

    for col in range(N):
        if is_safe(row, col):
            board[row] = col
            solve(row + 1)
            board[row] = -1   # backtrack

def print_solution():
    print("\nSolution", solutions)
    for r in range(N):
        for c in range(N):
            if board[r] == c:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()

# -------- RUN --------
solve(0)
print("\nTotal Solutions:", solutions)
