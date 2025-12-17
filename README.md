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
