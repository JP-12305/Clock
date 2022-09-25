from tkinter import *

from time import strftime

root=Tk()
root.title("Clock")
root.geometry('1280x720')

global z


def on():
    global z
    z=('%I:%M:%S %p') 
    x()
    

def off():
    global z
    z=" "

def twentyfour():
    global z
    z = ('%H:%M:%S %p')    
    x()

def twelve():
    global z
    z= ('%I:%M:%S %p')
    x()

def x():
    global z
    string=strftime(z)
    a.config(text=string)
    a.after(1000,x)
    
    

n=Button(root,text="12",width=8,height=1,font=('BATMANFOREVERALTERNATE',40),fg="WHITE",bg="black",command=lambda : twelve()).place(x=250,y=270)

m=Button(root,text="24",width=8,height=1,font=('BATMANFOREVERALTERNATE',40),fg="WHITE",bg="black",command=lambda : twentyfour()).place(x=650,y=270)

o=Button(root,text="ON",width=17,height=1,font=('BATMANFOREVERALTERNATE',40),fg="WHITE",bg="black",command=lambda : on()).place(x=260,y=400)

p=Button(root,text="OFF",width=17,height=1,font=('BATMANFOREVERALTERNATE',40),fg="WHITE",bg="black",command=lambda : off()).place(x=260,y=500)


    

title=Label(root,text=("CLOCK"),font=("MONSTER BITES",80),width=70)
title.pack()

a= Label (root,font=("DS-DIGITAL",65),foreground="CYAN",bg="black",width=100,height=1)
a.pack()
on()



mainloop()


