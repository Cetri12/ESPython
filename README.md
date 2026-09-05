ESPython: Created 8/25/2026
Originally called Python-S, but renamed on 8/30/2026


Open Tutorial.txt, or read this:

ESPython is a python extension supporting custom syntax that is transpiled to python. ESPython currently supports $$ as comments, X++. and X-- in the base parser
invalid code. 

✅X++

❌++X
❌Y = X++

Use lib [library.extention] [runtime] to import a library.
example:
lib Library.py python

Libraries are not constrained to .py at all, you can code the library in anything you wish. If your OS can run it of course.

How to use:
Drag code.esp into the folder, then run Run.py
The code will be transpiled into ESPY_EXECUTE.py.
output.esp is the intermediary file, all libraries will parse this directly. 
After the libraries finish, output.esp will be copied to ESPY_EXECUTE.py

"Libraries" are simply additional parsers that you can create. Under the terms of the Apache 2.0 License, you may create
Libraries and distribute them as yours, as long as they weren't code taken from the parser. if they were, your library is
subject to the terms of the Apache 2.0 License. 

I would personally like it if you made libraries. Send a link to a repository with your library 
(I won't accept code files from strangers), and if i like it, i may list it under Main Libraries. 
If your license allows, i will put it on a seperate branch of the repository.

Official libraries are written by me, Main libraries are sponsored by me, and all other are Custom libraries.

Current Official ESPython Libraries:
ESPY_Parser.py (The core parser). 8/25/2026. 
ColorsLib.py
Script-SC.py

Current Main ESPython Libraries:
N/A





