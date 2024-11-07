import random as r

def nahodne_cisla():
    subor = open("24-11-04/uloha-1/nahodne_cisla.txt","w")
    n_riadkov = r.randint(1,99)
    for i in range(n_riadkov):
        r_int = r.randint(1,99)
        subor.write(str(r_int)+"\n")
    subor.close()


nahodne_cisla()
subor = open("24-11-04/uloha-1/nahodne_cisla.txt","r")
počet_riadkov = 0
n_sucet_cisel = 0
for riadok in subor:
    počet_riadkov += 1 
    n_sucet_cisel += int(riadok)
    
print(f"Súčet čísel riadkov: {n_sucet_cisel}")
print(f"Počet riadkov: {počet_riadkov}")
subor.close()
