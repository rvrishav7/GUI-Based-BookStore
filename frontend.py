from tkinter import *
import backend

def fun_view():
    l1.delete(0,END)
    data=backend.view()
    for rows in data:
        l1.insert(END,rows)

def fun_search():
    l1.delete(0,END)
    results=backend.search(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    for row in results:
        l1.insert(END,row)

def fun_add():
    backend.insert(title_text.get(),author_text.get(),year_text.get(),isbn_text.get())
    e1.delete(0,END)
    e2.delete(0,END)
    e3.delete(0,END)
    e4.delete(0,END)

def fun_select(entry):
    try:
        global get_data
        row=l1.curselection()
        get_data=l1.get(row)
        print(get_data)
        e1.delete(0,END)
        e1.insert(END,get_data[1])
        e2.delete(0,END)
        e2.insert(END,get_data[3])
        e3.delete(0,END)
        e3.insert(END,get_data[2])
        e4.delete(0,END)
        e4.insert(END,get_data[4])

    except:
        pass

def fun_update():

    title=title_text.get()
    author=author_text.get()
    year=year_text.get()
    isbn=isbn_text.get()
    backend.update(get_data[0],title,author,year,isbn)

def fun_delete():
     #print(get_data[0])
     backend.delete(get_data[0])
     fun_view()
def end():
    exit()
window=Tk()
window.wm_title('My BookStore')
lb1=Label(window,text='Title')
lb1.grid(row=0,column=0)

lb2=Label(window,text='Year')
lb2.grid(row=1,column=0)

lb3=Label(window,text='Author')
lb3.grid(row=0,column=2)

lb4=Label(window,text='ISBN')
lb4.grid(row=1,column=2)

title_text=StringVar()
e1=Entry(window,textvariable=title_text)
e1.grid(row=0,column=1)

year_text=StringVar()
e2=Entry(window,textvariable=year_text)
e2.grid(row=1,column=1)

author_text=StringVar()
e3=Entry(window,textvariable=author_text)
e3.grid(row=0,column=3)

isbn_text=StringVar()
e4=Entry(window,textvariable=isbn_text)
e4.grid(row=1,column=3)

b1= Button(text="View All",width=15,command=fun_view)
b1.grid(row=2,column=3)

b2= Button(text="Search Entry",width=15,command=fun_search)
b2.grid(row=3,column=3)

b3= Button(text="Add Entry",width=15,command=fun_add)
b3.grid(row=4,column=3)

b4= Button(text="Update Selected",width=15,command=fun_update)
b4.grid(row=5,column=3)

b5= Button(text="Delete Selected",width=15,command=fun_delete)
b5.grid(row=6,column=3)

b6= Button(text="Close",width=15,command=window.destroy)
b6.grid(row=7,column=3)

l1=Listbox(window,height=6,width=35)
l1.grid(row=2,column=0,rowspan=6,columnspan=2)

sb1=Scrollbar(window)
#sb2=Scrollbar(window)
sb1.grid(row=2,column=2,rowspan=6)
#sb2.grid(row=7,column=0,columnspan=2,padx=2)
l1.configure(yscrollcommand=sb1.set)
#l1.configure(xscrollcommand=sb2.set)
sb1.configure(command=l1.yview)
#sb2.configure(command=l1.xview)

l1.bind('<<ListboxSelect>>',fun_select)

window.mainloop()
