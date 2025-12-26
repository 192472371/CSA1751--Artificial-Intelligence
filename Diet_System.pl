diet(diabetes, 'Low sugar diet').
diet(bp, 'Low salt diet').
diet(obesity, 'Low fat diet').

suggest_diet(Disease, Diet) :-
    diet(Disease, Diet).
