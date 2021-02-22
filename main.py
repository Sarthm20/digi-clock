from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import datetime
root=Tk()
root.title("clock")

def time():
    now = datetime.now()
    string=now.strftime('%H:%M:%S')
    label.config(text=string)
    label.after(1000,time)

label=Label(root,font=("ds-digital",80),background="black",foreground="cyan")
label.pack(anchor='center')
time()


mainloop()
 
