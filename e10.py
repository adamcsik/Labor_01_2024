from tkinter import *
from tkinter import messagebox

def sugo():
    def sugouzenet():
        messagebox.showinfo("Súgó", "A súgó az interneten van!", parent=ablak)


    ablak = Toplevel(app)
    sugomenu = Menu()
    sugomenu.add_command(label="Súgóüzenet", command=sugouzenet)
    sugomenu.add_command(label="Bezárás", command=ablak.destroy)
    ablak.config(menu=sugomenu)

    ablak.lift()
    ablak.focus_force()
    ablak.mainloop()

app =Tk()
app.title("Menüprogram")
#app.geometry("600x400+350+250")
app.configure(bg="lightblue")
#app.attributes("-fullscreen", True)
#app.minsize(600, 400)
#app.maxsize(700,500)
app.resizable(False, False)

menu = Menu()
menu.add_command(label="Kilépés", command=app.destroy)
menu.add_command(label="Súgó", command=sugo)
app.config(menu=menu)

app.mainloop()