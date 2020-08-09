from tkinter import *
from tkinter import scrolledtext
from tkfontchooser import askfont
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os
from tkinter.messagebox import showerror
from tkinter import colorchooser
import pyttsx3

window = Tk()

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voice', voices[0].id)


#Functions of menu
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# def Read():
#     speak("Aadi Jain")

def newFile():
    global file
    window.title("Unknown File - Notepad")
    file = None
    text.delete(1.0, END)

def openfile():
    global file
    file = askopenfilename(defaultextension="*.*",
                           filetypes=[("Text Documents", "*.txt"), ("Python Files", "*.py"), ("All Files", "*.*")])
    if file == "":
        file = None
    else:
        window.title(os.path.basename(file) + " > AL-Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

def save():
    global file
    file = asksaveasfilename(initialfile="Unknown.txt", defaultextension="*.txt"
                             , filetypes=[("Text Document", "*.txt"), ("Python File", "*.py"),
                                          ("Python File (No Console)", "*.pyw"), ("All Files", "*.*")])
    if file == "":
        file = None
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

        window.wm_title(os.path.basename(file) + "- Notepad")


def saveas():
    global file
    file = asksaveasfilename(initialfile="Unknown.txt", defaultextension="*.txt"
                             , filetypes=[("Text Document", "*.txt"), ("Python File", "*.py"),
                                          ("Python File (No Console)", "*.pyw"), ("All Files", "*.*")])

    if file == "":
        file = None
    else:
        Saveas = text.get(1.0, END)
        file.write(saveas.fstrip())
        file.write("\n")


def quitApp():
    window.destroy()

def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))

def bgcolor():
    if i.get() == 1:
        showerror("Error", "Please First Uncheck Random Mode")
    else:
        r = colorchooser.askcolor(title = " Choose Background Color")
        text.config(bg = r[1])


def fontcolor():
    if i.get() == 1:
        showerror("Error", "Please First Uncheck Random Mode")
    else:
        r = colorchooser.askcolor(title=" Choose Background Color")
        text.config(fg=r[1])

def date():
    from datetime import datetime
    d = datetime.now()
    text.insert(INSERT, d.strftime(' %d-%m-%Y  %H:%M:%S'))

def black():
    if i.get() == 1:
        showerror("Error", "Please First Uncheck Random Mode")
    else:
        text.config(bg='black', fg='white', insertbackground='white')
        FileMenu.config(bg='black', fg='white')
        EditMenu.config(bg='black', fg='white')
        HelpMenu.config(bg='black', fg='white')
        format.config(bg='black', fg='white')

def white():
    if i.get() == 1:
        showerror("Error", "Please First Uncheck Random Mode")
    else:
        text.config(bg='white', fg='black', insertbackground='black')
        FileMenu.config(bg='white', fg='black')
        EditMenu.config(bg='white', fg='black')
        HelpMenu.config(bg='white', fg='black')
        format.config(bg='white', fg='black')

def ran():
    from random import choice
    if i.get() == 1:
        colourvalues = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        colourcode = '#'
        for c in range(0, 6):
            colourcode = colourcode + choice(colourvalues)
        text.config(bg=colourcode, fg='white')
        FileMenu.config(bg=colourcode, fg='white')
        EditMenu.config(bg=colourcode, fg='white')
        HelpMenu.config(bg=colourcode, fg='white')
        format.config(bg=colourcode, fg='white')
        window.after(3000, ran)

def wordwrap():
    if j.get() == 1:
        text.config(wrap=WORD)
        Scroll.pack_forget()
    else:
        text.config(wrap=NONE)

def font():
    font = askfont(window)
    if font:
        font['family'] = font['family'].replace(' ', '\ ')
        font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
        if font['underline']:
            font_str += ' underline'
        if font['overstrike']:
            font_str += ' overstrike'
        text.configure(font=font_str)

def statusbar():
    if k.get() == 1:
        lc = text.index(INSERT)
        status.config(text=lc)
        window.after(100, statusbar)
    else:
        status.config(text='0.0')

