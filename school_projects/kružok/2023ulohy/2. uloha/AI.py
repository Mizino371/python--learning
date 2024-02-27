import tkinter as tk
from tkinter import PhotoImage
import random

c = tk.Canvas(width=2000, height=560)
c.pack()

def fotky():
    vyber_zviera = random.randint(0, 4)
    stopy = PhotoImage(file=f"school projects/kružok/2023 ulohy/2. uloha/zvierata+stopy/stopy{vyber_zviera}.png")
    
    for i in range(5):
        if i != vyber_zviera:
            c.create_image(100 + i * 100, 100, anchor=tk.CENTER, 
                           image=PhotoImage(file=f"school projects/kružok/2023 ulohy/2. uloha/zvierata+stopy/zviera{i}.png"), 
                           tags="nespravne_zviera")    
        else:
            zviera = PhotoImage(file=f"school projects/kružok/2023 ulohy/2. uloha/zvierata+stopy/zviera{i}.png")
            c.create_image(100 + i * 100, 100, anchor=tk.CENTER, image=zviera, tags="spravne_zviera")
            print(f"spravne zviera {i}")

fotky()

c.mainloop()
