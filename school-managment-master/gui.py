from tkinter import *
from tkinter.ttk import Notebook
root=Tk()
note=Notebook()

s_insert=Frame()
s_update=Frame()
s_delete=Frame()

note.add(s_insert, text='INSERT')
note.add(s_update,text= 'UPDATE')


note.grid()
Label(s_insert,text='name').grid()
name=StringVar()
Entry(s_insert,textvariable=name).grid()
root.mainloop()