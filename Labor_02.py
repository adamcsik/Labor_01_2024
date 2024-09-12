''' Ez az első laborfoglalkozás
    2024.09.12.
    lapbor feladatai'''

print("Szia DUE!", end='')  # megjelenítés

print("\tSzia", "DUE!")

print("Szia", "DUE!", sep="-")

print("Szia", "\n\tDUE!")

print('''Szép napunk
lesz ma!
''')

felhasznalo_neve = "Józsi"
felhasznalo_kora = 21

print("Szia", felhasznalo_neve)
print(f"Szia {felhasznalo_neve}")

print("Neve: {0} \nKora: {1}".format(felhasznalo_neve, felhasznalo_kora))

print(felhasznalo_neve.rjust(30, "."))
print(str(felhasznalo_kora).rjust(30, "."))

print(felhasznalo_neve.ljust(30, "."))
print(str(felhasznalo_kora).ljust(30, "."))

print(felhasznalo_neve.center(30, "."))
print(str(felhasznalo_kora).center(30, "."))

felhasznalo_neve = input("\nKérem a nevedet: ")
felhasznalo_kora = input("Hány éves vagy: ")
print("\nSzia", felhasznalo_neve)
print("Biztosan", felhasznalo_kora, "éves vagy? Nem ", int(felhasznalo_kora) + 10)
