import tkinter as t
from tkinter import filedialog as fd
from tkinter import ttk




def open_file():
    file=fd.askopenfile(mode='r')
    if file is not None:
        content=file.read()
        print(content)
win=t.Tk()
btn=ttk.Button(win,text="Open",command=open_file)
btn.pack(side="top",pady=10)
win.mainloop()
