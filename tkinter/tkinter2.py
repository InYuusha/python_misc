import tkinter as t
from tkinter import ttk

win=t.Tk()
win.title('Interface')
color='red'
color2='blue'
color3='purple'
color4='pink'

zel=ttk.LabelFrame(win,text='Zeldoris')
zel.grid(column=0,row=0,padx=8,pady=4)
lab=ttk.Label(zel,text="Enter Your Name")
lab.grid(column=1,row=1)

lab2=ttk.Label(zel,text="Choose Your Country")
lab2.grid(column=2,row=1)

lab3=ttk.Label(zel,text="")
lab3.grid(column=1,row=3)
def clicked():
    lab3.configure(text="Hello "+name.get()+" You Live in :"+country.get())

def radcall():
    col=radvar.get()
    if col==1:
        win.configure(background=color)
    elif col==2:
        win.configure(background=color2)
    elif col==3:
        win.configure(background=color3)
    elif col==4:
        win.configure(background=color4)
   

name=t.StringVar()
inputobj=ttk.Entry(zel,width=10,textvariable=name)
inputobj.grid(column=1,row=2)

country=t.StringVar()
drpbox=ttk.Combobox(zel,width=15,textvariable=country)
drpbox.grid(column=2,row=2)
drpbox['values']=('Country','Armenia','Argentina','America','Iran','India','Syria')
drpbox.current(0)

submit=ttk.Button(zel,text="Submit",command=clicked)
submit.grid(column=3,row=2)

radvar=t.IntVar()
rad=t.Radiobutton(zel,text=color,variable=radvar,value=1,command=radcall)
rad.grid(column=1,row=5,sticky=t.N)

rad2=t.Radiobutton(zel,text=color2,variable=radvar,value=2,command=radcall)
rad2.grid(column=2,row=5,sticky=t.N)

rad3=t.Radiobutton(zel,text=color3,variable=radvar,value=3,command=radcall)
rad3.grid(column=3,row=5,sticky=t.N)

rad4=t.Radiobutton(zel,text=color4,variable=radvar,value=4,command=radcall)
rad4.grid(column=4,row=5,sticky=t.E)



inputobj.focus()
win.mainloop()
