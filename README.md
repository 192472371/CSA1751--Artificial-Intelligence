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

## CRYPT Arithematic Problem 

```text
CRYPTOARITHMETIC(Puzzle)

LET Letters = all unique letters in Puzzle
LET N = number of unique letters

FUNCTION Solve(Puzzle, Letters, Mapping)

    IF all Letters are assigned digits THEN
        SUBSTITUTE letters in Puzzle with Mapping
        IF arithmetic equation is valid THEN
            PRINT Mapping
        END IF
        RETURN
    END IF

    LET CurrentLetter = next unassigned letter in Letters

    FOR Digit in 0 to 9 DO
        IF Digit not already used in Mapping THEN
            ASSIGN CurrentLetter = Digit
            Solve(Puzzle, Letters, Mapping)
            UNASSIGN CurrentLetter
        END IF
    END FOR

END FUNCTION
```

## FeedForward Neural Network

```text
FEEDFORWARD_NEURAL_NETWORK

READ input values x1, x2

READ weights w13, w23
READ weights w14, w24
READ weights w35, w45

DEFINE sigmoid(x) = 1 / (1 + e^(-x))

COMPUTE a3 = (w13 × x1) + (w23 × x2)
COMPUTE y3 = sigmoid(a3)

COMPUTE a4 = (w14 × x1) + (w24 × x2)
COMPUTE y4 = sigmoid(a4)

COMPUTE a5 = (w35 × y3) + (w45 × y4)
COMPUTE y5 = sigmoid(a5)

PRINT final output y5

END
```

## Backward Neural network

```text
FEEDFORWARD_BACKPROP_NEURAL_NETWORK

READ input values x1, x2
READ target output t

READ weights w13, w23
READ weights w14, w24
READ weights w35, w45

DEFINE sigmoid(x) = 1 / (1 + e^(-x))
DEFINE sigmoid_derivative(y) = y × (1 − y)

# -------- FEEDFORWARD --------
COMPUTE a3 = (w13 × x1) + (w23 × x2)
COMPUTE y3 = sigmoid(a3)

COMPUTE a4 = (w14 × x1) + (w24 × x2)
COMPUTE y4 = sigmoid(a4)

COMPUTE a5 = (w35 × y3) + (w45 × y4)
COMPUTE y5 = sigmoid(a5)

COMPUTE Error = t − y5

# -------- BACKPROPAGATION --------
COMPUTE delta5 = Error × sigmoid_derivative(y5)

COMPUTE delta3 = delta5 × w35 × sigmoid_derivative(y3)
COMPUTE delta4 = delta5 × w45 × sigmoid_derivative(y4)

# Learning rate
READ learning_rate η

# Update weights
w35 = w35 + η × delta5 × y3
w45 = w45 + η × delta5 × y4

w13 = w13 + η × delta3 × x1
w23 = w23 + η × delta3 × x2

w14 = w14 + η × delta4 × x1
w24 = w24 + η × delta4 × x2

PRINT updated weights
PRINT final output y5
PRINT error
END
```


## 8 - Puzzle Algorithm

```text
8PuzzleBFS(StartState, GoalState)

CREATE empty queue Q
CREATE empty set Visited

ENQUEUE (StartState, []) into Q  // state + moves taken
ADD StartState to Visited

WHILE Q is not empty DO
    (CurrentState, Moves) = DEQUEUE Q
    
    IF CurrentState == GoalState THEN
        RETURN Moves  // solution found
    END IF

    FOR each valid move (Up, Down, Left, Right) DO
        NextState = result of moving empty tile
        IF NextState not in Visited THEN
            ADD NextState to Visited
            ENQUEUE (NextState, Moves + [Move])
        END IF
    END FOR
END WHILE

RETURN "No solution found"
```

## 8-Queen Algorithm 

