#Python-S. 1.00.00 Made 8/25/2026
#Adds additional libraries to python.
import subprocess
from pathlib import Path
import os
import platform
import time



Version = "\033[34mVersion: 1.01.02\033[0m"

#Clears executable file and output.pys
with open("PS_EXECUTE.py", "w") as f:
    pass
with open("output.pys", "w") as f:
    pass

print("===Python-S===")
print(Version)
print("Please insert code.pys into folder. Dont worry if it's code.pys.txt. I got you")

#Renames .pys.txt to .pys
if Path("code.pys.txt").exists():
    os.rename("code.pys.txt", "code.pys")

if Path("output.pys.txt").exists():
    os.rename("output.pys.txt", "output.pys")

#Checks that the parser exists
file_path = Path("PS_Parser.py")
if not file_path.exists():
    print("Error: Parser not found")
else:
    print("Parser Docked Sucessfully")

    OSTYPE = platform.system()
    print("OS:",OSTYPE)
    time.sleep(1)
    subprocess.run(["python", "PS_Parser.py"])