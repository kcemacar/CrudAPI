from tkinter import *
import tkinter.messagebox as MessageBox
from crud import *

def interface():
    root = Tk()
    root.geometry("600x300")
    root.title("Pytkmysql")

    def insert():
        id = id_entry.get()
        name = name_entry.get()
        surname = surname_entry.get()

        if (id == "" or name == "" or surname ==""):
            MessageBox.showinfo("Insert Status","All attributes are required ! ")
        else :
            try:
                crud_insert(id,name,surname)
                MessageBox.showinfo("Database", "OK !!! ")
            except:
                MessageBox.showinfo("Database", "ERROR !!! ")

    def update():
        id = id_entry.get()
        name = name_entry.get()
        surname = surname_entry.get()

        if (id == "" or name == "" or surname ==""):
            MessageBox.showinfo("Update Status","All attributes are required ! ")
        else :
            try:
                crud_update(id,name,surname)
                MessageBox.showinfo("Database", "OK !!! ")
            except:
                MessageBox.showinfo("Database", "ERROR !!! ")



    id = Label(root, text = 'Enter ID : ', font = ('bold',15))
    id.place(x=20,y=30)

    id_entry = Entry()
    id_entry.place(x=120,y=35)

    name = Label(root, text = 'Name : ', font = ('bold',15))
    name.place(x=20,y=70)

    name_entry = Entry()
    name_entry.place(x=120,y=75)

    surname = Label(root, text = 'Surname : ', font = ('bold',15))
    surname.place(x=20,y=110)

    surname_entry = Entry()
    surname_entry.place(x=120,y=115)

    insert = Button(root, text= "insert", font = ("italic",10), bg = "white",command=insert).place(x = 20, y = 150)
    delete = Button(root, text="delete", font=("italic", 10), bg="white").place(x=120, y=150)
    update = Button(root, text="update", font=("italic", 10), bg="white",command=update).place(x=20, y=200)
    get = Button(root, text="get", font=("italic", 10), bg="white").place(x=120, y=200)

    root.mainloop()
