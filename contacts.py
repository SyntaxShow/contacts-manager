from tkinter import *
from tkinter import messagebox
import db_contacts
bg='#1B1464'
bg_lst = '#31ff31'
win = Tk()
win.geometry('468x415')
win.title('Contacts')
win.config(bg=bg)
win.resizable(0,0)
db1 = db_contacts.Database('mydata.db')
#|||||||||||||||||||||||||||||||||functions||||||||||||||||||||||||||||||||||||
def insert():
    fname = ent_fname.get()
    lname = ent_lname.get()
    city = ent_city.get()
    phone = ent_phone.get()
    if fname =='' or len(lname)==0:
        messagebox.showerror('ERROR','Firstname or Lastname is empty!!!')
        return
    db1.insert(fname, lname, city, phone)
    clear()
    show()
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_city.delete(0,END)
    ent_phone.delete(0,END)
    ent_fname.focus_set()
def show():
    lst_info.delete(0,END)
    records = db1.select()
    for record in records:
        lst_info.insert(END, f'{record[0]},{record[1]},{record[2]},{record[3]},{record[4]}')
def delete():
    try:
        index = lst_info.curselection()
        data = lst_info.get(index)
        ask = messagebox.askquestion('Delete',f'do you want delete item [{data}]?')
        if ask.lower()=='yes':
            db1.delete(data[0])
        show()
    except Exception:
        messagebox.showwarning('Index Error','Select item in listbox!!!')
def select_item(event):
    global data
    index = lst_info.curselection()
    if index:
        info = lst_info.get(index)
        data = info.split(',')
        ent_fname.delete(0,END)
        ent_lname.delete(0,END)
        ent_city.delete(0,END)
        ent_phone.delete(0,END)
        ent_fname.insert(END, data[1])
        ent_lname.insert(END, data[2])
        ent_city.insert(END, data[3])
        ent_phone.insert(END, data[4])
def update():
    global data
    db1.update(data[0], ent_fname.get(), ent_lname.get(), ent_city.get(), ent_phone.get())
    show()
def search():
    info = ent_search.get()
    records = db1.search(info)
    if records:
        lst_info.delete(0,END)
        for record in records:
            lst_info.insert(END, f'{record[0]},{record[1]},{record[2]},{record[3]},{record[4]}')
        return
    else:
        messagebox.showerror('ERORR',f'Record {info} not found!!!')
        ent_search.delete(0,END)
        ent_search.focus_set()
def clear_search():
    ent_search.delete(0,END)
#|||||||||||||||||||||||||||||||||widgets||||||||||||||||||||||||||||||||||||||
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>lable<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lbl_fname = Label(win, text='Fname:', font='tahoma 12 bold',fg='white', bg=bg)
lbl_fname.place(x = 17, y=10)
lbl_lname = Label(win, text='Lname:', font='tahoma 12 bold',fg='white', bg=bg)
lbl_lname.place(x = 237, y=10)
lbl_city = Label(win, text='City:', font='tahoma 12 bold',fg='white', bg=bg)
lbl_city.place(x = 39, y=40)
lbl_tel = Label(win, text='Phone:', font='tahoma 12 bold',fg='white', bg=bg)
lbl_tel.place(x = 240, y=40)
lbl_search = Label(win, text='Search', font='tahoma 12 bold',fg='white', bg=bg)
lbl_search.place(x = 205, y=280)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>entry<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
ent_fname = Entry(win)
ent_fname.place(x = 80, y=15)
ent_lname = Entry(win)
ent_lname.place(x = 300, y=15)
ent_city = Entry(win)
ent_city.place(x = 80, y=45)
ent_phone = Entry(win)
ent_phone.place(x = 300, y=45)
ent_search = Entry(win, font='tahoma 10 bold')
ent_search.place(x = 153, y=260)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>listbox<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lst_info = Listbox(win, bg=bg_lst,width=57, height=11)
lst_info.place(x = 40, y=78)
lst_info.bind('<<ListboxSelect>>',select_item)
sb = Scrollbar(win)
sb.place(x=22, y=78, height=170)
sb.config(command=lst_info.yview)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>button<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
btn_insert = Button(win, text='insert', font='tahoma 12 bold', bg='#fbc000', width=10, command=insert)
btn_insert.place(x=60, y= 320)
btn_delete = Button(win, text='delete', font='tahoma 12 bold', bg='#fbc000', width=10, command=delete)
btn_delete.place(x=180, y= 320)
btn_update = Button(win, text='update', font='tahoma 12 bold', bg='#fbc000', width=10, command=update)
btn_update.place(x=300, y= 320)
btn_show = Button(win, text='show', font='tahoma 12 bold', bg='#fbc000', width=10, command=show)
btn_show.place(x=60, y= 360)
btn_clear = Button(win, text='clear', font='tahoma 12 bold', bg='#fbc000', width=10, command=clear)
btn_clear.place(x=180, y= 360)
btn_exit = Button(win, text='exit', font='tahoma 12 bold', bg='#fbc000', width=10, command=win.destroy)
btn_exit.place(x=300, y= 360)
btn_clear_search = Button(win, text='clear search', font='tahoma 8 bold', bg='white', width=10, command=clear_search)
btn_clear_search.place(x=60, y= 260)
btn_search = Button(win, text='search', font='tahoma 8 bold', fg='white', bg='green', width=10, command=search)
btn_search.place(x=330, y= 260)
win.mainloop()