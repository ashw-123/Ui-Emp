from tkinter import *
import tkinter as tk
from tkinter import ttk,messagebox
import sqlite3 as sq
root=tk.Tk()
root.title('Mini Project')
root.geometry('1280x720')
con = sq.connect('project.sqlite')
cur = con.cursor()
cur.execute('create table if not exists EMPDETAILS(Employee_id int,Name text,Contact int,Gender text,Email text,Designation text,Salary int)')

def add():
    Employee_id=empid.get()
    Name = name.get()
    Contact=contact.get()
    Gender=gender.get()
    Email=email.get()
    Designation=designation.get()
    Salary=salary.get()
    con.execute('insert into EMPDETAILS values(?,?,?,?,?,?,?)',(Employee_id,Name,Contact,Gender,Email,Designation,Salary))
    #print('inserted')
    #res=con.execute('select *from EMPDETAILS')
    #for row in res:
        #print(row)
    con.commit()
        
def update():
    data=(name.get(),contact.get(),email.get(),designation.get(),salary.get(),empid.get())
    con.execute("update EMPDETAILS set Name=?,Contact=?,Email=?,Designation=?,Salary=? where Employee_id =?",(data))
    #print("one row updated")
    con.execute('select *from EMPDETAILS')
    #for row in res:
        #print(row)
    con.commit()
def print_data():
    if empid.get()==0 or name.get()=='' or gender.get()=='' or email.get()=='' or designation.get()=='' or salary.get()=='':
        messagebox.showerror('Error','All fields are required ?')
    else:
        #textarea.delete(1.0,END)
        textarea.insert(END, '\n==============================================')
        textarea.insert(END, f'\nEmployee Ref\t\t\t\t{empid.get()}')
        textarea.insert(END, '\n==============================================')
        textarea.insert(END, f'\n\nFull Name\t\t\t\t{name.get()}')
        textarea.insert(END, f'\nEmail Id\t\t\t\t{email.get()}')
        textarea.insert(END, f'\nGender \t\t\t\t{gender.get()}')
        textarea.insert(END, f'\nDesignation\t\t\t\t{designation.get()}')
        textarea.insert(END, f'\nContact Number\t\t\t\t{contact.get()}')
        textarea.insert(END, f'\n Salary\t\t\t\t{salary.get()}')
        textarea.insert(END, '\n\n##################################################')


def delete():
    con.execute("delete from EMPDETAILS where Employee_id =?",( empid.get(),))
    #print('deleted one row')
    con.execute('select *from EMPDETAILS')
    #for row in res:
        #print(row)
    con.commit()
        
def quit():
    #print('quitted')
    #con.close()
    root.destroy()
    
# title
title=Label(root,text='Employee Management System',bg='LIGHT BLUE',fg='black',font=('times new rommon',35,'bold'),relief=RAISED,bd=20)
title.pack(fill='x')


empid=IntVar()
name=StringVar()
contact=IntVar()
gender=StringVar()
email=StringVar()
designation=StringVar()
salary=IntVar()
F1=Frame(root,bg='white',relief=RIDGE,bd=15)
F1.place(x=20,y=100,width=750,height=1000)
# id
lbl=Label(F1,text='Employee id',font=('times new rommon',20,'bold'),fg='black')
lbl.grid(row=0,column=0,padx=30,pady=10)
txt=Entry(F1,font=('times new rommon',18,'bold'),relief=RAISED,bd=7,textvariable=empid)
txt.grid(row=0,column=1,pady=10)

#name
lbl=Label(F1,text='Employee Name',font=('times new rommon',20,'bold'),fg='black')
lbl.grid(row=1,column=0,padx=30,pady=10)
txt=Entry(F1,font=('times new rommon',18,'bold'),relief=RAISED,bd=7,textvariable=name)
txt.grid(row=1,column=1,pady=10)

#contact
lbl=Label(F1,text='Contact',font=('times new rommon',20,'bold'),fg='black')
lbl.grid(row=2,column=0,padx=30,pady=10)
txt=Entry(F1,font=('times new rommon',18,'bold'),relief=RAISED,bd=7,textvariable=contact)
txt.grid(row=2,column=1,pady=10)

#gender
lbl=Label(F1,text='Gender',font=('times new rommon',20,'bold'),fg='black')
lbl.grid(row=3,column=0,padx=30,pady=10)
comboGender = ttk.Combobox(F1, font=("times new rommon", 18,'bold'), width=18, textvariable=gender, state="readonly")
comboGender['values'] = ("Male", "Female","other")
comboGender.grid(row=3, column=1, padx=10)

#email
lbl=Label(F1,text='Email',font=('times new rommon',20,'bold'),fg='black')
lbl.grid(row=4,column=0,padx=30,pady=10)
txt=Entry(F1,font=('times new rommon',18,'bold'),relief=RAISED,bd=7,textvariable=email)
txt.grid(row=4,column=1,pady=10)

#designation
lbl=Label(F1,text='Designation',font=('times new rommon',20,'bold'),fg='black')
lbl.grid(row=5,column=0,padx=30,pady=10)
txt=Entry(F1,font=('times new rommon',18,'bold'),relief=RAISED,bd=7,textvariable=designation)
txt.grid(row=5,column=1,pady=10)

#salary
lbl=Label(F1,text='Salary',font=('times new rommon',20,'bold'),fg='black')
lbl.grid(row=6,column=0,padx=30,pady=10)
txt=Entry(F1,font=('times new rommon',18,'bold'),relief=RAISED,bd=7,textvariable=salary)
txt.grid(row=6,column=1,pady=10)

#buttons
F2=Frame(root,bg='light blue',relief=RIDGE,bd=15)
F2.place(x=20,y=715,width=1460,height=200)

 


btn1=Button(F2,text='Add ',font='arial 20 bold',bg='white',fg='black',width=10,command=add)
btn1.grid(row=0,column=0,padx=25,pady=7)

 

btn3=Button(F2,text='Update',font='arial 20 bold',bg='white',fg='black',width=10,command=update)
btn3.grid(row=0,column=2,padx=25,pady=7)

 

btn4=Button(F2,text='Delete',font='arial 20 bold',bg='white',fg='black',width=10,command=delete)
btn4.grid(row=0,column=3,padx=25,pady=7)



btn5=Button(F2,text='Print',font='arial 20 bold',bg='white',fg='black',width=10,command=print_data)
btn5.grid(row=0,column=4,padx=25,pady=7)



btn6=Button(F2,text='Exit',font='arial 20 bold',bg='white',fg='black',width=10,command=quit)
btn6.grid(row=0,column=5,padx=25,pady=7)



#==========================Right frame================
F3=Frame(root,bg='light blue',relief=RIDGE,bd=15)
F3.place(x=765,y=95,width=780,height=620)

lbl_t=Label(F3,text='Employee Details',font=('arial 15 bold'),fg='black',bd=7,relief=GROOVE)
lbl_t.pack(fill=X)

scrol=Scrollbar(F3,orient=VERTICAL)
scrol.pack(side=RIGHT,fill=Y)
textarea=Text(F3,font='arial 15',yscrollcommand=scrol.set)
textarea.pack(fill=BOTH)
scrol.config(command=textarea.yview)



 

 

 

root.mainloop()