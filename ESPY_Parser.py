#Parser. Made 8/25/2026
import shutil
import sys
import subprocess
from pathlib import Path
import os
import time

LINES = [] #The individual lines
POS = 0 #Position in the line
READ = True #Tells the parser if it should read the code. off for comments and strings
DEPTH = 0 #Depth in the parenthesis
LCHAR = [] #line split into it's chars
STRIN = False #If the parser is in a string
GRID = [] #The list of each edited line. is re-inserted back into the file at the end.
COMMENT = False #Tracker to check if the parer is in a comment
runtime = "python" #The runtime of final executable

Version = "Version 1.05.07"

Build_Data = [Version,"Type: Core File", "Gen2"]



#Finds Libraries
def LIBFINDER():
    global GRID
    libraries = [] #list of libraries
    new_lines = [] #the new lines
    with open("output.espython", "r") as file:
        lines = file.readlines()

    new_lines = []

    for line in lines:
        LCHAR = list(line)
        remove_line = False
        lang = ""
        FILE = ""
        LIBLINE = []

        if line.lstrip().startswith("lib "):
            LIBLINE = line.split()
            
            #Checks that the Statement defining txt is there before acting upon it
            file_path = Path("ESPY_STATEMENT.txt")
            if file_path.exists():
                with open ("ESPY_STATEMENT.txt","r") as file:
                    STATEMENTS = file.read().splitlines()
                    for i in STATEMENTS:
                        LIBLINE = [x.replace(i, "") for x in LIBLINE] #Replaces custom lib syntax for the parser


            if len(LIBLINE) >2:
                LIBLINE = [x.replace(";", "") for x in LIBLINE] #Replaces semicolons used in Python-S
                FILE = LIBLINE[1]
                lang = LIBLINE[2]
                remove_line = True
                libraries.append((lang, FILE))
                    
            else:
                print(f"Error, missing argument(s) for library {FILE} ")


        if not remove_line:
            new_lines.append("".join(LCHAR))

    #Saves the Parser's changes
    with open("output.espython", "w") as file:
        file.writelines(new_lines)

    #Runs the list of libraries
    for lang, FILE in libraries:
        subprocess.run([lang, FILE])





def PARSE():
    global READ
    global DEPTH
    global POS
    global LCHAR
    global STRIN
    global GRID
    global COMMENT

    with open("code.espython", "r") as file:
        lines = file.readlines()

    for line in lines:
        LCHAR = list(line)
        POS = 0
        READ = True
        STRIN = False
        COMMENT = False

        while POS < len(LCHAR):

            if not COMMENT:
                if LCHAR[POS] == '"':
                    READ = not READ #Flips reading state
                    STRIN = not STRIN #Flips string mode

            if not COMMENT:
                if LCHAR[POS] == '\\' and LCHAR[POS+1] == '"':
                    print("Escaped qoute")
                    READ = not READ
                    STRIN = not STRIN

            if READ:
                if LCHAR[POS] == "#":
                    READ = False
                    COMMENT = True



            #Incremental
            if READ and STRIN == False:
                if "".join(LCHAR[POS:POS+2]) == "++":
                    del LCHAR[POS:POS+2]
                    LCHAR.insert(POS, " += 1")

                    POS += len(" += 1")
                    continue
            
            #Decremental
            if READ and STRIN == False and not COMMENT:
                if "".join(LCHAR[POS:POS+2]) == "--":
                    del LCHAR[POS:POS+2]
                    LCHAR.insert(POS, " -= 1")
                    POS += len(" -= 1")
                    continue
            
            # $$ Comments
            if READ and STRIN == False and not COMMENT:
                if "".join(LCHAR[POS:POS+2]) == "$$":
                    del LCHAR[POS:POS+2]
                    LCHAR.insert(POS, "#")
                    POS +=2
                    READ = False #Turns off for the comment :D
                    COMMENT = True
                    continue

            POS += 1
        GRID.append("".join(LCHAR))

    with open("output.espython", "w") as file:
        for i in GRID:
            file.write(i)

if __name__ == "__main__":
    PARSE()

    # Runs LIBFINDER
    LIBFINDER()

    # copies output to PS_EXECUTE
    shutil.copyfile("output.espython", "ESPY_EXECUTE.py")

    # Clears output.pys
    with open("output.espython", "w") as file:
        pass

    print("\033[34mRunning...\033[0m")

    #Checks that the os is windows. If it is, terminal is cleared for execution
    time.sleep(1)
    if os.name == "nt":
        os.system("cls")

    #Deletes output.espython
    file_path = Path("output.espython")
    file_path.unlink()

    #Auto execution
    settings_path = Path(__file__).parent / "ESPY_Settings.txt"
    execute_path = Path(__file__).parent.parent / "ESPY_EXECUTE.py"
    with open(settings_path, "r") as file:
        SETT = file.readlines()
        if "1" in SETT[1]: #Checks the setting for auto execution
            subprocess.run([runtime,execute_path])