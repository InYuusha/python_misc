import tkinter as t
from tkinter import ttk
from tkinter import messagebox as msg
import os
from tkinter import filedialog as fd
class copy_gui:
    
    def __init__(self):
        self.win=t.Tk()
        self.win.configure(background="black")
        self.create_widgets()
        
    def create_widgets(self):
        self.zel=ttk.LabelFrame(self.win,text="Zeldoris")
        self.zel.grid(column=2,row=2,padx=30,pady=50)
        
        self.butts=ttk.Button(self.zel,text="Browse Source location",command=self.entrys_focus)
        self.butts.grid(column=1,row=3)
        
        self.buttd=ttk.Button(self.zel,text="Browse Destination location",command=self.entryd_focus)
        self.buttd.grid(column=1,row=4,padx=20,pady=20)

        self.buttsu=ttk.Button(self.zel,text="Copy",command=self.copyf)
        self.buttsu.grid(column=2,row=5)
        
        self.slocate=t.StringVar()
        self.entrys=ttk.Entry(self.zel,width=20,textvariable=self.slocate)
        self.entrys.grid(column=2,row=3)
        self.entrys.insert(3,'Source Path')
        
        self.dlocate=t.StringVar()
        self.entryd=ttk.Entry(self.zel,width=20,textvariable=self.dlocate)
        self.entryd.grid(column=2,row=4)
        self.entryd.insert(2,"Destination Path")
        
    def entryd_focus(self):
        file=list(fd.askdirectory())
        self.ddir="".join(file)
        self.ddir.strip("")
        self.ddir=str(self.ddir+"\\New")
        self.entryd.delete(0,t.END)
        self.entryd.insert(0,self.ddir)
        
    
    def entrys_focus(self):
        filed=list(fd.askdirectory(initialdir="C:\\Users\\op\\Desktop"))
        self.spath="".join(filed)
        self.spath.strip("")
        self.entrys.delete(0,t.END)
        self.entrys.insert(0,self.spath)
      

    def copyf(self):
        import shutil as stl
        s=self.entrys.get()
        d=self.entryd.get()
        try:   
            stl.copytree(s,d)
            msg.showinfo("Copy File"," File copied succesfully")
            
        except :
            msg.showerror("Copy File ","Failed to Copy File to Network")

run=copy_gui()
run.win.mainloop()

        
        
