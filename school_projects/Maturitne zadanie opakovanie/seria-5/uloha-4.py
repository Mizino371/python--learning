zoz_pocasia = {}
preklady = {"JASNO":"JJ" ,"POLOOBLAČNO":"PO", "POLOJASNO":"PJ"  ,  "OBLAČNO": "OO", "POLOOBLACNO": "P0", "OBLACNO": "OO"}
# typ : počet dni , max teplota , min teplota
subor = open("/Users/m1promichalpalencar/Desktop/python--learning/school_projects/Maturitne zadanie opakovanie/seria-5/sliac.txt","r")
p = 0
for riadok in subor:
    riadok = riadok.strip().split(" ")
    if riadok[1] in zoz_pocasia:

        if zoz_pocasia[riadok[1]][1] < int(riadok[0]):
            zoz_pocasia[riadok[1]][1] = int(riadok[0])
        elif zoz_pocasia[riadok[1]][2] > int (riadok[0]):
            zoz_pocasia[riadok[1]][2] = int(riadok[0])
        else:
            pass
        zoz_pocasia[riadok[1]][0] += 1

    else:
        zoz_pocasia[riadok[1]] = [1,int(riadok[0]),int(riadok[0])]


print (zoz_pocasia)
vstup = input("Zadaj typ pocasia: \nJasno\nPolooblacno\npolojasno\noblacno\n: ")
pocet_dni = zoz_pocasia[preklady[vstup.upper()]][0]
max_tep = zoz_pocasia[preklady[vstup.upper()]][1]
min_tep = zoz_pocasia[preklady[vstup.upper()]][2]
print(f"Na Sliači bolo počasie {vstup} {pocet_dni}x, najvyššia teplota bola {max_tep}°C a najnižšia teplota bola {min_tep}°C.")