def alphabeta(depth, nodeIndex, isMax, values, height, alpha, beta):

    # Base case: leaf node
    if depth == height:
        return values[nodeIndex]

    if isMax:
        best = float('-inf')

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                             False, values, height, alpha, beta)
            best = max(best, val)
            alpha = max(alpha, best)

            if beta <= alpha:
                break   # Beta pruning

        return best

    else:
        best = float('inf')

        for i in range(2):
            val = alphabeta(depth + 1, nodeIndex * 2 + i,
                             True, values, height, alpha, beta)
            best = min(best, val)
            beta = min(beta, best)

            if beta <= alpha:
                break   # Alpha pruning

        return best

import math

values = list(map(int, input("Enter leaf node values: ").split()))
height = int(math.log2(len(values)))

result = alphabeta(0, 0, True, values, height,
                   float('-inf'), float('inf'))

print("Optimal value with Alpha-Beta Pruning:", result)
