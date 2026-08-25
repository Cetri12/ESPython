#Parser. Made 8/25/2026
import shutil
import sys
import subprocess
from pathlib import Path
LINES = [] #The individual lines
POS = 0 #Position in the line
READ = True #Tells the parser if it should read the code. off for comments and strings
DEPTH = 0 #Depth in the parenthesis
LCHAR = [] #line split into it's chars


#Finds Libraries
def LIBFINDER():
    with open("output.pys", "r") as file:
        lines = file.readlines()
    for line in lines:
        LCHAR = list(line)
        POS = 0

        while POS < len(LCHAR):

            if "".join(LCHAR[POS:POS+4]) == "lib ":
                start = POS + 4
                end = start

                while end < len(LCHAR) and LCHAR[end] not in ";:":
                    end += 1

                library_name = "".join(LCHAR[start:end]).strip()

                if not Path(library_name).exists():
                    print()
                    print(f"\033[91mLIBFINDER ERROR: Library {library_name} does not exist\033[0m")
                    print("^" * (len(library_name) + 40))
                    print()
                else:
                    subprocess.run([library_name])

                del LCHAR[POS:end]

                continue




def PARSE():
    global READ
    global DEPTH
    global POS
    global LCHAR

    with open("code.pys", "r") as file:
        lines = file.readlines()

    for line in lines:
        LCHAR = list(line)
        POS = 0

        while POS < len(LCHAR):

            if READ != False:

                #Incremental
                if "".join(LCHAR[POS:POS+2]) == "++":
                    del LCHAR[POS:POS+2]
                    LCHAR.insert(POS, " += 1")

                    POS += len(" += 1")
                    continue

                #Decremental
                if "".join(LCHAR[POS:POS+2]) == "--":
                    del LCHAR[POS:POS+2]
                    LCHAR.insert(POS, " -= 1")

                    POS += len(" -= 1")
                    continue

                # $$ comments
                if "".join(LCHAR[POS:POS+2]) == "$$":
                    del LCHAR[POS:POS+2]
                    LCHAR.insert(POS, "#")
                    POS +=2
                    continue

            POS += 1

        with open("output.pys", "a") as file:
            file.write("".join(LCHAR))

    shutil.copyfile("output.pys", "PS_EXECUTE.py")

    #runs libfinder
    LIBFINDER()
    #wipes file
    with open("output.pys", "w") as file:
        pass

PARSE()
print("\033[34mFile Transpiled Sucessfully \033[0m")