#ESPython Library folder unpackager 1.00.00 Made 9/5/2026-9/6/2026

from pathlib import Path

Version = "Version: 1.00.00"
Build_Data = [Version, "Type: Utility File", "Gen2"]

if __name__ == "__main__":
    print("===Unpackager===")
    folder = input("Name of folder: ")

    folder = Path(folder)
    print()
    print("Files:\033[35m")
    for file in folder.iterdir():
        if file.is_file():
            file_name = file.name
            print(file_name)
            filen = file.stem

        if file.suffix != ".txt":
            sys.path.append(folder)
            selfile = __import__(file)
            Build_Data = selfile.Build_Data
            if "Utility" in Build_Data[1]:
                file.rename(Path("Core") / file.name)

        if file.suffix == ".txt":
            if "tutorial" in str(file).lower():
                file.rename(Path("Core") / "Tutorials" / file.name)
            
            else:
                file.rename(Path("Core") / file.name)

        efolder = Path(folder)
        efolder.rmdir()

    print("\033[0m")

