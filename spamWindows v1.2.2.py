import tkinter as tk, pyautogui as pg, time, os, webbrowser, json
from tkinter import filedialog, Text

#setting up the mainframe
root = tk.Tk(className = ' Spammer ') #sets the title of the script
root.geometry("500x450") #sets the screen size
root.resizable(False, False)
menu = tk.Menu(root)

#making variables
NotDict = ''
Version = ''
frame = ''
Credits = ''
Tempfilename = ''
Settings = ''
ErrorLabel = ''
TimeLabel = ''
VersionNumber = '1.2.2'
ExsitingFileLabel = False
FileLabel = ''
loop = tk.BooleanVar()
PreferencesStorage = {'FilePath': '', 'mode': 'dark', 'loop': 'False'} #store file paths and preferences

SettingsText = {'Settings': 'Settings', 'SettingsBack': 'Back'}
SettingsTextStr = SettingsText['Settings']
SettingsTextTk = tk.StringVar()
SettingsTextTk.set(SettingsTextStr)

CreditsText = {'Credits': 'Credits', 'CreditsBack': 'Back'}
CreditsTextStr = CreditsText['Credits']
CreditsTextTk = tk.StringVar()
CreditsTextTk.set(CreditsTextStr)

mode = tk.StringVar()
mode.set('light')
Modes = {'light': [{'frame': 'white'}, {'root': 'white'}, {'text': 'black'}, {'background': 'white'}], 'dark': [{'frame': 'gray'}, {'root': 'black'}, {'text': 'white'}, {'background': 'black'}]}

def ShowCredits(CreditsTextCredits, CreditsTextBack):
    global frame, Credits, CreditsTextStr, CreditsTextTk, Version, mode, Modes
    
    for child in frame.winfo_children():
        child.destroy()
    
    for child in root.winfo_children():
        if child != frame and child != Credits and child != Version:
            child.destroy()
    
    HelpServerLabel1 = tk.Label(frame, text="Props to", padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][0]['frame'])
    HelpServer = tk.Button(frame, text = 'https://discord.gg/c7bj76RhH3', padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][0]['frame'], command = lambda: webbrowser.open('https://discord.gg/c7bj76RhH3'))
    HelpServerLabel2 = tk.Label(frame, text="for helping me with this project.", padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][0]['frame'])

    HelpServerLabel1.pack()
    HelpServer.pack()
    HelpServerLabel2.pack()

    if CreditsTextStr == CreditsTextBack:
        CreditsTextStr = CreditsTextCredits
        CreditsTextTk.set(CreditsTextStr) 
        Credits.configure(textvariable=CreditsTextTk)
        for child in frame.winfo_children(): #delet all of the buttons
            child.destroy()
        MakeChildren() #redraw the main interface
    else:
        CreditsTextStr = CreditsTextBack
        CreditsTextTk.set(CreditsTextStr)
        Credits.configure(textvariable=CreditsTextTk)

def ShowSettings(SettingsTextSettings, SettingsTextBack):
    global frame, Settings, SettingsText, SettingsTextTk, SettingsTextStr, mode, Modes

    for child in frame.winfo_children():
        child.destroy()
    
    for child in root.winfo_children():
        if child != frame and child != Settings and child != Version:
            child.destroy()
    
    DarkMode = tk.Checkbutton(frame, text='Dark Mode', variable=mode, background=Modes[mode.get()][3]['background'], onvalue='dark', offvalue='light', command=RedrawAll)
    DarkMode.place(x=50, y=100)

    LoopMode = tk.Checkbutton(frame, text='Loop', variable=loop, background=Modes[mode.get()][3]['background'], onvalue=True, offvalue=False)
    LoopMode.place(x=50, y=125)

    PreferencesStorage['mode'] = mode.get()
    PreferencesStorage['loop'] = loop.get()

    if SettingsTextStr == SettingsTextBack:
        SettingsTextStr = SettingsTextSettings
        SettingsTextTk.set(SettingsTextStr) 
        Settings.configure(textvariable=SettingsTextTk)
        for child in frame.winfo_children():
            child.destroy()
        MakeChildren() #redraw the main interface
    else:
        SettingsTextStr = SettingsTextBack
        SettingsTextTk.set(SettingsTextStr)
        Settings.configure(textvariable=SettingsTextTk)

def SaveLoadPreferences(LoadorSave):
    global FileLabel, PreferencesStorage, NotDict
    
    try:
        NotDict.destroy()
    except Exception:
        pass

    if LoadorSave == 'save':
        temp = {'FilePath': Tempfilename}
        save_path = tk.filedialog.askdirectory(title='Please select a folder to save the preferences')
        save_path = str(save_path + '/')
        complete_path = os.path.join(save_path + 'preferences.json')
        with open(complete_path, "w") as f:
            json.dump(temp, f)
    else:
        load_path = tk.filedialog.askopenfilename(initialdir='/', title='Select the preferences file', filetypes=(('text files', '*.json'),))
        try:
            with open(load_path) as f:
                PreferencesStorage = json.load(f)
        except Exception:
            NotJson = tk.Label(frame, text='Please select the correct file', padx=10, pady=5, bg=Modes[mode.get()][3]['background'], fg=Modes[mode.get()][2]['text'])
            NotJson.pack()
        if type(PreferencesStorage) == dict:
            RedrawAll()
        else:
            NotDict = tk.Label(frame, text='Please select the correct file', padx=10, pady=5, bg=Modes[mode.get()][3]['background'], fg=Modes[mode.get()][2]['text'])
            NotDict.pack()

