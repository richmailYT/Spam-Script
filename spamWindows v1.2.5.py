import tkinter as tk, os, webbrowser, json, keyboard
from tkinter import filedialog
#pynput.keyboard import Key, Controller as KeyboardController
from pynput.mouse import Button, Controller as MouseController

#setting up the mainframe
root = tk.Tk(className = ' Spammer ') #sets the title of the script
root.geometry("500x450") #sets the screen size
root.resizable(False, False)
menu = tk.Menu(root)

#making variables
NotCorrect = ''
Version = ''
frame = ''
Credits = ''
Settings = ''
ErrorLabel = ''
TimeLable = ''

PreferencesStorage = {'FilePath': '', 'mode': 'light', 'loop': 'False'} #store file paths and preferences
#modes
Modes = {'light': [{'frame': 'white'}, {'root': 'white'}, {'text': 'black'}, {'background': 'white'}], 'dark': [{'frame': 'gray'}, {'root': 'black'}, {'text': 'white'}, {'background': 'black'}]}
MenuText = {'Settings': 'Settings', 'SettingsBack': 'Back', 'Credits': 'Credits', 'CreditsBack': 'Back'}

SettingsTextStr = MenuText['Settings']
SettingsTextTk = tk.StringVar()
SettingsTextTk.set(MenuText['Settings'])

CreditsTextStr = MenuText['Credits']
CreditsTextTk = tk.StringVar()
CreditsTextTk.set(MenuText['Credits'])

mode = tk.StringVar()
loop = tk.BooleanVar()
VersionNumber = tk.StringVar()

loop.set(PreferencesStorage['loop'])
mode.set(PreferencesStorage['mode'])
VersionNumber.set('1.2.5')

def ShowCredits():
    global Credits, CreditsTextStr, CreditsTextTk, Version
    
    for child in frame.winfo_children():
        child.destroy()
    
    for child in root.winfo_children():
        if child != frame and child != Credits and child != Version:
            child.destroy()
    
    #makes saving and loading menu
    root_menu = tk.Menu(root)
    root.config(menu=root_menu)
    options = tk.Menu(root_menu)

    root_menu.add_cascade(label='options', menu=options) 
    options.add_command(label='Save Preferences', command=lambda: SaveLoadPreferences('save'))
    options.add_command(label='Load Preferences', command=lambda: SaveLoadPreferences('load'))
    
    HelpServerLabel = tk.Button(frame, text="Props to https://discord.gg/c7bj76RhH3 for helping me", padx=10, pady=5, borderless=1, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][0]['frame'], command=lambda: webbrowser.open('https://discord.gg/c7bj76RhH3'))
    HelpServerLabel.place(x=0, y=50)

    if CreditsTextStr == MenuText['CreditsBack']:
        CreditsTextStr = MenuText['Credits']
        CreditsTextTk.set(CreditsTextStr) 
        Credits.configure(textvariable=SettingsTextTk)
        for child in frame.winfo_children():
            child.destroy()
        RedrawAll() #redraw the main interface
    else:
        CreditsTextStr = MenuText['CreditsBack']
        CreditsTextTk.set(CreditsTextStr)
        Credits.configure(textvariable=CreditsTextTk)

