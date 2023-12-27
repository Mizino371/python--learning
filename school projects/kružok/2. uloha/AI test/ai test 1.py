import tkinter as tk
import random as r
from tkinter import PhotoImage

# Globálne premenné
posledny_kolac_x = 50  # Počiatočná x pozícia pre prvý koláč
posledny_kolac_y = 350  # Y pozícia pre všetky koláče

c = tk.Canvas(width=920, height=400)
c.pack()
global_images = [PhotoImage(file=f"school projects/kružok/2. uloha/kolace/kolac{i}.png") for i in range(4)]

def tanier_vyzobrazenie():
    x = 50
    for i in range(3):
        sirka_strany = 240
        topy = 50
        boty = 230
        c.create_rectangle(x, topy, x + sirka_strany, boty, width=3)
        x += sirka_strany + 50

def klik_na_kolac(event):
    global posledny_kolac_x
    kolac_id = event.widget.find_withtag("current")[0]
    info = c.gettags(kolac_id)
    # Ak je to prvý výber alebo ak vyberáme rovnaký typ koláča a z rovnakej tácky
    if predchadzajuci_vyber['kolac'] is None or (predchadzajuci_vyber['kolac'] == info[0] and predchadzajuci_vyber['tanier'] == info[1]):
        predchadzajuci_vyber['kolac'], predchadzajuci_vyber['tanier'] = info[0], info[1]
        c.coords(kolac_id, posledny_kolac_x, posledny_kolac_y)
        posledny_kolac_x += 50  # Posun x pozície pre ďalší koláč
    else:
        c.create_text(150, 390, text="Vybral si zle. Vyberaj rovnaké koláče z rovnakej tácky.")

# Uchovávanie predchádzajúceho výberu
predchadzajuci_vyber = {'kolac': None, 'tanier': None}

# Vytvorenie koláčov
for tanier_id in range(3):
    for kolac_id in range(12):
        kolac_type = r.randint(0, 3)
        kolac_img = global_images[kolac_type]
        x = 80 + (kolac_id % 4) * 60 + (tanier_id * 290)
        y = 80 + (kolac_id // 4) * 60
        zobrazenie_kolac = c.create_image(x, y, image=kolac_img)
        c.tag_bind(zobrazenie_kolac, "<Button-1>", klik_na_kolac)
        c.addtag_withtag(f"k{kolac_type}", zobrazenie_kolac)  # Tag pre typ koláča
        c.addtag_withtag(f"t{tanier_id}", zobrazenie_kolac)  # Tag pre tácku

tanier_vyzobrazenie()
c.mainloop()
