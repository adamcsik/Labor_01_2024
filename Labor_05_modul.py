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
