#generuj nahodne cislo < 100, vypiš či sa jedná o prvočíslo alebo o zložené čislo, ak zložené, vypíš jeho delitele
import random
r_cislo = random.randint(1, 100)
delitele = []
print(r_cislo)
if r_cislo == 1:
    print("1 nie je prvočíslo ani zložené číslo")
Prvocislo = True
for i in range(2,r_cislo):
    if r_cislo % i ==0:
        delitele.append(i)
    else:
        continue
if len(delitele) == 0:
    print(f"{r_cislo} je prvočíslo")
print(delitele)