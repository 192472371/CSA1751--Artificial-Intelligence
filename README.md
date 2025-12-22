## BFS (Breadth First Search)

```text
BFS(graph, StartNode)
// Graph is represented as adjacency list

CREATE empty queue Q
CREATE empty set Visited

ADD StartNode to Visited
ENQUEUE StartNode into Q

WHILE Q is not empty DO
    CurrentNode = DEQUEUE Q
    VISIT CurrentNode

    FOR each Neighbor of CurrentNode in Graph DO
        IF Neighbor not in Visited THEN
            ADD Neighbor to Visited
            ENQUEUE Neighbor into Q
        END IF
    END FOR
END WHILE

END BFS
```

## DFS (Depth First Search)
```text
DFS(graph, StartNode)
// Graph is represented as adjacency list

CREATE empty set Visited

VISIT StartNode
ADD StartNode to Visited

FOR each Neighbor of StartNode in Graph DO
    IF Neighbor not in Visited THEN
        DFS(graph, Neighbor)
    END IF
END FOR

END DFS
```

## UCS (Uniform Cost Search)

```text
UCS(graph, StartNode, GoalNode)
// Graph is represented as adjacency list with costs

CREATE priority queue PQ
CREATE empty set Visited

INSERT (0, StartNode) into PQ

WHILE PQ is not empty DO
    (cost, CurrentNode) = REMOVE node with minimum cost from PQ

    IF CurrentNode is GoalNode THEN
        RETURN cost
    END IF

    IF CurrentNode not in Visited THEN
        ADD CurrentNode to Visited

        FOR each (Neighbor, EdgeCost) of CurrentNode DO
            INSERT (cost + EdgeCost, Neighbor) into PQ
        END FOR
    END IF
END WHILE

END UCS
```

## A* Search Algorithm 

```text
A*(graph, StartNode, GoalNode)
// Graph is represented as adjacency list with costs
// h(n) is the heuristic function

CREATE priority queue OPEN
CREATE empty set CLOSED

INSERT (f= h(StartNode), g=0, StartNode) into OPEN

WHILE OPEN is not empty DO
    (f, g, CurrentNode) = REMOVE node with lowest f value from OPEN

    IF CurrentNode is GoalNode THEN
        RETURN g   // total path cost
    END IF

    ADD CurrentNode to CLOSED

    FOR each (Neighbor, Cost) of CurrentNode DO
        IF Neighbor not in CLOSED THEN
            g_new = g + Cost
            f_new = g_new + h(Neighbor)
            INSERT (f_new, g_new, Neighbor) into OPEN
        END IF
    END FOR
END WHILE

END A*
```

## GBFS Algorithm

```text
GBFS(graph, StartNode, GoalNode)
// Graph is represented as adjacency list
// h(n) is the heuristic function

CREATE priority queue OPEN
CREATE empty set CLOSED

INSERT (h(StartNode), StartNode) into OPEN

WHILE OPEN is not empty DO
    (h, CurrentNode) = REMOVE node with lowest heuristic value from OPEN

    IF CurrentNode is GoalNode THEN
        RETURN SUCCESS
    END IF

    ADD CurrentNode to CLOSED

    FOR each (Neighbor, Cost) of CurrentNode DO
        IF Neighbor not in CLOSED THEN
            INSERT (h(Neighbor), Neighbor) into OPEN
        END IF
    END FOR
END WHILE

END GBFS
```

## Minimax Algorithm 

```text
MINIMAX(Node, Depth, IsMaximizing)

IF Depth == 0 OR Node is terminal THEN
    RETURN value of Node
END IF

IF IsMaximizingPlayer THEN
    BestValue = -∞
    FOR each Child of Node DO
        Value = MINIMAX(Child, Depth-1, FALSE)
        BestValue = MAX(BestValue, Value)
    END FOR
    RETURN BestValue
ELSE
    BestValue = +∞
    FOR each Child of Node DO
        Value = MINIMAX(Child, Depth-1, TRUE)
        BestValue = MIN(BestValue, Value)
    END FOR
    RETURN BestValue
END IF
```

##  α-β pruning Algorithm

```text
ALPHABETA(Node, Depth, α, β, IsMaximizing)

IF Depth == 0 OR Node is terminal THEN
    RETURN value of Node
END IF

IF IsMaximizingPlayer THEN
    BestValue = -∞
    FOR each Child of Node DO
        Value = ALPHABETA(Child, Depth-1, α, β, FALSE)
        BestValue = MAX(BestValue, Value)
        α = MAX(α, BestValue)

        IF β ≤ α THEN
            BREAK   // Beta cut-off
        END IF
    END FOR
    RETURN BestValue
ELSE
    BestValue = +∞
    FOR each Child of Node DO
        Value = ALPHABETA(Child, Depth-1, α, β, TRUE)
        BestValue = MIN(BestValue, Value)
        β = MIN(β, BestValue)

        IF β ≤ α THEN
            BREAK   // Alpha cut-off
        END IF
    END FOR
    RETURN BestValue
END IF
```

## Water Jug Problem 

```text
WATER-JUG(Jug1, Jug2, Target)

CREATE empty queue Q
CREATE empty set Visited

ADD (0, 0) to Q and Visited

WHILE Q is not empty DO
    (x, y) = DEQUEUE Q

    IF x == Target OR y == Target THEN
        PRINT solution path
        EXIT
    END IF

    GENERATE all possible next states:
        1. Fill Jug1
        2. Fill Jug2
        3. Empty Jug1
        4. Empty Jug2
        5. Pour Jug1 → Jug2
        6. Pour Jug2 → Jug1

    FOR each new state DO
        IF not in Visited THEN
            ADD to Visited and Q
        END IF
    END FOR
END WHILE
```

## Decision Tree

```text
ID3DecisionTree(Dataset, Attributes)

IF all examples in Dataset have same class THEN
    RETURN Leaf Node with that class
END IF

IF Attributes is empty THEN
    RETURN Leaf Node with majority class of Dataset
END IF

BestAttribute = attribute in Attributes with highest info_gain(Dataset, attribute)
CREATE Node Root with BestAttribute

FOR each value v in Values(BestAttribute, Dataset) DO
    Subset = examples in Dataset where BestAttribute = v

    IF Subset is empty THEN
        ADD Leaf Node to Root with majority class of Dataset
    ELSE
        Subtree = ID3DecisionTree(Subset, Attributes without BestAttribute)
        ADD Subtree to Root under branch v
    END IF
END FOR

RETURN Root
```
