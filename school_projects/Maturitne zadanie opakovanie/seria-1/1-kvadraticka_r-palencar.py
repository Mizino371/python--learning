import math
vstup = input("Zadaj koeficietny kvadratickej rovnice\n(a b c): ")
vstup = list(map(int, vstup.strip().split(" "))) # premena stringu na int v liste

D = (vstup[1]**2) - (4*vstup[0]*vstup[2]) # vyjadrenie diskriminantu

if D > 0:
    vysledok1 = (-vstup[1] + math.sqrt(D))/(2*vstup[0]) #riešenie obidvoch rovníc
    vysledok2 = (-vstup[1] - math.sqrt(D))/(2*vstup[0])
    print(f"Rovnica má dva riešenia: {round(vysledok1,2)} {round(vysledok2)}")
elif D == 0: # jedno riešenie kedy diskriminant musí byť 0
    vysledok = (-vstup[1])/(2*vstup[0])
    print(f"Rovnica má jeden koreň: {round(vysledok,2)}")
else:
    print("Rovnica nemá reálne riešenie.")
