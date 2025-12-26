teaches(ravi, math, m101).
teaches(sita, physics, p102).
teaches(anu, chemistry, c103).

student(john, math).
student(mary, physics).
student(raj, chemistry).

student_details(Student, Teacher, Subject, Code) :-
    student(Student, Subject),
    teaches(Teacher, Subject, Code).
