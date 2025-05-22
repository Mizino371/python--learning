# rodne cislo vstup - rodne cyslo , vystup - rok narodenia + pohlavie

vstup = input("Zadaj rodné číslo bez lomítka: ")
desatrocie = int(vstup[0:2])
mesiac = int(vstup[2:4])
den = int(vstup[4:6])

pohlavie = "Muž"
if mesiac > 12:
    pohlavie = "Žena"
    mesiac-= 50


if desatrocie < 25:
    rok = 2000 + desatrocie
else:
    rok = 1900 + desatrocie

print(f"Pohlavie: {pohlavie}")
print(f"Datum narodenia: {den}.{mesiac}.{rok}")