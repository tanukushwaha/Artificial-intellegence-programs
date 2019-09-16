
from tkinter import *
top=Tk()
top.title("My first Gui")
def helloCallBack():
    l=Label(top,text="FILL YOUR INFORMATION",font=("times",25,"bold italic"))
    m=Message(top,text="Enter your full name:")
    E=Entry(top)
    m1=Message(top,text="Select your Area of interest: ")
    f=Checkbutton(top,text="Singing",bg="yellow")
    s=Checkbutton(top,text="Arts",bg="yellow")
    t=Checkbutton(top,text="Dancing",bg="yellow")
    m2=Message(top,text="Select your class: ")
    r=Radiobutton(top,text="FYBSCIT",variable="v",value="FYBSCIT")
    r1=Radiobutton(top,text="SYBSCIT",variable="v",value="SYBSCIT")
    r2=Radiobutton(top,text="TYBSCIT",variable="v",value="TYBSCIT")
    m3=Message(top,text="Select on scale")
    s1=Scale(top)
    l.pack()
    m.pack()
    E.pack()
    m1.pack()
    f.pack()
    s.pack()    
    t.pack()
    m2.pack()
    r.pack()
    r1.pack()
    r2.pack()
    m3.pack()
    s1.pack(anchor=CENTER)
    
    
    
B=Button(top,text="CLICK HERE",bg="red",relief="raised",command=helloCallBack)
B.pack()

top.mainloop()
