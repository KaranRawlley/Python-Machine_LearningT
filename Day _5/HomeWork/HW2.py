from tkinter import *
window = Tk()

def grams():
    print(val.get())
    grams=float(val.get())*1000
    t1.insert(END,grams)
    
def pounds():
    print(val.get())
    pounds=float(val.get())*2.20462
    t2.insert(END,pounds)

def ounces():
    print(val.get())
    ounce=float(val.get())*35.274
    t3.insert(END,ounce)
    
def kg():
    grams()
    pounds()
    ounces()            


g=Label(window,text='KG')
g.grid(row=0,column=1)

val=StringVar()

v=Entry(window,textvariable=val)
v.grid(row=0,column=2)


b1=Button(window,text='Convert',command=kg)
b1.grid(row=0,column=3,pady=10)
#b1.pack()


t1=Text(window,height=1,width=20)
t1.grid(row=2,column=1)

t2=Text(window,height=1,width=20)
t2.grid(row=2,column=2)

t3=Text(window,height=1,width=20)
t3.grid(row=2,column=3)



window.mainloop()