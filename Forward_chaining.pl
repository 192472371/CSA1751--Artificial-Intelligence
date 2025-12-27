fact(fever).
fact(cough).

rule(flu) :-
    fact(fever),
    fact(cough).

forward :-
    rule(Disease),
    write('Derived disease: '), write(Disease).
