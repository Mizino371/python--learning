import tkinter as t
from random import *
from math import *
c=t.Canvas(width=500,height=800,bg="white",)
c.pack()
typ = 0 #0,3,4
y = randint(100,400)
trampolina_img = t.PhotoImage(file="school_projects/kružok/PythonCup_materials/15_uloha/img/trampolina.png")
simon_img0 = t.PhotoImage(file=f"school_projects/kružok/PythonCup_materials/15_uloha/img/simon (1)/p0.png")    
simon_img3 = t.PhotoImage(file=f"school_projects/kružok/PythonCup_materials/15_uloha/img/simon (1)/p3.png")
simon_img4 = t.PhotoImage(file=f"school_projects/kružok/PythonCup_materials/15_uloha/img/simon (1)/p4.png")        
c.create_image(250,750,image= trampolina_img)


c.create_image(250,690,image= simon_img0,tags="simon")

posuny = -5
def simon():
    global posuny
    vyskok = 690 - (randint(200,600))
    poloha_simona = c.coords("simon")
    
    if poloha_simona[1] >=690:
        c.delete("simon")                   # zmena obrázkov 
        c.create_image(250,690,image= simon_img0,tags="simon")
        posuny = -8
    elif poloha_simona[1] <= vyskok:
        c.delete("simon")
        r_num = randint(1,2)
        if r_num == 1 :
            c.create_image(250,vyskok,image= simon_img3,tags="simon")
        elif r_num == 2:
            c.create_image(250,vyskok,image= simon_img4,tags="simon")   
        posuny = 8
        
    c.move("simon",0,posuny)
    

def loop():
    c.after(100,loop)
    c.after(100,simon)
    
loop()
c.mainloop()