def RedrawAll():
    global frame, SettingsTextTk, SettingsTextStr#, PreferencesStorage
    for child in frame.winfo_children():
        child.destroy()
    
    for child in root.winfo_children():
            child.destroy()

    root.configure(bg=Modes[mode.get()][1]['root'])

    frame = tk.Frame(root, bg=Modes[mode.get()][0]['frame'])
    frame.place(relheight=0.8, relwidth=0.8, relx=0.05, rely=0.05, x=25, y=100)

    SettingsTextStr = SettingsText['Settings']
    SettingsTextTk = tk.StringVar()
    SettingsTextTk.set(SettingsTextStr)
    MakeChildren()

def AddFile():	
    global ExsitingFileLabel, FileLabel, PreferencesStorage
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
    global TimeLabel, ErrorLabel
    #destoryes error labels and the countdown timer
    try:
        for child in root.winfo_children():
            if child == TimeLabel or child == ErrorLabel:
                child.destroy()
    except NameError:
        pass
    
    countdown_value = 6
    counter = tk.StringVar()
    counter.set(countdown_value)
    TimeLabel = tk.Label(frame, textvariable=counter, padx=10, pady=5, bg=Modes[mode.get()][3]['background'], fg=Modes[mode.get()][2]['text'])
    TimeLabel.pack()
    
    #coundown
    for _ in range(1, countdown_value):
        TempX, TempY = pg.position()
        x = TempX
        y = TempY
        x = int(x)
        y = int(y)

        TimeLabel = tk.Label(frame, textvariable=counter, padx=10, pady=5, bg=Modes[mode.get()][3]['background'], fg=Modes[mode.get()][2]['text'])
        TimeLabel.pack()

        #.1 intervals
        for _ in range(1, 10):
            if not (x < 21 and y < 21):
                time.sleep(0.1)
            else:
                return
        
        countdown_value-=1
        counter.set(countdown_value)
        TimeLabel.destroy()
    
    try:
        TimeLabel.destroy()
        with open(PreferencesStorage['FilePath'], 'r') as SpamText:
            while PreferencesStorage['loop']:
                for word in SpamText:
                    pg.typewrite(word)
                if SpamText.read() == '':
                    SpamText.seek(0) 
            if not PreferencesStorage['loop']:
                for word in SpamText:
                    pg.typewrite(word)
    except TypeError:
        TimeLabel.destroy()
        NoFile = tk.Label(frame, text = 'Please Select A File', padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][3]['background'])
        NoFile.pack()

def MakeChildren():
    global Credits, SettingsText, Settings, FileLabel, PreferencesStorage# mode, Modes, SettingsTextTk

    #makes all the buttons
    SelectFile = tk.Button(root, text='Select File', padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][3]['background'], command=AddFile)
    StartSpam = tk.Button(root, text='Start Spam', padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][3]['background'], command=StartTheSpam)
    Settings = tk.Button(root, textvariable=SettingsTextTk, padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][3]['background'], command=lambda: ShowSettings(SettingsText['Settings'], SettingsText['SettingsBack']))
    Credits = tk.Button(root, text='Credits', padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][3]['background'], command=lambda: ShowCredits(CreditsText['Credits'], CreditsText['CreditsBack']))

    Settings.place(x=360, y=20)
    Credits.place(x=60, y=20)
    SelectFile.pack()
    StartSpam.pack()

    #makes all the labels
    Version = tk.Label(frame, text=VersionNumber, padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][0]['frame'])      
    StopLabel1 = tk.Label(frame, text = "Move Your Mouse To The Top Left", padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][0]['frame'])
    StopLabel2 = tk.Label(frame, text = 'Corner To Stop The Countdown and Spam', padx=10, pady=5, fg=Modes[mode.get()][2]['text'], bg=Modes[mode.get()][0]['frame'])
    StopLabel1.place(x=90,y=30)
    StopLabel2.place(x=70,y=50)
    Version.place(x=350, y=300)   

    if PreferencesStorage['FilePath'] != '':
        filenameTk = tk.StringVar()
        filenameTk.set(PreferencesStorage['FilePath'])
        FileLabel = tk.Label(frame, textvariable=filenameTk, padx=10, pady=5, bg=Modes[mode.get()][3]['background'], fg=Modes[mode.get()][2]['text'])
        FileLabel.pack()

    root_menu = tk.Menu(root)
    root.config(menu=root_menu)
    options = tk.Menu(root_menu)

    root_menu.add_cascade(label='options', menu=options) 
    options.add_command(label='Save Preferences', command=lambda: SaveLoadPreferences('save'))
    options.add_command(label='Load Preferences', command=lambda: SaveLoadPreferences('load'))

if __name__ == '__main__':
    frame = tk.Frame(root, bg=Modes[mode.get()][0]['frame'])#'black')
    frame.place(relheight=0.8, relwidth=0.8, relx=0.05, rely=0.05, x=25, y=100)
    MakeChildren()

    root.mainloop()