# from tkinter import *
# 
# root = Tk()
# 
# def pm(event):
#     print('message')
#     
# def q():
#     root.quit() 
#     print('Quit')   
# 
# 
# printb = Button(root,text='Print Message')
# printb.pack(side=LEFT)
# printb.bind('<Button-3>',pm)
# quitb = Button(root,text='Quit',command=q)
# quitb.pack(side=LEFT)
# 
# 
# 
# 
# root.mainloop()
 
# import tkinter as tk
# root = tk.Tk()
# logo = tk.PhotoImage(file='photoblogbg.')
# w1 = tk.Label(root,image=logo).pack(side='right')
# explanation = """ When I'll be older
# I will be stronger
# They'll call me freedom
# Just like a wavein flag """
# 
# w2 = tk.Label(root,justify = tk.LEFT,padx=10,text=explanation).pack(side='left')
# root.mainloop()
        
from tkinter import *

def doN():
    print('ok')

root = Tk()

menu = Menu(root) 
root.config(menu=menu)
submenu=Menu(menu)
menu.add_cascade(label='File',menu=submenu)
submenu.add_command(label='New Project',command=doN)
submenu.add_command(label='New ...',command=doN)
submenu.add_separator()
submenu.add_command(label='Exit',command=doN)

editMenu=Menu(menu)

menu.add_cascade(label='Edit',menu=editMenu)
submenu.add_command(label='Redo',command=doN)

root.mainloop()
       
    