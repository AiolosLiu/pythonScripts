# Author1:Xuguang Liu      
# Author2: Ming Li
# This assignment created a class that inherited Tk class in tkinter.
# The notepad transforms the original text to encrypted text,
# and be able to save and retrieve the results of notepad.

#! /usr/bin/env python
## ================================================
## Python Text Editor
## International Technological University
## Author: adapted from Web examples by  Richard Riehle, PhD
## 
## =======================================================
## This program is an example of how to create a simple
## text editor using Python.  It is not entirely original
## code. It is adapted from similar programs already
## published on various Python tutorial Web Sites.
## It has options to create new file, save file, save a file
## with a new name, and exit.
## We can also change the background theme colors
## the program displays the change in line number
## as we edit the file
# =========================================================
from tkinter import *  ## imports all the features of tkinter
from tkinter import messagebox as tkMessageBox
from tkinter import filedialog as tkFileDialog
import os  # import os for os related functions

root = Tk()  # creates the window
root.geometry("651x481+51+51")  # dimensions of the window
root.title("Ming&Xuguang's TextEditor")

# label present above below right left of menu bar

label1 = Label(root, bg="#ffffbb", height=2, width=1200)
label1.pack(side=TOP, expand=NO, fill=X)

label2 = Label(root, bg="antique white", height=800, width=2)
label2.pack(side=LEFT, expand=NO, fill=Y)

label4 = Label(root, bg="#e3ffff", height=800, width=2)
label4.pack(side=RIGHT, expand=NO, fill=Y)

# the area where we will enter text
textPad = Text(root, undo=TRUE, bg="light yellow", padx=20, pady=10)
textPad.pack(expand=YES, fill=BOTH)

textPad.file_opt = options = {}

label3 = Label(root, bg="#e3ffff", height=2, width=1200)
label3.pack(side=BOTTOM, expand=NO, fill=X)


class MyNotebook(Toplevel):
    def __init__(self, master=None):
        Toplevel.__init__(self, master)
        self.title("Ming&Xuguang's Notepad")

    # menu bar function'
    def new_file(self):
        # the ok cancel function of the messagebox
        if tkMessageBox.askokcancel("Save", "Do you want to save current file"):
            root.title("Untitled")
        global filename
        filename = None
        textPad.delete(1.0, END)

    # delete(start index,END index)

    # the open function
    def open_file(self):
        global filename
        filename = tkFileDialog.askopenfilename(defaultextension=".txt",
                                                filetypes=[("All files", "*.*"), ("Text Documents", "*.txt")])
        if filename == '':
            filename = None;
        else:
            root.title(os.path.basename(filename) + " -TextEditor")
            textPad.delete(1.0, END)
            fh = open(filename, "r")
            text = fh.read()
            text_copy = set(text)
            for i in text_copy:
                if i in characters:
                    text = text.replace(i, characters[i])
            textPad.insert(1.0, text)
            fh.close()

    # the save function
    def save(self):
        global filename
        try:
            f = open(filename, 'w')
            text = textPad.get(1.0, 'end')
            text_copy = set(text)
            for i in text_copy:
                if i in characters:
                    text = text.replace(i, characters[i])
            f.write(text)
            f.close()
        except:
            self.save_as()

    # the saveas function
    def save_as(self):
        try:
            f = tkFileDialog.asksaveasfilename(**textPad.file_opt)
            fh = open(f, 'w')
            text = textPad.get(1.0, END)
            text_copy = set(text)
            for i in text_copy:
                if i in characters:
                    text = text.replace(i, characters[i])
            fh.write(text)
            fh.close()
            root.title(os.path.basename(f))
        except:
            pass

    # the exit function
    def exit_editor(self, event=None):
        if tkMessageBox.askokcancel("quit", "Do you Want to quit?"):
            root.destroy()
        root.protocol('WM_DELETE_WINDOW', self.exit_command)  # override close

    ########EDIT MENU Functions############



    def update_line_number(self, event=None):
        txt = ''
        if showln.get():
            # split the string and return both parts
            # end -1c : The last character before the new line in line 2.
            endline, endcolumn = textPad.index('end-1c').split('.')
            txt = '\n'.join(map(str, range(1, int(endline))))
            label2.config(text=txt, anchor='nw')
            # Anchors are used to define where text is positioned relative to a reference point.
        currline, curcolumn = textPad.index("insert").split('.')
        infobar.config(text='Line: %s | Column: %s' % (currline, curcolumn))

    def theme(self):
        global bgc, fgc
        val = themechoice.get()
        clrs = clrschms.get(val)
        fgc, bgc = clrs.split('.')
        fgc, bgc = '#' + fgc, '#' + bgc
        textPad.config(bg=bgc, fg=fgc)

    ## ____________________________________________________
    # This procedure posts a menu at a given position
    # on the screen and configures Tk so that the menu
    # and its cascaded children can be traversed with
    # the mouse or the keyboard. Menu is the name of a
    # menu widget and x and y are the root coordinates
    # at which to display the menu.
    ## ____________________________________________________
    def popup(self, event):
        cmenu.tk_popup(event.x_root, event.y_root, 0)


