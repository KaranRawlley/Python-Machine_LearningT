from tkinter import *

window=Tk()

def km():
    print(e1_value.get())
    miles=float(e1_value.get())*0.6
    t1.insert(END,miles)
    
b1=Button(window,text='Calculate',command=km)
#b1.pack()
b1.grid(row=0,column=0)

e1_value=StringVar()

e1=Entry(window,textvariable=e1_value)
e1.grid(row=0,column=1)

t1=Text(window,height=1,width=20)
t1.grid(row=0,column=3)
window.mainloop()