def about():
    pass

def aboutauthor():
    pass


if __name__ == '__main__':
    #Basic Setup
    window.title("Unknown File - Notepad")
    window.geometry("450x450")
    #Textarea setup
    text = scrolledtext.ScrolledText(window,font = "lucida 10")
    fill = None
    text.pack(expand = True, fill = BOTH)

        #Main Menu Setup
    # create a menubar
    MenuBar = Menu(window)
    window.config(menu=MenuBar)

    # create File drop down menu
    FileMenu = Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label="File", menu=FileMenu)
    # create options in File menu
    FileMenu.add_command(label="New", command=newFile, accelerator='Ctrl+N')
    FileMenu.add_command(label="Open...", command=openfile, accelerator='Ctrl+O')
    FileMenu.add_command(label="Save", command=save, accelerator='Ctrl+S')
    FileMenu.add_command(label="Save As...", command=saveas, accelerator='Shift+Ctrl+S')
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=quitApp, accelerator='Ctrl+Q')
    # create Edit drop down menu
    EditMenu = Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)
    # create options in edit menu
    EditMenu.add_command(label='Undo', command=text.edit_undo, accelerator='Ctrl+Z')
    EditMenu.add_command(label='Redo', command=text.edit_redo, accelerator='Ctrl+Y')
    EditMenu.add_separator()
    EditMenu.add_command(label="Cut", command=cut, accelerator='Ctrl+X')
    EditMenu.add_command(label="Copy", command=copy, accelerator='Ctrl+C')
    EditMenu.add_command(label="Paste", command=paste, accelerator='Ctrl+V')
    EditMenu.add_separator()
    EditMenu.add_command(label='Background colour', command=bgcolor, accelerator='Ctrl+Alt+B')
    EditMenu.add_command(label='Font colour', command=fontcolor, accelerator='Ctrl+Alt+F')
    EditMenu.add_separator()
    EditMenu.add_command(label='DateTime', command=date, accelerator='Ctrl+D')
    EditMenu.add_separator()
    # create Mode drop down menu in Edit menu
    mode = Menu(EditMenu, tearoff=0)
    EditMenu.add_cascade(label='Mode', menu=mode)
    # EditMenu.add_separator()
    # EditMenu.add_cascade(label='Read Text', menu=Read)
    # create option in Mode menu who is situated in Edit menu
    mode.add_radiobutton(label='Black Mode', command=black, accelerator='Alt+B')
    mode.add_radiobutton(label='White Mode', command=white, accelerator='Alt+W')
    mode.add_separator()
    i = IntVar()
    mode.add_checkbutton(label='Random Mode', variable=i, command=ran)

    # create Format drop down menu
    format = Menu(MenuBar, tearoff=False)
    MenuBar.add_cascade(label='Format', menu=format)
    # create option in format menu
    j = IntVar()
    format.add_checkbutton(label="Word Wrap", variable=j, command=wordwrap)
    format.add_command(label="Font...", command=font, accelerator='Ctrl+F')
    k = IntVar()
    format.add_checkbutton(label="Start Status Bar", variable=k, command=statusbar)

    # create Help drop down menu
    HelpMenu = Menu(MenuBar, tearoff=0)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)
    # create options in help menu
    HelpMenu.add_command(label="About Notepad", command=about, accelerator='Shift+Ctrl+A')
    HelpMenu.add_command(label="About Author", command=aboutauthor)

    window.protocol('WM_DELETE_WINDOW', quitApp)

    # Horizontal scroll bar
    Scroll = Scrollbar(text, orient = HORIZONTAL)
    Scroll.pack(side = BOTTOM, fill = X)
    Scroll.config(command = text.xview)
    text.config(yscrollcommand = Scroll.set)

    #Status Bar
    statusframe = LabelFrame(window, text='Line.Column')
    statusframe.pack(side=BOTTOM, anchor=E)
    status = Label(statusframe, text='0.0', font='Lucida 13 bold')
    status.pack(side=BOTTOM)


window.mainloop()