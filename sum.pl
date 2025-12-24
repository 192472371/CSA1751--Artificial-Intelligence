
sum_to_n(0, 0).
sum_to_n(N, Sum) :-
    N > 0,
    N1 is N - 1,
    sum_to_n(N1, PartialSum),
    Sum is PartialSum + N.
