from tkinter import *
from tkinter import ttk
from database import db_t
from tkinter import messagebox
root=Tk()
tab_parent=ttk.Notebook(root)
tab1 = ttk.Frame(tab_parent)
tab2 = ttk.Frame(tab_parent)
tab_parent.add(tab1, text="register")
tab_parent.add(tab2, text="login")
tab_parent.pack(expand=1, fill='both')
def login():
    n=db_t()
    cn,cr=n.connectschool()
    data=(e3.get(),e4.get())
    query="select username,password from account"
    cr.execute(query)
    cn.commit()
    for i in cr:
        if i == data:
            r=str(i)
            e=(str(r)).split(',')
            t=e[0]
            k=(str(t)).split("(")
            q=k[1]
            n = (str(q)).split("'")
            print(n)
            v=n[1]
            x=str(v)
            z=v.strip("'")

            messagebox.showinfo("logged in", "hi"+" " + str(z))

def delete():
    n=db_t()
    cn,cr=n.connectschool()
    query="DELETE FROM account where username='sepehr'"
    cr.execute(query)
    cn.commit()
def show():
    n=db_t()
    cn,cr=n.connectschool()
    query="select * from account"
    cr.execute(query)
    cn.commit()
    for i in cr:
        print(i)
def insert():
    n=db_t()
    cn,cr=n.connectschool()
    query="insert into account(username, password) values (%s,%s)"
    data=(e1.get(),e2.get())
    cr.execute(query,data)
    cn.commit()
l1=Label(tab1,text="username").grid(row=0,column=0)
e1=Entry(tab1)
e1.grid(row=0,column=1)
l2=Label(tab1,text="password").grid(row=1,column=0)
e2=Entry(tab1)
e2.grid(row=1,column=1)
b1=Button(tab1,text="register",command=insert).grid(row=5,column=1)
l3=Label(tab2,text="username").grid(row=0,column=0)
e3=Entry(tab2)
e3.grid(row=0,column=1)
l4=Label(tab2,text="password").grid(row=1,column=0)
e4=Entry(tab2)
e4.grid(row=1,column=1)
b2=Button(tab2,text="login",command=login).grid(row=5,column=1)
show()

root.mainloop()
