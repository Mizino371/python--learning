
cestovne_per_person = float(input("Cena cestovného(desatinné číslo v tvare 0.5):  "))

subor = open("4.roč/24-11-04/uloha-2/prihlaseni.txt","r")
p_riadkov = 1
n_osob = 0
pocet_menej_15 = 0
cestovne_spolu = 0
scitanie_veku = 0
for riadok in subor:
    if p_riadkov % 2 != 0:
        n_osob += 1
    else:
        if int(riadok) <15:
            pocet_menej_15 +=1
            cestovne_spolu += (cestovne_per_person/2)
            
        else:
            cestovne_spolu += cestovne_per_person
        scitanie_veku += int(riadok)
    p_riadkov +=1   
priemer_veku =  scitanie_veku/n_osob

print(f"a) počet osôb: {n_osob}")
print(f"b) Počet osôb menej ako 15: {pocet_menej_15}")
print(f"c) Celková cena cestovného: {round(cestovne_spolu,2)}€")
print(f"d) Priemerný vek osôb je {round(priemer_veku,2)}")


