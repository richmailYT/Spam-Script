import webbrowser, keyboard, sys
#pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

#making variables
Version = '1.3.0'

#take command line args

def StartSpam(FilePath):
    #needed for fail-safe 1
    mouse = MouseController()

    try:
        with open(FilePath, "r") as SpamText:
            #check if loop is ture, if so keep 
            #repeating until the fail-safe is triggered
            x, y = 100, 100
            for word in SpamText:
                    #fail safe 1
                    if x < 21 and y < 21:
                        return
                    TempX, TempY = mouse.position
                    x = int(TempX)
                    y = int(TempY)
                    #fail-safe 2
                    if keyboard.is_pressed('ctrl+c'):
                        return
                    keyboard.write(word)
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

#loop code, unused
""" 
if loop:
    while loop:
        for word in SpamText:
            #fail safe 1
            if x < 21 and y < 21:
                return
            TempX, TempY = mouse.position
            x = int(TempX)
            y = int(TempY)
            #fail-safe 2
            if keyboard.is_pressed('ctrl+c'):
                return
            keyboard.write(word)
            print(word)
        #return to begining when at end
        #thats why its outside of the loop
        SpamText.seek(0)
else: """