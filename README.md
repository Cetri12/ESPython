ESPython: Created 8/25/2026
Originally called Python-S, but renamed on 8/30/2026


Open ESPY_tutorial.txt, or read this:

ESPython is a python extentsion supporting syntax such as X++, and X--. ESPython is directly transpiled to python
Also currently supports $$ as comments. Since X++ is transpiled, it becomes X += 1. So, things such as ++X, and Y = X++ are
invalid code. 

✅X++

❌++X
❌Y = X++

Use lib [library.extention] [runtime] to import a library.
example:
lib Library.py python

Libraries are not constrained to .py at all, you can code the library in anything you wish. If your OS can run it of course.

How to use:
Drag code.pys into the folder, then run ESPython_Main.py
The code will be transpiled into ESPY_EXECUTE.py.
output.pys is the intermediary file, all libraries will parse this directly. 

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





