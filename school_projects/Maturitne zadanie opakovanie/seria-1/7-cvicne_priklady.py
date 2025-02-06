import random as r 

spravne = 0 
for i in range(5): #vytvorenie príkladu
    scitanec1 = r.randint(101,999)
    scitanec2 = r.randint(101,999)
    spravny_vysledok= scitanec1 + scitanec2
    
    vstup = input(f"{scitanec1} + {scitanec2} = ")
    if spravny_vysledok == int(vstup): #následná kontrola výsledku a zrátanie správnych odpovedí 
        spravne +=1
if spravne == 5:
    print("Všetko správne - 1")
elif spravne == 4 :
    print("takmer všetko správne - 2")
elif spravne == 3: 
    print("Musíš sa ešte posnažiť - 3")
elif spravne == 2:
    print("Musíš na sebe ešte zapracovať ale mohlo byť aj horšie - 4 ")
else:
    print("Máš čo robiť - 5")