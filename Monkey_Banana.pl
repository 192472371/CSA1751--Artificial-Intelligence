move_to_box :-
    write('Monkey moves to the box'), nl.

push_box :-
    write('Monkey pushes the box under the banana'), nl.

climb_box :-
    write('Monkey climbs the box'), nl.

get_banana :-
    write('Monkey gets the banana'), nl.

solve :-
    move_to_box,
    push_box,
    climb_box,
    get_banana.
