#Python-S. 1.00.00 Made 8/25/2026
#Adds additional libraries to python.
import subprocess
from pathlib import Path
import os
import platform
import time
import sys

settings_path = Path(__file__).parent / "Core" / "ESPY_Settings.txt"

#File build data
Version = "Version: 1.04.03"
Build_Data = [Version, "Type: Utility File", "Gen2"]

#Espython build data
Espy_Version = "Version: 1.07.05"
Espy_Build_Data = [Espy_Version,"Gen2"]


if __name__ == "__main__":

    #Clears executable file and output.pys
    with open("ESPY_EXECUTE.py", "w") as f:
        pass
    
    output_path = Path("Core") / "output.espython"
    with open(output_path, "w") as f:
        pass

    with open(settings_path, "r") as file:
        SETT = file.readline()

    if SETT[0] == "1": #Checks the setting for terminal feedback
        print("===Python-S===")
        print(Version)
        print("Please insert code.espython into folder. Dont worry if it's code.espython.txt. I got you")
        OSTYPE = platform.system()
        print("OS:",OSTYPE)

    #Renames .esp.txt to .esp
    if Path("code.esp.txt").exists():
        os.rename("code.espython.txt", "code.espython")

    if Path("output.esp.txt").exists():
        os.rename("output.espython.txt", "output.espython")

    #Checks that the parser exists
    file_path = Path(__file__).parent / "Core" / "ESPY_Parser.py"
    if not file_path.exists():
        print()
        print("\033[31mError: Parser not found\033[0m")
        print()
    else:
        print()
        print("\033[34mParser Docked Sucessfully\033[0m")
        print()

    subprocess.run([sys.executable, file_path])