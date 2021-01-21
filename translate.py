from tkinter import *
from translate import Translator
from termcolor import colored
from tkinter import ttk
import pyttsx3

# Window Height And Width
window_height=1200
window_width=680

# Program Settings
root = Tk()
root.title('Your Title')
root.iconbitmap('C:/YourPath')
root.geometry(f"{window_height}x{window_width}")

#Functions
def translate():
    global translation
    words = word.get()
    from_language = from_lan.get()
    to_language = to_lan.get()

    translator = Translator(from_lang=from_language, to_lang=to_language)
    translation = translator.translate(words)
    notif.config(fg="green",text=f"--------------> {translation}")

def mySpeech():
    engine = pyttsx3.init()
    engine.say(translation)
    engine.runAndWait()

#Main Screen
ttk.Label(root, text='Translate Your Words:', font=("Calibri", 12)).grid(row=1, column=3, sticky=W, padx=30)

#Notification
notif = Label(root,font=("Calibri", 12))
notif.grid(row=7, column=3, sticky=W, padx=15)

#Variables
word = StringVar()
from_lan = StringVar()
to_lan = StringVar()

#Inputs
ttk.Label(root, text='From Language:', font=("Calibri", 12)).grid(row=4, column=2, sticky=W, padx=20)
ttk.Entry(root,width=50,textvariable=from_lan).grid(row=5, column=2, sticky=W, padx=6)

ttk.Label(root, text='To Language:', font=("Calibri", 12)).grid(row=4, column=3, sticky=W, padx=20)
ttk.Entry(root,width=50,textvariable=to_lan).grid(row=5, column=3, sticky=W, padx=6)

ttk.Label(root, text='The Words:', font=("Calibri", 12)).grid(row=6, column=2, sticky=W, padx=20)
ttk.Entry(root,width=50,textvariable=word).grid(row=7, column=2, sticky=W, padx=6)

#Button
ttk.Button(root,width=30,text="Translate",command=translate).grid(sticky=W,row=10)
ttk.Button(root,width=30,text="Speech",command=mySpeech).grid(sticky=W,row=11)

root.mainloop()
