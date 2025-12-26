symptom(fever).
symptom(cough).

disease(flu) :-
    symptom(fever),
    symptom(cough).

diagnose(Disease) :-
    disease(Disease).
