class Jelszo:
    felhasznalo_jelszava = "NincsJelszo"

    """def __init__(self, felhasznalo_jelszava = "van"):
        self.felhasznalo_jelszava = felhasznalo_jelszava
       """

    def jelszo_bekerese(self, hossz):
        def jelszo_hossza(_jelszo, _hossz):
            ok = True
            if len(_jelszo) < _hossz:
                ok = False
            return ok

        def szamjegy(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.isnumeric():
                    ok = True
                    break
            return ok

        def kisbetu(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.islower():
                    ok = True
                    break
            return ok

        def nagybetu(_jelszo):
            ok = False
            for betu in _jelszo:
                if betu.isupper():
                    ok = True
                    break
            return ok

        jelszo = input("Kérek egy jelszót: ")
        while not jelszo_hossza(jelszo, hossz) or not szamjegy(jelszo) or not kisbetu(jelszo) or not nagybetu(jelszo):
            print("Rossz a jelszó!")
            jelszo = input("Kérek egy jelszót: ")
        self.felhasznalo_jelszava = jelszo

    def jelszo_generalasa(self, hossz=8, kisbetu=True, nagybetu=True, szam=True):
        import string
        import random
        jelszo = ""
        karaktersor = ""
        if kisbetu:
            karaktersor = string.ascii_lowercase
        if nagybetu:
            karaktersor = karaktersor + string.ascii_uppercase
        if szam:
            karaktersor = karaktersor + string.digits
        for _ in range(hossz):
            jelszo = jelszo + karaktersor[random.randint(0, len(karaktersor)-1)]
        self.felhasznalo_jelszava = jelszo

    def jelszo_ellenorzese(self):
        ok = True
        probalkozasok_szama = 0
        while True:
            jelszo2 = input("Kérem ismét a jelszót: ")
            if self.felhasznalo_jelszava == jelszo2:
                break
            else:
                probalkozasok_szama += 1
                if probalkozasok_szama == 3:
                    ok = False
                    break
                print("Nem azonos a két jelszó! Próbálja ismét!")
        return ok

class Felhasznalo(Jelszo):
    felhasznalo_neve ="Valaki"

    """def __init__(self, felhasznalo_jelszo,  felhasznalo_neve = "Senki"):
        self.felhasznalo_neve = felhasznalo_neve
        super().__init__(felhasznalo_jelszo)
    """
    def __init__(self):
        super().__init__()

    def felhasznalonev(self):
        _felhasznalo_neve = input("Kérem a felhasználói nevét (egy email): ")
        while " " in _felhasznalo_neve or not "@" in _felhasznalo_neve or not "." in _felhasznalo_neve:
            print("Érvénytelen email formátum!")
            if " " in _felhasznalo_neve:
                print("Szóköz van az emailben!")
            if "@" not in _felhasznalo_neve:
                print("Hiányzik a @ jel!")
            if "." not in _felhasznalo_neve:
                print("Hiányzik a . jel!")
            _felhasznalo_neve = input("Kérem a felhasználói nevét (egy email): ")
        self.felhasznalo_neve  = _felhasznalo_neve

    def rogzites(self):
        with open('dolgozok.txt', 'a', encoding='utf-8') as fajl:
            fajl.write(self.felhasznalo_neve + ";" + self.felhasznalo_jelszava + "\n")

    def tarolas(self):
        import sqlite3
        kapcsolat = sqlite3.connect("dolgozok.db")
        ab = kapcsolat.cursor()
        ab.execute('CREATE TABLE IF NOT EXISTS dolgozok(nev TEXT, jelszo TEXT)')
        nev = self.felhasznalo_neve
        jelszo = self.felhasznalo_jelszava
        ab.execute('INSERT INTO dolgozok (nev, jelszo) VALUES (?, ?)', (nev, jelszo))
        kapcsolat.commit()
        kapcsolat.close()


# főprogram
dolgozo = Felhasznalo()
print(dolgozo.felhasznalo_neve)
print(dolgozo.felhasznalo_jelszava)
dolgozo.felhasznalonev()
dolgozo.jelszo_generalasa()
print(dolgozo.felhasznalo_neve)
print(dolgozo.felhasznalo_jelszava)
dolgozo.tarolas()
