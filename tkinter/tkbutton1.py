import tkinter as t
from tkinter import ttk
win=t.Tk()
lab=ttk.Label(win,text="Enter a name:")
lab.grid(column=1,row=0)

lab0=ttk.Label(win,text="Choose your country:")
lab0.grid(column=2,row=0)

lab2=ttk.Label(win,text="")
lab2.grid(column=1,row=3)
def clicked():
    lab2.configure(text="Hello "+name.get()+" You live in "+country.get()) 
    
    
    
action=ttk.Button(win,text="Click me",command=clicked)
action.grid(column=3,row=1)

name=t.StringVar()
inputobj=ttk.Entry(win,width=20,textvariable=name)
inputobj.grid(column=1,row=1)

country=t.StringVar()
drp=ttk.Combobox(win,width=20,textvariable=country)
drp.grid(column=2,row=1)
drp['values']=('Country','India','Greece','USA','Russia','Spain')
drp.current(0)

checkvar=t.IntVar()
check=t.Checkbutton(win,text="Male",variable=checkvar)
check.grid(column=1,row=4,sticky=t.N)
check.select()

checkvar2=t.IntVar()
check2=t.Checkbutton(win,text='Teenage',variable=checkvar2)
check2.grid(column=2,row=4,sticky=t.N)
check2.deselect()

checkvar3=t.IntVar()
check3=t.Checkbutton(win,text="student",variable=checkvar3)
check3.grid(column=3,row=4,sticky=t.W)
check.select()


inputobj.focus()
win.mainloop()



