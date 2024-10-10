def felhasznalonev():
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
    return _felhasznalo_neve


def jelszo_ellenorzese(jelszo):
    ok = True
    probalkozasok_szama = 0
    while True:
        jelszo2 = input("Kérem ismét a jelszót: ")
        if jelszo == jelszo2:
            break
        else:
            probalkozasok_szama += 1
            if probalkozasok_szama == 3:
                ok = False
                break
            print("Nem azonos a két jelszó! Próbálja ismét!")
    return ok


def regisztracio():
    def jelszo_bekerese(hossz):
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
        return jelszo

    def rogzites(email, jelszo):
        with open('dolgozok.txt', 'a', encoding='utf-8') as fajl:
            fajl.write(email + ";" + jelszo + "\n")

    felhasznalo_neve = felhasznalonev()
    felhasznalo_jelszava = jelszo_bekerese(8)
    ok = jelszo_ellenorzese(felhasznalo_jelszava)
    if ok:
        rogzites(felhasznalo_neve, felhasznalo_jelszava)
    return ok


def beleptetes():
    def felhasznalo_bekerese():
        jelszo = False
        email = felhasznalonev()
        with open('dolgozok.txt', 'r', encoding='utf-8') as falj:
            for sor in falj:
                felhasznalo = sor.strip().split(";")
                if felhasznalo[0] == email:
                    jelszo = felhasznalo[1]
                    break
        return jelszo

    felhasznalo = felhasznalo_bekerese()
    if not felhasznalo:
        print("Nincs ilyen felhasználó!")
    else:
        if jelszo_ellenorzese(felhasznalo):
            print("sikerült belépned")
        else:
            print("Belépés megtagadva!")
