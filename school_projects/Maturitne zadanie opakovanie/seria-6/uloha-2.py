
#Vytvorte program, ktorý otestuje, či zadaný reťazec je bezpečným heslom, •	má minimálne 8 znakov,•	začína písmenom,•	obsahuje aspoň jeden špeciálny znak (*,  $, @, #),•	obsahuje aspoň jednu číslicu.
# Ak je heslo bezpečné, vypíšte „Heslo je bezpečné“, inak vypíšte „Heslo nie je bezpečné“.
heslo = input("Zadaj heslo: ")
heslo = heslo.strip()
specialne_znaky = ["*", "$", "@", "#"]
cislo = False
pismeno = False
dlzka = False
specialny_znak = False
if len(heslo) >= 8:
    dlzka = True
    if "a "<=heslo[0] <= "z" or "A"<=heslo[0] <= "Z":
        pismeno = True
    for znak in heslo:
        if znak in specialne_znaky:
            specialny_znak = True
        if "0" <= znak <= "9":
            cislo = True
if dlzka and pismeno and specialny_znak and cislo:
    print("Heslo je bezpečné")
else:
    print("Heslo nie je bezpečné")