# dictionary for changing theme colors
clrschms = {
    '1.  White': '000000.FFFFFF',
    '2.  Grey': '83406A.D1D4D1',
    '3.  Lavender': '202B4B.E1E1FF',
    '4.  Aquamarine': '5B8340.D1E7E0',
    '5.  Beige': '4B4620.FFF0E1',
    '6.  Blue': 'ffffBB.3333aa',
    '7.  Green': 'D1E7E0.5B8340',
}

# The text will match corresponding characters according to this dictionary.
characters = {
    'a': 'z', 'A': 'Z',
    'b': 'y', 'B': 'Y',
    'c': 'x', 'C': 'X',
    'd': 'w', 'D': 'W',
    'e': 'v', 'E': 'V',
    'f': 'u', 'F': 'U',
    'g': 't', 'G': 'T',
    'h': 's', 'H': 'S',
    'i': 'r', 'I': 'R',
    'j': 'q', 'J': 'Q',
    'k': 'p', 'K': 'P',
    'l': 'o', 'L': 'O',
    'm': 'n', 'M': 'N',
    'n': 'm', 'N': 'M',
    'o': 'l', 'O': 'L',
    'p': 'k', 'P': 'K',
    'q': 'j', 'Q': 'J',
    'r': 'i', 'R': 'I',
    's': 'h', 'S': 'H',
    't': 'g', 'T': 'G',
    'u': 'f', 'U': 'F',
    'v': 'e', 'V': 'E',
    'w': 'd', 'W': 'D',
    'x': 'c', 'X': 'C',
    'y': 'b', 'Y': 'B',
    'z': 'a', 'Z': 'A'
}
# menubar label and options
menubar = Menu(root)
# infobar=Label(label3)
# infobar.pack(expand=NO, side=RIGHT , anchor =SE)
infobar = Label(textPad, text='Line: 1 | Column: 0')
infobar.pack(expand=NO, fill=None, side=RIGHT, anchor='se')
# Create a notepad instance.
my_notepad = MyNotebook()
my_notepad.destroy()

# a menu can be torn off, the first position (position 0) in the list of choices is occupied by the tear-off element,
# and the additional choices are added starting at position 1. If you set tearoff=0,
# the menu will not have a tear-off feature, and choices will be added starting at position 0.
filemenu = Menu(menubar, tearoff=1)
filemenu.add_command(label="New", accelerator="Ctrl+N", command=my_notepad.new_file)
filemenu.add_command(label="Open", accelerator="Ctrl+O", command=my_notepad.open_file)
filemenu.add_command(label="Save", accelerator="Ctrl+S", command=my_notepad.save)
filemenu.add_command(label="Save As", accelerator="Shift+Ctrl+S", command=my_notepad.save_as)
filemenu.add_separator()
filemenu.add_command(label="Exit", accelerator="Alt+F4", command=my_notepad.exit_editor)
menubar.add_cascade(label="File", menu=filemenu)

editmenu = Menu(menubar, tearoff=1)
editmenu.add_command(label="Undo", accelerator="Ctrl+Z")
editmenu.add_command(label="Redo", accelerator="Ctrl+Y")
editmenu.add_separator()
editmenu.add_command(label="Delete", accelerator="Del")
editmenu.add_command(label="Clear", accelerator="Alt+Ctrl+C")
editmenu.add_separator()
menubar.add_cascade(label="Edit", menu=editmenu)
showinbar = IntVar()
viewmenu = Menu(menubar, tearoff=1)
themesmenu = Menu(viewmenu)
themechoice = StringVar()

## ___________________ End Menu Bar Definitions _______________________


for k in sorted(clrschms):
    themesmenu.add_radiobutton(label=k, variable=themechoice, command=my_notepad.theme)

# check box for theme menu
showln = IntVar()  # construct an interger variable
showln.set(1)

my_notepad.update_line_number()
viewmenu.add_checkbutton(label="Show Line Number", variable=showln)

viewmenu.add_cascade(label="Themes", menu=themesmenu)
menubar.add_cascade(label="View", menu=viewmenu)

scrollbar = Scrollbar(label4)

scrollbar.config(command=textPad.yview)
textPad.configure(yscrollcommand=scrollbar.set)

scrollbar.pack(side=RIGHT, fill=Y)
textPad.bind("<Any-KeyPress>", my_notepad.update_line_number)

# to use keyboard for executing the commands
textPad.bind('<Control-N>', my_notepad.new_file)
textPad.bind('<Control-n>', my_notepad.new_file)
textPad.bind('<Control-O>', my_notepad.open_file)
textPad.bind('<Control-o>', my_notepad.open_file)
textPad.bind('<Control-S>', my_notepad.save)
textPad.bind('<Control-s>', my_notepad.save)

root.config(menu=menubar)

root.mainloop()
