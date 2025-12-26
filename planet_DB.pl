planet(mercury, rocky).
planet(earth, habitable).
planet(jupiter, gas_giant).

planet_type(Planet, Type) :-
    planet(Planet, Type).
