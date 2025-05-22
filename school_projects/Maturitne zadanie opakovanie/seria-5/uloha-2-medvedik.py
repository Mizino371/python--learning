import math
subor = open("/Users/m1promichalpalencar/Desktop/python--learning/school_projects/Maturitne zadanie opakovanie/seria-5/medved.txt", "r")

celkovo_presiel = 0
d_sledovanie = 0
for riadok in subor:
    riadok = riadok.strip().split(" ")
    p_x = int(riadok[0])
    p_y = int(riadok[1])
    celkovo_presiel +=math.sqrt(p_x**2 + p_y**2)
    d_sledovanie +=1

print(f"Medvedik presiel celkovo {round(celkovo_presiel,2)}km za {d_sledovanie} dni.")