bird(sparrow).
bird(penguin).

can_fly(sparrow).
cannot_fly(penguin).

fly(Bird) :-
    can_fly(Bird),
    write(Bird), write(' can fly').

fly(Bird) :-
    cannot_fly(Bird),
    write(Bird), write(' cannot fly').
