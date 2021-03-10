import tkinter as t
from tkinter import ttk

win=t.Tk()
win.geometry('80x800')

tabc=ttk.Notebook(win)
tab1=ttk.Frame(tabc)
tabc.add(tab1,text="UI")
tab2=ttk.Frame(tabc)
tabc.add(tab2,text="setting")
tab3=ttk.Frame(tabc)
tabc.add(tab3,text="Canvas")
tabc.pack(expand=1,fill="both")

tab3_frame=t.Frame(tab3,bg='blue')
tab3_frame.pack(fill="both",expand=1)
for i in range(0,10,2):
    
       canvas=t.Canvas(tab3_frame,width=120,bg='red',height=80,highlightthickness=0 )
       canvas.grid(column=i,row=i)
