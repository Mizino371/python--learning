import math

usečka_ax = int(input("zadaj suradnice bodu Ax: "))
usečka_ay = int(input("zadaj suradnice bodu Ay: "))

usečka_bx = int(input("zadaj suradnice bodu Bx: "))
usečka_by = int(input("zadaj suradnice bodu By: "))


vzialenosť_bodov_AB = (math.sqrt ( (usečka_ax-usečka_bx)**2 + (usečka_ay-usečka_by)**2 ) )

print(f"vzdialenosť dvoch bodov je: {round(vzialenosť_bodov_AB,2)}")