from cProfile import label
from tkinter import *
from tkinter import messagebox

def beleptetes():
    def ok_bevitel():
        be_ablak.destroy()

    def reg_kerese():
        be_ablak.destroy()
        regisztracio()

    be_ablak = Tk()
    be_ablak.title("Beléptetés")

    f_nev_cimke = Label(be_ablak, text="A felhasználó neve (email):")
    f_jelszo_cimke = Label(be_ablak, text="Jelszó:")
    f_nev = StringVar()
    f_nev.set("")
    f_nev_be = Entry(be_ablak, textvariable=f_nev, width=20)
    f_jelszo =StringVar()
    f_jelszo.set("")
    f_jelszo_be = Entry(be_ablak, textvariable=f_jelszo, width=20)

    ok_gomb = Button(be_ablak, text="OK", command=ok_bevitel, width=10)
    reg_gomb = Button(be_ablak, text="Regisztráció", command=reg_kerese)

    f_nev_cimke.grid(row=0, column=0, sticky="E", padx=15, pady=5)
    f_nev_be.grid(row=0, column=1)
    f_jelszo_cimke.grid(row=1, column=0, sticky="E", padx=15, pady=5)
    f_jelszo_be.grid(row=1, column=1)
    reg_gomb.grid(row=3  , column=2, padx=15, pady=5)
    ok_gomb.grid(row=3, column=0, pady=5)

    be_ablak.mainloop()

def regisztracio():

    def ok_bevitel():
        reg_ablak.destroy()

    def jelszo_gen():
        pass

    reg_ablak = Tk()
    reg_ablak.title("Regisztráció")
    #reg_ablak.geometry("400x200")

    f_nev_cimke = Label(reg_ablak, text="A felhasználó neve (email):")
    f_jelszo_cimke = Label(reg_ablak, text="Jelszó:")
    f_jelszo2_cimke = Label(reg_ablak, text="Jelszó ismét:")

    ok_gomb = Button(reg_ablak, text="OK", command=ok_bevitel, width=10)
    jelszo_gen_gomb = Button(reg_ablak, text="Jelszó generálása", command=jelszo_gen)

    f_nev = StringVar()
    f_nev.set("")
    f_nev_be = Entry(reg_ablak, textvariable=f_nev, width=20)
    f_jelszo =StringVar()
    f_jelszo.set("")
    f_jelszo_be = Entry(reg_ablak, textvariable=f_jelszo, width=20)
    f_jelszo2 = StringVar()
    f_jelszo2.set("")
    f_jelszo2_be = Entry(reg_ablak, textvariable=f_jelszo2, width=20)

    f_nev_cimke.grid(row=0, column=0, sticky="E", padx=15, pady=5)
    f_nev_be.grid(row=0, column=1)
    f_jelszo_cimke.grid(row=1, column=0, sticky="E", padx=15, pady=5)
    f_jelszo_be.grid(row=1, column=1)
    f_jelszo2_cimke.grid(row=2, column=0, sticky="E", padx=15, pady=5)
    f_jelszo2_be.grid(row=2, column=1)
    jelszo_gen_gomb.grid(row=1  , column=3, padx=15, pady=5)
    ok_gomb.grid(row=3, column=1, pady=5)

    reg_ablak.mainloop()

def nevjegy():
    messagebox.showinfo("Készítő", "Készítette: Én, 2024")

def sugo():
    messagebox.showerror("súgó", "Még nem készült el a súgó!")

# főprogram
app = Tk()
app.title("Dolgozói nyilvántartás")
app.geometry("600x400")
menulista = Menu(app)

hozzaferes = Menu(menulista)
hozzaferes.add_command(label="Beléptetés", command=beleptetes)
hozzaferes.add_command(label="Regisztráció", command=regisztracio)
hozzaferes.add_command(label="Kilépés", command=app.destroy)
menulista.add_cascade(label="Fájl", menu=hozzaferes)

egyeb = Menu(menulista)
egyeb.add_command(label="Névjegy", command=nevjegy)
egyeb.add_command(label="Súgó", command=sugo)
menulista.add_cascade(label="Egyéb", menu=egyeb)

app.config(menu=menulista)
app.mainloop()