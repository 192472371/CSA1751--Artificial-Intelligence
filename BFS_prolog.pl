edge(a, b, 1).
edge(a, c, 2).
edge(b, d, 3).
edge(c, d, 1).

bestfs(Start, Goal) :-
    path(Start, Goal, [Start]).

path(Goal, Goal, _) :-
    write('Goal reached').

path(Node, Goal, Visited) :-
    edge(Node, Next, _),
    \+ member(Next, Visited),
    path(Next, Goal, [Next|Visited]).
