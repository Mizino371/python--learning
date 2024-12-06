import math
def vypočet_kv_rovnice():
    koef_a = float(input("zadaj koeficient a: "))
    koef_b = float(input("zadaj koeficient b: "))
    koef_c =float( input("zadaj koeficient c: "))

    kvadraticka = f"{(koef_a)}x^2 {(koef_b)}x {(koef_c)}"

    D = (koef_b**2) - (4*koef_a*koef_c)
    if D < 0:
        print("Nemá riešenie")
        
    elif D == 0:
        x = (-koef_b + math.sqrt(D))/ (2*koef_a)
        print(f"Rovnica {kvadraticka} má jeden koreň: x = {round(x,2)}")
        
    else:
        x1 = (-koef_b + math.sqrt(D))/ (2*koef_a)
        x2 = (-koef_b - math.sqrt(D))/ (2*koef_a)
        print(f"Rovnica {kvadraticka} má 2 korene: x1 = {round(x1,2)}; x2 = {round(x2,2)}")
        
    znova = input("Cheš zadať dalšiu kvadraticku rovnicu? a/n : ")
        
    if znova =="a":
        vypočet_kv_rovnice()

vypočet_kv_rovnice()


