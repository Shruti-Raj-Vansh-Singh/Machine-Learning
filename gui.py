# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 16:33:18 2019

@author: shruti
"""

from tkinter import *
from functools import partial  
values=[[0,0,0,0,0,0,0,0,0,0]]
root = Tk()
label1= Label(root,text="Enter the values of the following to check whether the person is diabetic or not")
label1.grid(row=0)

e2=StringVar()
e3=StringVar()
e4=StringVar()
e5=StringVar()
e6=StringVar()
e7=StringVar()
e8=StringVar()
e9=StringVar()


label2=Label(root,text="Preganancies:")
label2.grid(row=1)
entry2=Entry(root,textvariable=e2)
entry2.grid(row=1,column=1)

label3=Label(root,text="Glucose:")
label3.grid(row=2)
entry3=Entry(root,textvariable=e3)
entry3.grid(row=2,column=1)

label4=Label(root,text="Blood pressure")
label4.grid(row=3)
entry4=Entry(root,textvariable=e4)
entry4.grid(row=3,column=1)

label5=Label(root,text="Skin thickness:")
label5.grid(row=4)
entry5=Entry(root,textvariable=e5)
entry5.grid(row=4,column=1)

label6=Label(root,text="insulin:")
label6.grid(row=5)
entry6=Entry(root,textvariable=e6)
entry6.grid(row=5,column=1)

label7=Label(root,text="BMI")
label7.grid(row=6)
entry7=Entry(root,textvariable=e7)
entry7.grid(row=6,column=1)

label8=Label(root,text="Diabetes Pedigree Function:")
label8.grid(row=7)
entry8=Entry(root,textvariable=e8)
entry8.grid(row=7,column=1)


label9=Label(root,text="Age:")
label9.grid(row=8)
entry9=Entry(root,textvariable=e9)
entry9.grid(row=8,column=1)


def onclick(e2,e3,e4,e5,e6,e7,e8,e9):
    p1=e2.get()
    values[0][0]=int(p1)
    p2=e3.get()
    values[0][1]=int(p2)
    p3=e4.get()
    values[0][2]=int(p3)
    p4=e5.get()
    values[0][3]=int(p4)
    p5=e6.get()
    values[0][4]=int(p5)
    p6=e7.get()
    values[0][5]=int(p6)
    p7=e8.get()
    values[0][6]=int(p7)
    p8=e9.get()
    values[0][7]=int(p8)
    print(p1+p2)
    print(values[0][6]+values[0][6])
    print(p2)
    print(p3)
    print(p4)
    return
    
onclick = partial(onclick,e2,e3,e4,e5,e6,e7,e8,e9)
button = Button(root,text="SUBMIT",command=onclick)
button.grid(row=9,column=1)
root.mainloop()