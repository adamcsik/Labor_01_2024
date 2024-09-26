def adatok_bekerese():
    jel = input("Adja meg a műveleti jelet (+,-,/,*): ")
    while jel not in ("+", "-", "*", "/"):
        print("Nem megfelelő a műveleti jel!\nKérek másikat!")
        jel = input("Adja meg a műveleti jelet (+,-,/,*): ")

    szam1 = input("Adja meg az első számot: ")
    while not szam1.isnumeric():
        print("Nem számot adtál meg!")
        szam1 = input("Adja meg az első számot: ")
    szam1 = int(szam1)

    szam2 = input("Adja meg az első számot: ")
    while not szam2.isnumeric():
        print("Nem számot adtál meg!")
        szam2 = input("Adja meg az első számot: ")
    szam2 = int(szam2)

    return jel, szam1, szam2


def muveletek_vegregajtasa(jel, szam1, szam2):
    muvelet = 0
    if jel == "+":
        muvelet = szam1 + szam2
    elif jel == "-":
        muvelet = szam1 - szam2
    elif jel == "*":
        muvelet = szam1 * szam2
    elif jel == "/":
        muvelet = szam1 / szam2
    return muvelet


def eredmenyek_megjelenitese(jel, szam1, szam2, muvelet_eredmenye):
    print("A művelet végrehajtása: ")
    print(str(szam1).rjust(30))
    print(str(szam2).rjust(30))
    print(jel.ljust(30, "_"))
    print(str(muvelet_eredmenye).rjust(30))