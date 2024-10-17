class Jelszo:
    felhasznalo_jelszava = "nincs"

    def jelszo_bekerese(self):
        pass

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


# főprogram
felh_jelszo = Jelszo()
print(felh_jelszo.felhasznalo_jelszava)
felh_jelszo.jelszo_generalasa()
print(felh_jelszo.felhasznalo_jelszava)
