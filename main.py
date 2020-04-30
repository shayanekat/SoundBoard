# Author : Shayane Katchera
# SoundBoard Python app

# place new sound .wav in the sound folder

import winsound
from tkinter import *

# ====Backend====
def fucked_up():
    winsound.PlaySound(".\sounds\he_fucked_up",winsound.SND_FILENAME)

def damn():
    winsound.PlaySound(".\sounds\damn",winsound.SND_FILENAME)

def bruh():
    winsound.PlaySound(".\sounds\cruh",winsound.SND_FILENAME)

def honteux():
    winsound.PlaySound(".\sounds\honteux",winsound.SND_FILENAME)

def wtf():
    winsound.PlaySound(".\sounds\wtf",winsound.SND_FILENAME)

def oh():
    winsound.PlaySound(".\sounds\oh",winsound.SND_FILENAME)

def shine():
    winsound.PlaySound(".\sounds\shine",winsound.SND_FILENAME)

def nani():
    winsound.PlaySound(".\sounds\what",winsound.SND_FILENAME)

def yeah():
    winsound.PlaySound(".\sounds\yeah",winsound.SND_FILENAME)

# ====frontend====
root = Tk()
root.title("Sound Board")


title = Label(root,text="Sound Board",font=('Calibri', 36, 'bold','underline'))
title.grid(row=0,columnspan=5,padx=5,pady=5)
space = Label(root,text="")
space.grid(row=1,column=1,padx=5,pady=5)


b11 = Button(root,text="He Fucked Up",command=fucked_up)
b11.grid(row=2,column=0,padx=5,pady=5)

b12 = Button(root,text="damn",command=damn)
b12.grid(row=2,column=1,padx=5,pady=5)

b13 = Button(root,text="bruh",command=bruh)
b13.grid(row=2,column=2,padx=5,pady=5)

b14 = Button(root,text="C'est Honteux",command=honteux)
b14.grid(row=2,column=3,padx=5,pady=5)

b15 = Button(root,text="WTF BOOM",command=wtf)
b15.grid(row=2,column=4,padx=5,pady=5)

b21 = Button(root,text="OOOOHHHHH",command=oh)
b21.grid(row=3,column=0,padx=5,pady=5)

b22 = Button(root,text="Shindehiru",command=shine)
b22.grid(row=3,column=1,padx=5,pady=5)

b23 = Button(root,text="NANNI",command=nani)
b23.grid(row=3,column=2,padx=5,pady=5)

b24 = Button(root,text="YEAH!",command=yeah)
b24.grid(row=3,column=3,padx=5,pady=5)


root.mainloop()
