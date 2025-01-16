import random as r 
zoznam_cisel = []
hladane_cisla = [0] *6
mensie_4 = []
for i in range (30):
    r_cisla= r.randint(0,9)
    zoznam_cisel.append(r_cisla)
    if r_cisla <= 4 :
        hladane_cisla[r_cisla] +=1
    if r_cisla > 4 :
        mensie_4.append(r_cisla)


for i in range(5):
    print(f"Počet výskytu číslice {i} je {hladane_cisla[i]}x")
    perc_vyskyt = round((hladane_cisla[i]/30) * 100,2),
    print(f"Perentuálny výskyt čísla {i} je {perc_vyskyt}%.")

print("Nový zoznam obsahuje prvky: ",mensie_4)
