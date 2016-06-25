# Phichess
A(n unfinished) GUI for exploring chess openings as generated single file images.

Written in Python (3.4)

![Example Session](Phichess_example.JPG =492x361)

Completed thus far: 
* a main.py file for interacting with the program through a command line (view, reset, move, etc...).  
* displaying the chessboard objects as unicode 
* render images of chess positions using [Pillow](https://github.com/python-pillow/Pillow). 
* display a listbox for chess openings, associating each with their lines

TO DO: 
* finish interpreter for chess algebraic notations (e.g., "Nc6" = "knight to C6") 
* add listbox selection functionality for the openings 
* add text box or label which displays the current line in its notation form 
* add "undo" ability to the GUI manual entry and main.py file 
