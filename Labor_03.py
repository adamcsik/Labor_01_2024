""" nettó jövedelemszámítás bruttóból
print("Jövedelmszámítás\n")
brutto = int(input("Mennyi a bruttó jövelme:"))
kor = int(input("Hány éves vagy: "))

if kor < 25:
    if brutto > 599790:
        szja = (brutto - 599790) * 0.15
    else:
        szja = 0
else:
    szja = brutto * 0.15
nyugdij = brutto * 0.1
tb = brutto * 0.07
munkanelkuli = brutto * 0.015
netto = brutto - szja - nyugdij - tb - munkanelkuli

print("Jövedelem".center(50))
print("")
print("Bruttó jövedelem:".ljust(25, "_"), str(int(brutto)).rjust(25, "_"), " Ft", sep="")
print("SZJA:".ljust(25, "_"), str(int(szja)).rjust(25, "_"), " Ft", sep="")
print("Nyugdíj:".ljust(25, "_"), str(int(nyugdij)).rjust(25, "_"), " Ft", sep="")
print("TB járulék:".ljust(25, "_"), str(int(tb)).rjust(25, "_"), " Ft", sep="")
print("Munkanélküli:".ljust(25, "_"), str(int(munkanelkuli)).rjust(25, "_"), " Ft", sep="")
print("Nettó jövedelem:".ljust(25, "_"), str(int(netto)).rjust(25, "_"), " Ft", sep="")
"""
# Számológép
muvelet = 0
jel = input("Adja meg a műveleti jelet: ")
if jel not in ("+", "-", "*", "/"):
    print("Nem megfelelő input")
    exit()
else:
    szam1 = int(input("Addja meg az első számot: "))
    szam2 = int(input("Addja meg a második számot: "))
    if jel == "+":
        muvelet = szam1 + szam2
    elif jel == "-":
        muvelet = szam1 - szam2
    elif jel == "*":
        muvelet = szam1 * szam2
    elif jel == "/":
        muvelet = szam1 / szam2

    print("A művelet: ", szam1, jel, szam2, "=", muvelet)
