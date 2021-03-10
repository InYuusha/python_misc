import tkinter as t
from tkinter import ttk
win=t.Tk()
win.title("hello")
lab=ttk.Label(win,text="hello world")
lab.grid(column=2,row=3)
def clicked():
    
    butt.configure(text="I have been clicked")
    lab.configure(foreground='red')
    lab.configure(text="bye")
    
butt=ttk.Button(win,text="click me",command=clicked)
butt.grid(row=5,column=10)
