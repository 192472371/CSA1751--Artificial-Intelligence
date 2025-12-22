def minimax(depth, nodeIndex, isMax, values, height):
    
    # Base case: leaf node
    if depth == height:
        return values[nodeIndex]

    if isMax:
        return max(
            minimax(depth + 1, nodeIndex * 2, False, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, False, values, height)
        )
    else:
        return min(
            minimax(depth + 1, nodeIndex * 2, True, values, height),
            minimax(depth + 1, nodeIndex * 2 + 1, True, values, height)
        )

import math

values = list(map(int, input("Enter leaf node values: ").split()))
height = int(math.log2(len(values)))

result = minimax(0, 0, True, values, height)
print("Optimal value:", result)