def ShowSettings():
    global frame, Settings, SettingsTextTk, SettingsTextStr

    for child in frame.winfo_children():
        child.destroy()
    
    for child in root.winfo_children():
        if child != frame and child != Settings and child != Version:
            child.destroy()

    #makes saving and loading menu
    root_menu = tk.Menu(root)
    root.config(menu=root_menu)
    options = tk.Menu(root_menu)

    root_menu.add_cascade(label='options', menu=options) 
    options.add_command(label='Save Preferences', command=lambda: SaveLoadPreferences('save'))
    options.add_command(label='Load Preferences', command=lambda: SaveLoadPreferences('load'))
    
    DarkMode = tk.Checkbutton(frame, text='Dark Mode', variable=mode, fg=Modes[PreferencesStorage['mode']][2]['text'], background=Modes[PreferencesStorage['mode']][3]['background'], onvalue='dark', offvalue='light', command=RedrawAll)
    LoopMode = tk.Checkbutton(frame, text='Loop', variable=loop, fg=Modes[PreferencesStorage['mode']][2]['text'], background=Modes[PreferencesStorage['mode']][3]['background'], onvalue=True, offvalue=False)
    Save_Preferences = tk.Button(frame, text='Save Preferences', padx=10, pady=5, fg=Modes[PreferencesStorage['mode']][2]['text'], bg=Modes[PreferencesStorage['mode']][3]['background'], borderless=1, command=lambda: SaveLoadPreferences('save'))
    Load_Preferences = tk.Button(frame, text='Load Preferences', padx=10, pady=5, fg=Modes[PreferencesStorage['mode']][2]['text'], bg=Modes[PreferencesStorage['mode']][3]['background'], borderless=1, command=lambda: SaveLoadPreferences('load'))

    Load_Preferences.place(x=200, y=10)
    LoopMode.place(x=50, y=125)
    Save_Preferences.place(x=30, y=10)
    DarkMode.place(x=50, y=100)

    PreferencesStorage['mode'] = mode.get()
    PreferencesStorage['loop'] = loop.get()


    if SettingsTextStr == MenuText['SettingsBack']:
        SettingsTextStr = MenuText['Settings']
        SettingsTextTk.set(SettingsTextStr) 
        Settings.configure(textvariable=SettingsTextTk)
        for child in frame.winfo_children():
            child.destroy()
        RedrawAll() #redraw the main interface
    else:
        SettingsTextStr = MenuText['SettingsBack']
        SettingsTextTk.set(SettingsTextStr)
        Settings.configure(textvariable=SettingsTextTk)

def SaveLoadPreferences(LoadorSave):
    global NotCorrect, PreferencesStorage
    
    try:
        NotCorrect.destroy()
    except Exception:
        pass

    if LoadorSave == 'save':
        #save_path = tk.filedialog.askdirectory(title='Please select a folder to save the preferences')
        #save_path = str(save_path + '/')
        #complete_path = os.path.join(save_path + 'preferences.json')
        os.system('mkdir /Library/Application\ Support/Spammer')
        with open('/Library/Application\ Support/Spammer/preferences.json', "w") as f:
            json.dump(PreferencesStorage, f)
    else:
        #load_path = tk.filedialog.askopenfilename(initialdir='/', title='Select the preferences file', filetypes=(('text files', '*.json'),))
        NotCorrect = tk.Label(frame, text='Please select the correct file', padx=10, pady=5, bg=Modes[mode.get()][3]['background'], fg=Modes[mode.get()][2]['text'])
        try:
            with open('/Library/preferences.json') as f:
                PreferencesStorage = json.load(f)
        except Exception:
            NotCorrect.pack()
            return
        if type(PreferencesStorage) == dict:
            mode.set(PreferencesStorage['mode'])
            loop.set(PreferencesStorage['loop'])
            RedrawAll()
        else:
            NotCorrect.pack()

