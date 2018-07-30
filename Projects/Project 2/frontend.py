from tkinter import *
from backend2 import *





def get_selected_row(event):   
    try:
        
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        print(selected_tuple[0])

        
        title.delete(0,END)
        title.insert(END,selected_tuple[1])
        author.delete(0, END)
        author.insert(END,selected_tuple[2])
        year.delete(0, END)
        year.insert(END,selected_tuple[3])
        isbn.delete(0, END)
        isbn.insert(END,selected_tuple[4])
    except IndexError:
        pass                

def view_command():
    list1.delete(0, END)  
    for row in view():
        list1.insert(END, row)

def search_command():
    list1.delete(0, END)
    for row in search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get()):
        list1.insert(END, row)

def add_command():
    insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    list1.delete(0, END)
    list1.insert(END, (title_text.get(), author_text.get(),year_text.get(),isbn_text.get()))

def delete_command():
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    delete(selected_tuple[0])
    view_command()

def update_command():
    
    index = list1.curselection()[0]
    selected_tuple = list1.get(index)
    update(selected_tuple[0],title_text.get(),author_text.get(),year_text.get(), isbn_text.get())
    view_command()
    
prints()    

root = Tk()
root.configure(bg='#e3cf57',bd=10)


root.title('BookStore')
titlel = Label(root,text='Title :',bg='#e3cf57')

titlel.grid(row=0,column=0)
title_text = StringVar()
title = Entry(root,width = 20,bd=4,textvariable=title_text,bg='#d1eeee')
title.grid(row=0,column=1)


authorl = Label(root,text='Author :',bg='#e3cf57')
authorl.grid(row=0,column=2)
author_text = StringVar()
author = Entry(root,width = 20,bd=4,textvariable=author_text,bg='#d1eeee')
author.grid(row=0,column=3,padx=4)


yearl = Label(root,text='Year :',bg='#e3cf57')
yearl.grid(row=1,column=0)
year_text = StringVar()
year = Entry(root,width = 20,bd=4,textvariable=year_text,bg='#d1eeee')

year.grid(row=1,column=1,pady=4)


isbnl = Label(root,text='ISBN  :',bg='#e3cf57')
isbnl.grid(row=1,column=2)
isbn_text = StringVar()
isbn = Entry(root,width = 20,bd=4,textvariable=isbn_text,bg='#d1eeee')
isbn.grid(row=1,column=3,pady=4)

list1 = Listbox(root, height=6, width=35,bd=5,bg='#76ee00')
list1.grid(row=2, column=0, rowspan=6, columnspan=2)
list1.bind('<<ListboxSelect>>',get_selected_row)

sb1 = Scrollbar(root)
sb1.grid(row=2, column=2, rowspan=6)
sb1 = Scrollbar(root)
sb1.grid(row=2, column=2, rowspan=6)
list1.config(yscrollcommand=sb1.set)
sb1.config(command=list1.yview)



b1 = Button(root, text="View all", width=12,pady=4,command=view_command,bd=6,bg='#CD8500')
b1.grid(row=2, column=3)

b2 = Button(root,bd=6, text="Search entry", width=12,pady=4,command=search_command,bg='#CD8500')
b2.grid(row=3, column=3)

b3 = Button(root,bd=6, text="Add entry", width=12,pady=4,command=add_command,bg='#CD8500')
b3.grid(row=4, column=3)

b4 = Button(root,bd=6, text="Update selected", width=12,pady=4,command=update_command,bg='#CD8500')
b4.grid(row=5, column=3)

b5 = Button(root,bd=6, text="Delete selected", width=12,pady=4,command=delete_command,bg='#CD8500')
b5.grid(row=6, column=3)
b6 = Button(root,bd=6, text="Close", width=12,pady=4,command=root.destroy,bg='#CD8500')
b6.grid(row=7, column=3)




root.mainloop()


