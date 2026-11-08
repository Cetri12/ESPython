#ESPython Build info checker. 1.00.00 Made 9/5/2026

Version = "Version: 1.01.01"

Build_Data = [Version, "Type: Utility File", "Gen2"]

from pathlib import Path
import sys

def BUILD_INFO():
    from Run import Espy_Build_Data
    print()
    print("\033[35mESPython Build Info Checker")
    print(Version)
    print("\033[0m")
    print("\033[32m===ESPython Build Data===")
    print(Espy_Build_Data[0])
    print(Espy_Build_Data[1],"\033[0m")
    print()
    file = input("Name of file(Without file extention): ")
    folder = input("In Core Folder(y/n)?: ")

    #If in Main folder
    if folder.lower() == "n":
        file = __import__(file)
        Build_Data = file.Build_Data
        print()
        print("\033[32m===Data===")
        print(Build_Data[0])
        print(Build_Data[1])
        print("\033[0m")



    #If in core folder
    else:
        sys.path.append("Core")
        file = __import__(file)
        Build_Data = file.Build_Data
        print()
        print("\033[32m===Data===")
        print(Build_Data[0])
        print(Build_Data[1])
        print("\033[0m")

if __name__ == "__main__":
    BUILD_INFO()