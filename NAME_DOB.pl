
person('Alice', date(12, may, 1995)).
person('Bob', date(3, january, 1990)).
person('Charlie', date(25, december, 1985)).
person('Diana', date(8, march, 2001)).
person('Ethan', date(15, july, 1998)).% --- Example query patterns ---

born_after(Name, Year) :-
    person(Name, date(_, _, Y)),
    Y > Year.

born_before(Name, Year) :-
    person(Name, date(_, _, Y)),
    Y < Year.
