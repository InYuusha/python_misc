import tkinter as t
from tkinter import ttk
win=t.Tk()

win.title("example")

ttk.Label(win,text="hello world").grid(column=0,row=0)
win.mainloop()
