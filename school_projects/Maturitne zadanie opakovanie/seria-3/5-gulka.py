import tkinter
c = tkinter.Canvas(width=600, height=500)
c.pack()
x = 300
y = 50
pohybovanie = False  # Premenná na signalizáciu pohybu


def delete():
    c.delete("all")


def pohyb(smer):
    global y, pohybovanie
    if not pohybovanie:# Skontroluj, či má pohyb pokračovať
        return


    if smer == "dole" and y < 500:  # Pohyb nadol
        y += 10
    elif smer == "hore" and y > 0:  # Pohyb nahor
        y -= 10
    else:  # Ak dosiahneme hranicu, zmeníme smer
        if smer == "dole":
            smer = "hore"
        else:
            smer = "dole"

    c.delete("all")
    c.create_oval(x - 5, y - 5, x + 5, y + 5, fill="red")
    c.update()
    c.after(50, pohyb, smer)  # Znova zavoláme túto funkciu po 50 milisekundách


def akcia():
    global pohybovanie
    pohybovanie = True  # Spustenie pohybu
    pohyb("dole")  # Začni pohyb smerom nadol


def end():
    global pohybovanie
    pohybovanie = False  # Zastavenie pohybu


but_akcia = tkinter.Button(text="Akcia", command=akcia)
but_akcia.pack()
but_end = tkinter.Button(text="STOP", command=end)
but_end.pack()

c.mainloop()
