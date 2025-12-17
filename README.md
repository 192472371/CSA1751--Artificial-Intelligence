**Breadth First Search **
Represent the graph using an adjacency list

Create an empty queue Q

Create an empty set/list Visited

Add StartNode to Visited

Enqueue StartNode into Q

While Q is not empty do

Dequeue a node from Q → CurrentNode

Visit CurrentNode

For each neighbor of CurrentNode in Graph do

If neighbor is not in Visited then

Add neighbor to Visited

Enqueue neighbor into Q

End If

End For

End While

End BFS