```text
PlaceQueen(row):
    IF row == 8 THEN
        PRINT current board as a solution
        RETURN

    FOR col in 0 to 7 DO
        IF placing a queen at (row, col) is safe THEN
            place queen at (row, col)
            PlaceQueen(row + 1)
            remove queen at (row, col)  // backtrack
```

## Prolog Program for STUDENT–TEACHER–SUBJECT–CODE

```text
STUDENT_TEACHER_SUBJECT_CODE

STORE facts linking student, teacher, subject, subject_code
ACCEPT query for student or subject
MATCH facts using unification
DISPLAY related teacher and subject_code

END
```


## Prolog Program for PLANETS Database

```text
PLANETS_DATABASE

STORE planet facts with properties
ACCEPT query for planet or property
MATCH facts using rules
DISPLAY required planet information

END
```


## Prolog Program for Towers of Hanoi

```text
TOWERS_OF_HANOI

IF number_of_disks = 1
    MOVE disk from source to destination
ELSE
    MOVE n-1 disks from source to auxiliary
    MOVE nth disk from source to destination
    MOVE n-1 disks from auxiliary to destination
END IF

END
```


## Prolog Program to Check Whether a Bird Can Fly

```text
BIRD_CAN_FLY

STORE bird facts
STORE flying and non-flying rules
ACCEPT bird name as query
CHECK rules
DISPLAY whether bird can fly or not

END
```

## Prolog Program for Family Tree

```text
FAMILY_TREE

STORE parent relationships
DEFINE rules for father, mother, sibling, grandparent
ACCEPT relationship query
INFER relationship using rules
DISPLAY result

END
```


## Prolog Program to Suggest Dieting System Based on Disease

```text
DIET_SUGGESTION_SYSTEM

STORE disease and diet facts
ACCEPT disease name as input
MATCH disease with diet rule
DISPLAY suggested diet plan

END
```

## Prolog Program for Monkey–Banana Problem

```text
MONKEY_BANANA_PROBLEM

DEFINE initial state of monkey, box, banana
DEFINE possible actions (move, climb, grab)
APPLY actions using rules
CHECK goal state (monkey has banana)
DISPLAY solution path

END
```

## Prolog Program for Fruit and Color Using Backtracking

```text
FRUIT_COLOR_BACKTRACKING

STORE fruit-color facts
ACCEPT fruit or color query
USE backtracking to find all matches
DISPLAY possible results

END
```

## Prolog Program to Implement Best First Search

```text
BEST_FIRST_SEARCH

INITIALIZE open list with start node
WHILE open list not empty
    SELECT node with best heuristic value
    IF goal reached
        STOP
    ELSE
        EXPAND node and add successors
END WHILE

END
```

## Prolog Program for Medical Diagnosis

```text
MEDICAL_DIAGNOSIS_SYSTEM

STORE symptoms and disease facts
ACCEPT patient symptoms
MATCH symptoms with disease rules
DISPLAY possible disease

END
```

## Prolog Program for Forward Chaining

```text
FORWARD_CHAINING

STORE initial facts
STORE inference rules
APPLY rules to derive new facts
REPEAT until no new facts
DISPLAY inferred results

END
```

## Prolog Program for Backward Chaining

```text
BACKWARD_CHAINING

ACCEPT goal as query
SEARCH rules whose conclusion matches goal
RECURSIVELY prove sub-goals
DISPLAY success or failure

END
```

## Prolog Program for Pattern Matching

```text
PATTERN_MATCHING

STORE patterns as facts
ACCEPT input pattern
MATCH input with stored patterns
DISPLAY matching result

END
```

## Prolog Program to Find Number of Vowels

```text
COUNT_VOWELS

ACCEPT input string
CHECK each character
IF character is vowel
    INCREMENT count
DISPLAY total vowel count

END
```

## Prolog program WEB BLOG USING WORDPRESS

```text
WEB_BLOG_USING_WORDPRESS

STORE title of the blog
STORE headings used in the blog
STORE anchor links
STORE images used in the blog

ACCEPT query for blog components
DISPLAY corresponding details

END
```
