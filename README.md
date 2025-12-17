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
