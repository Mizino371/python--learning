# vstupny_datum = input("Dátum v tvare dd:mm:rrrr ")
# novy_datum = f"{vstupny_datum[6:10]}-{vstupny_datum[3:5]}-{vstupny_datum[:2]}"
# print(novy_datum)


# rodne cislo bez lomitka 7556037110 -- /11 = bez zvysku "OK"
# rodne cislo 
# muzi - 01 - 12
# ženy - 51 - 62

rodne_cislo = input("Zadaj rodne číslo bez lomitka: ")
if rodne_cislo[2] == "5" or  rodne_cislo[2] == "6":
    mesiac= int(rodne_cislo[2:4]) - 50
    pohlavie = "Žena"
else:
    pohlavie = "Muž"

if int(rodne_cislo[:2]) >24:
    tisic = 19
elif int(rodne_cislo[:2]) <24:
    tisic = 20

print(f"Dátum narodenia: {rodne_cislo[4:6]}.{mesiac}.{tisic}{rodne_cislo[:2]}")
print(f"Pohlavie: {pohlavie}")