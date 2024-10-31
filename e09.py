from tkinter import *
from tkinter import messagebox

def sugo():
    messagebox.showinfo("Súgó", "A súgó az interneten van!")

app =Tk()
app.title("Menüprogram")

menu = Menu()
menu.add_command(label="Kilépés", command=app.destroy)
menu.add_command(label="Súgó", command=sugo)
app.config(menu=menu)

app.mainloop()