parent(john, mary).
parent(john, sam).
parent(mary, anna).

father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).

male(john).
female(mary).
female(anna).

grandparent(X, Y) :-
    parent(X, Z),
    parent(Z, Y).
