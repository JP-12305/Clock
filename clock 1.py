
from ast import Assign
from tkinter import *

from time import strftime



root=Tk()
root.title("Clock")
root.geometry('1280x720')

global string

def on():
    string = strftime('%I:%M:%S %p') 
    a.config(text=string)
    

def off():
    a.config(text=' ')

def twentyfour():
    string = strftime('%H:%M:%S %p')    
    a.config(text=string)

def twelve():

    string= strftime('%I:%M:%S %p')
    a.config(text=string)


n=Button(root,text="12",width=10,height=1,font=('FAGRAK',40),fg="cyan",bg="black",command=lambda : twelve()).place(x=250,y=270)

m=Button(root,text="24",width=10,height=1,font=('FAGRAK',40),fg="cyan",bg="black",command=lambda : twentyfour()).place(x=700,y=270)

o=Button(root,text="ON",width=24,height=1,font=('FAGRAK',40),fg="cyan",bg="black",command=lambda : on()).place(x=260,y=400)

p=Button(root,text="OFF",width=24,height=1,font=('FAGRAK',40),fg="cyan",bg="black",command=lambda : off()).place(x=260,y=500)

def x():
    a.config(text=string)
    a.after(1000,x)
    

title=Label(root,text=("JP'S CLOCK"),font=("BATMANFOREVERALTERNATE",60),width=90)
title.pack()

a= Label (root,font=("FAGRAK",50),foreground="blue")
a.pack()



mainloop()

