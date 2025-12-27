fact(fever).
fact(cough).

rule(flu) :-
    fact(fever),
    fact(cough).

backward(Goal) :-
    rule(Goal),
    write('Goal achieved: '), write(Goal).