def RedrawAll():
    global SettingsTextTk, SettingsTextStr, frame, Credits, Settings, FileLabel, PreferencesStorage
    
    #destorys everything
    for child in frame.winfo_children():
        child.destroy()
    
    for child in root.winfo_children():
            child.destroy()

    #remakes the base and sets it to a color
    root.configure(bg=Modes[mode.get()][1]['root'])

    frame = tk.Frame(root, bg=Modes[mode.get()][0]['frame'])
    frame.place(relheight=0.8, relwidth=0.8, relx=0.05, rely=0.05, x=25, y=100)

    SettingsTextStr = MenuText['Settings']
    SettingsTextTk = tk.StringVar()
    SettingsTextTk.set(SettingsTextStr)

    #makes all the buttons
    SelectFile = tk.Button(root, text='Select File', padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][3]['background'], borderless=1, command=AddFile)
    StartSpam = tk.Button(root, text='Start Spam', padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][3]['background'], borderless=1, command=StartTheSpam)
    Settings = tk.Button(root, textvariable=SettingsTextTk, padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][3]['background'], borderless=1, command=ShowSettings)
    Credits = tk.Button(root, text='Credits', padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][3]['background'], borderless=1, command=ShowCredits)

    Settings.place(x=360, y=20)
    Credits.place(x=60, y=20)
    SelectFile.place(x=200, y=0)
    StartSpam.place(x=200, y=30)

    #makes all the labels
    Version = tk.Label(frame, textvariable=VersionNumber, padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][0]['frame'])      
    StopLabel = tk.Label(frame, text = "Move Your Mouse To The Top Left Corner To Stop The Spam", padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][0]['frame'])
    
    StopLabel.place(x=0,y=30)
    Version.place(x=350, y=300)   

    if PreferencesStorage['FilePath'] != '':
        filenameTk = tk.StringVar()
        filenameTk.set(PreferencesStorage['FilePath'])
        FileLabel = tk.Label(frame, textvariable=filenameTk, padx=10, pady=5, bg=Modes[mode.get()][3]['background'], fg=Modes[mode.get()][2]['text'])
        FileLabel.pack()

    #makes saving and loading menu
    root_menu = tk.Menu(root)
    root.config(menu=root_menu)
    options = tk.Menu(root_menu)

    root_menu.add_cascade(label='options', menu=options) 
    options.add_command(label='Save Preferences', command=lambda: SaveLoadPreferences('save'))
    options.add_command(label='Load Preferences', command=lambda: SaveLoadPreferences('load'))

def AddFile():	
    global FileLabel, PreferencesStorage

    Tempfilename = tk.filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(("text file", "*.txt"),))
    TempfilenameTk = tk.StringVar()
    TempfilenameTk.set(Tempfilename)

    try:
        FileLabel.destroy()
    except Exception:
        pass

    FileLabel = tk.Label(frame, textvariable=TempfilenameTk, padx=10, pady=5, bg=Modes[mode.get()][3]['background'], fg=Modes[mode.get()][2]['text'])
    FileLabel.pack()

    PreferencesStorage['FilePath'] = Tempfilename

def StartTheSpam():
    global TimeLable, ErrorLabel
    #destoryes error labels and the countdown timer
    try:
        for child in root.winfo_children():
            if child == TimeLable or child == ErrorLabel:
                child.destroy()
    except NameError:
        pass
    #needed for fail-safe 1
    mouse = MouseController()

    countdown_value = 5
    counter = tk.StringVar()
    counter.set(countdown_value)
    TimeLable = tk.Label(frame, textvariable=counter, padx=10, pady=5, bg=Modes[mode.get()][3]['background'], fg=Modes[mode.get()][2]['text'])
    TimeLable.pack()

    #coundown
    for countdown in range(1, countdown_value):
        TimeLable.after(1000 * countdown, counter.set, countdown_value - countdown)
    x = 100
    y = 100
    try:
        with open(PreferencesStorage['FilePath'], 'r') as SpamText: 
            while PreferencesStorage['loop']:
                for word in SpamText:
                    #fail safe 1
                    if x < 21 and y < 21:
                        break
                    TempX, TempY = mouse.position
                    x = int(TempX)
                    y = int(TempY)
                    #fail-safe 2
                    if keyboard.is_pressed('ctrl+d'):
                        break
                    keyboard.write(word)
                    print(word)
                #return to begining when at end, thats why its outside of the loop
                SpamText.seek(0)
            for word in SpamText:
                keyboard.write(word)
    except FileNotFoundError:
        NoFile = tk.Label(frame, text = 'Please Select A File', padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][3]['background'])
        NoFile.pack()

if __name__ == '__main__':
    frame = tk.Frame(root, bg=Modes[mode.get()][0]['frame'])
    frame.place(relheight=0.8, relwidth=0.8, relx=0.05, rely=0.05, x=25, y=100)
    RedrawAll()

    root.mainloop()