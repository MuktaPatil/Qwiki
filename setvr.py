import tkinter
from tkinter import *
from tkinter import ttk
import vr

def getacr(language):
    if language == "Hindi":
        l = "hi-IN"
    elif language == "Marathi":
        l = "mr-IN"
    else:
        l = "en-IN"

    return l


def getlang(langs):
    if langs == "Hindi":
        lx = "hi"
    elif langs == "Marathi":
        lx = "mr"
    else:
        lx = "en"

    return lx


def show():
    x = clicked.get()
    ipt = "Selected Input Language:  " + x
    my_label.config(text=ipt)


def disp():
    y = lang.get()
    lg = "Selected Language:  " + y
    my_label2.config(text=lg)


def run_vr():
    # root.destroy()
    x = clicked.get()
    il = getacr(x)

    y = lang.get()
    wl = getlang(y)
    vr.virtual_assistant(il, wl)


root = Tk()
root.minsize(600,450)
options = [
    "Hindi",
    "Marathi",
    "English"
]

clicked = tkinter.StringVar()
lang = tkinter.StringVar()



# Input Language
s = "Please select the language of input:  "
instr1 = Label(root, text=s).place(x=150, y=56, anchor="center")
d = OptionMenu(root, clicked, *options)
d.configure(background="#ffdbf4",foreground="black")
d["menu"].configure(background="#ffdede",foreground="black")
d.place(x=330, y=56, anchor="center")
clicked.set("English")
my_label = Label(root, text="")
b1 = Button(root, text="Submit", command=show)
b1.configure(foreground="black", background="#bcdffd")
b1.place(x=330, y=100, anchor="center")

my_label.place(x=280, y=150, anchor="center")

# Find wikipedia language

w = "Please select the language of Wikipedia Results:  "
instr2 = Label(root, text=w).place(x=180, y=196, anchor="center")
dx = OptionMenu(root, lang, *options)
dx.configure(background="#ffdbf4",foreground="black")
dx["menu"].configure(background="#ffdede",foreground="black")
dx.place(x=397, y=196, anchor="center")
lang.set("English")
my_label2 = Label(root, text="")
b2 = Button(root, text="Submit", command=disp)
b2.configure(foreground="black", background="#bcdffd")
b2.place(x=397, y=240, anchor="center")
my_label2.place(x=350, y=270, anchor="center")

b3 = Button(root, text="Run Virtual Assistant", command=lambda: run_vr())
b3.configure(foreground="black", background="#bce3b5")
b3. place(x= 398, y=300,anchor="center")

b4 = Button(root, text="Exit", command=lambda: exit())
b4.configure(foreground="black", background="#bce3b5")
b4.place(x= 405, y=340,anchor="center")


root.mainloop()

