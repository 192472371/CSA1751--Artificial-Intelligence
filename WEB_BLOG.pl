% ----- BLOG TITLE -----
title('Introduction to Artificial Intelligence').

% ----- HEADINGS -----
heading(h1, 'Artificial Intelligence').
heading(h2, 'Applications of AI').
heading(h3, 'Advantages of AI').

% ----- ANCHOR TAGS -----
anchor('Wikipedia', 'https://www.wikipedia.org').
anchor('OpenAI', 'https://www.openai.com').

% ----- IMAGE TAG -----
image('ai_image', 'ai.jpg').

% ----- RULES -----
show_title :-
    title(T),
    write('Title: '), write(T), nl.

show_heading :-
    heading(Level, Text),
    write(Level), write(': '), write(Text), nl,
    fail.
show_heading.

show_anchor :-
    anchor(Text, Link),
    write('Anchor Text: '), write(Text),
    write(' | Link: '), write(Link), nl,
    fail.
show_anchor.

show_image :-
    image(Name, File),
    write('Image Name: '), write(Name),
    write(' | File: '), write(File), nl,
    fail.
show_image.
