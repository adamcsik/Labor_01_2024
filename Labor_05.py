from Labor_05_modul import *

def beleptetes():
    print("Beléptetés")


def regisztracio():
    print("Regisztráció")



def jelszo_ellenorzese():
    pass


# főprogram
# regisztracio()
# beleptetes()
felhasznalo_neve = felhasznalonev()
print(felhasznalo_neve)
felhasznalo_jelszava = jelszo_bekerese(8)
print(felhasznalo_jelszava)
