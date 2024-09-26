import Labor_04_modul

from Labor_04_modul import adatok_bekerese, muveletek_vegregajtasa, eredmenyek_megjelenitese

adatok = adatok_bekerese()
eredmeny = muveletek_vegregajtasa(adatok[0], adatok[1], adatok[2])
eredmenyek_megjelenitese(adatok[0], adatok[1], adatok[2], eredmeny)




