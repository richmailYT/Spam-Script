import pyautogui, sys, time

#making variables
Version = '1.3.1'

def StartSpam(FilePath):
    try:
        with open(FilePath, "r") as SpamText:
            x, y = 100, 100
            for word in SpamText:
                    #fail safe
                    if x < 21 and y < 21:
                        return
                    TempX, TempY = pyautogui.position()
                    x = int(TempX)
                    y = int(TempY)
                    pyautogui.write(word)
                    print(word)
    except FileNotFoundError:
        print("file not found. This may be due to an invaild path (file does not exist)")
    except IsADirectoryError:
        print("Python exspected a file, not a directory (read: folder)")

if __name__ == '__main__':
    print(Version)
    print("Credits to https://discord.gg/myvkRrvpGR for helping me with this project")
    try:
        StartSpam(sys.argv[1])
    except IndexError:
        print("please provide a file")
        sys.exit()

    i = 5
    while i != 0:
        print(f"Starting in {i}")
        i = i - 1