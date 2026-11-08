#Settings file. Made 8/27/2026

from pathlib import Path

Version = "Version: 1.01.00"
Build_Data = [Version, "Type: Utility File", "Gen2"]

if __name__ == "__main__":

    print("===Settings===")
    print(Version)
    print("Type in the setting number to toggle the setting")
    print("Type reset to reset settings")

    SL = [] #List of settings in human readable form
    LPOS = 1 #Position of line
    Default = """0
    0
    """

    settings_path = Path(__file__).parent / "Core" / "ESPY_Settings.txt"

#Decodes settings
def SREADR():
    global settings_path
    global SL
    global LPOS
    LPOS = 1 #Resets LPOS

    
    with open(settings_path, "r") as file:
        for RS in file:
            RS = RS.strip()


            #reads text output setting

            #Line 1
            if RS:
                if RS == "0" and LPOS == 1:
                    SL.append("1. Terminal Feedback: Off")

                if RS == "1" and LPOS == 1:
                    SL.append("1. Terminal Feedback: On")
            
            #Line 2
            if RS:
                if RS == "0" and LPOS == 2:
                    SL.append("2. Auto Execution: Off")

                if RS == "1" and LPOS == 2:
                    SL.append("2. Auto Execution: On")

            LPOS += 1 #Progresses line tracker
    print("Settings: ")

    for i in SL:
        print(i) #Prints the readable settings

def SETINSET():
    global settings_path
    global Default
    if settings_path.exists():
        with open(settings_path, "r") as file:
            SETTINZ = file.readlines()
    
    else:
        print("Settings file does not exist. Creating...")
        with open(settings_path, "r") as file:
            pass


    a = input("Action: ")

    #Settings reset
    if a.lower() == "reset":
        with open(settings_path, "w") as file:
            #writing the default settings in
            file.writelines(Default)


    if a == "1":
        if SETTINZ[0].strip() == "0":
            SETTINZ[0] = "1\n"
            with open(settings_path, "w") as file:
                #writing the settings in
                file.writelines(SETTINZ)
                return

        if SETTINZ[0].strip() =="1":
            SETTINZ[0] = "0\n"
            with open(settings_path, "w") as file:
                #writing the settings in
                file.writelines(SETTINZ)
                return

    if a == "2":
        if SETTINZ[1].strip() =="0":
            SETTINZ[1] = "1\n"
            with open(settings_path, "w") as file:
                #writing the settings in
                file.writelines(SETTINZ)
                return

        if SETTINZ[1].strip() =="1":
            SETTINZ[1] = "0\n"
            with open(settings_path, "w") as file:
                #writing the settings in
                file.writelines(SETTINZ)
                return

if __name__ == "__main__":
    SREADR()
    SETINSET()

