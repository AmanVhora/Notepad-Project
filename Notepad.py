import os
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
from tkinter.messagebox import showinfo


def openFile():
    global FILE
    FILE = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if FILE == "":
        FILE = None
    else:
        root.title(os.path.basename(FILE) + " - Notepad")
        textArea.delete(1.0, END)
        f = open(FILE, "r")
        textArea.insert(1.0, f.read())
        f.close()


def newFile():
    global FILE
    root.title("Untitled - Notepad")
    FILE = None
    textArea.delete(1.0, END)


def save():
    global FILE
    if FILE is None:
        FILE = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                                                 ("Text Documents",
                                                                                                  "*.txt")])
        if FILE == "":
            FILE = None

        else:
            f = open(FILE, "w")
            f.write(textArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(FILE) + " - Notepad")
    else:
        f = open(FILE, "w")
        f.write(textArea.get(1.0, END))
        f.close()


def save_as():
    global FILE
    if FILE is None:
        FILE = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                                                 ("Text Documents",
                                                                                                  "*.txt")])
        if FILE == "":
            FILE = None

        else:
            f = open(FILE, "w")
            f.write(textArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(FILE) + " - Notepad")

    else:
        FILE = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                                                 ("Text Documents",
                                                                                                  "*.txt")])
        root.title(os.path.basename(FILE) + " - Notepad")
        f = open(FILE, "w")
        f.write(textArea.get(1.0, END))
        f.close()


def theme1():
    textArea.configure(bg="white")


def theme2():
    root.configure(bg="white")


def theme3():
    textArea.configure(bg="black", fg="white", insertbackground="white")


def theme4():
    textArea.configure(bg="lightblue")


def cut():
    textArea.event_generate("<<Cut>>")


def copy():
    textArea.event_generate("<<Copy>>")


def paste():
    textArea.event_generate("<<Paste>>")


def selectAll():
    textArea.event_generate("<<SelectAll>>")


def about():
    showinfo("About", "Notepad By Aman Vhora")


root = Tk()
root.minsize(400, 450)
root.title("Untitled - Notepad")
root.wm_iconbitmap("Notepad.ico")

textArea = Text(root, font="Arial 12")
FILE = None
textArea.pack(expand=True, fill=BOTH)
MenuBar = Menu(root)

#  File Menu
file = Menu(root, tearoff=0)
file.add_command(label="Open", command=openFile)
file.add_command(label="New", command=newFile)
file.add_command(label="Save", command=save)
file.add_command(label="Save As", command=save_as)
file.add_separator()

th = Menu(file, tearoff=0)
th.add_command(label="Default", command=theme1)
th.add_command(label="Light", command=theme2)
th.add_command(label="Dark", command=theme3)
th.add_command(label="Light Blue", command=theme4)
file.add_cascade(label="Theme", menu=th)

file.add_command(label="Quit", command=quit)
MenuBar.add_cascade(label="File", menu=file)
root.config(menu=MenuBar)

# Edit Menu
edit = Menu(root, tearoff=0)
edit.add_command(label="Cut", command=cut)
edit.add_command(label="Copy", command=copy)
edit.add_command(label="Paste", command=paste)
edit.add_command(label="Select All", command=selectAll)
MenuBar.add_cascade(label="Edit", menu=edit)
root.config(menu=MenuBar)

# Help Menu
help = Menu(root, tearoff=0)
help.add_command(label="About", command=about)
MenuBar.add_cascade(label="Help", menu=help)
root.config(menu=MenuBar)

Scroll = Scrollbar(textArea)
Scroll.pack(side=RIGHT, fill=Y)
Scroll.config(command=textArea.yview)
textArea.config(yscrollcommand=Scroll.set)

root.mainloop()
