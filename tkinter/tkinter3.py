import tkinter as t
from tkinter import ttk
from tkinter import Menu

win=t.Tk()
win.title('Interface')

color='red'
color2='pink'
color3='green'
color4='black'

zel=ttk.LabelFrame(win,text='zeldoris')
zel.grid(column=3,row=1,padx=30,pady=30)

lab=ttk.Label(zel,text='Enter Your Name')
lab.grid(column=1,row=2)

lab2=ttk.Label(zel,text="Choose Your country")
lab2.grid(column=2,row=2)

lab3=ttk.Label(zel,text="")
lab3.grid(column=1,row=4)

bmnu=Menu(win)
win.configure(menu=bmnu)


fmnu=Menu(bmnu)
bmnu.add_cascade(label='File',menu=fmnu)
fmnu.add_command(label='new')

fmnu.add_separator()

fmnu.add_command(label='exit')

hmnu=Menu(bmnu)
bmnu.add_cascade(label='help',menu=hmnu)
hmnu.add_command(label='About')


def clicked():
    lab3.configure(text='Hello '+name.get()+" You live in "+country.get())
    
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
inputobj=ttk.Entry(zel,width=20,textvariable=name)
inputobj.grid(column=1,row=3)

country=t.StringVar()
drpbox=ttk.Combobox(zel,width=15,textvariable=country)
drpbox.grid(column=2,row=3)
drpbox['values']=('country','Armenia','America','Spain','Germany','India','Japan')
drpbox.current(0)

butt=ttk.Button(zel,text="Submit",command=clicked)
butt.grid(column=4,row=3)

radvar=t.IntVar()
rad=t.Radiobutton(zel,text=color,variable=radvar,value=1,command=radcall)
rad.grid(column=1,row=5)

rad2=t.Radiobutton(zel,text=color2,variable=radvar,value=2,command=radcall)
rad2.grid(column=2,row=5,sticky=t.N)

rad3=t.Radiobutton(zel,text=color3,variable=radvar,value=3,command=radcall)
rad3.grid(column=3,row=5,sticky=t.N)

rad4=t.Radiobutton(zel,text=color4,variable=radvar,value=4,command=radcall)
rad4.grid(column=4,row=5,sticky=t.N)

inputobj.focus()



win.mainloop()



