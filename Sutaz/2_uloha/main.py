import tkinter as t
from random import *
c=t.Canvas(width=500,height=500)
c.pack()

img_mach_O = t.PhotoImage(file= "Sutaz/2_uloha/zadanie/img/obrazky/machula0.png")
img_mach_1= t.PhotoImage(file="Sutaz/2_uloha/zadanie/img/obrazky/machula1.png")
img_mach_2 = t.PhotoImage(file="Sutaz/2_uloha/zadanie/img/obrazky/machula2.png")
img_mach_3 = t.PhotoImage(file="Sutaz/2_uloha/zadanie/img/obrazky/machula3.png")

img_kocka_0 = t.PhotoImage(file="Sutaz/2_uloha/zadanie/img/obrazky/stvorec0.png")
img_kocka_1 = t.PhotoImage(file="Sutaz/2_uloha/zadanie/img/obrazky/stvorec1.png")
img_kocka_2 = t.PhotoImage(file="Sutaz/2_uloha/zadanie/img/obrazky/stvorec2.png")    
img_kocka_3 = t.PhotoImage(file="Sutaz/2_uloha/zadanie/img/obrazky/stvorec3.png")


def nakresli_machulu():
    for i in range(4):
        postupnost = choice(["cervena","zelena","modra","zlta"])
        if i == 0:
            x=260
            y=90
        
        elif i == 1:
            x=200
            y=110
         
        elif i ==2:
            x =260
            y= 60
            
        elif i== 3:
            x=160,
            y=70
            
        if postupnost == "cervena":
            c.create_image(x,y,image= img_mach_O,tags=postupnost,anchor="nw")
        elif postupnost =="zelena":   
            c.create_image(x,y,image= img_mach_1,tags= postupnost,anchor="nw")
        elif postupnost == "modra":
            c.create_image(x,y,image= img_mach_2,tags= postupnost,anchor="nw")
        elif postupnost == "zlta":
            c.create_image(x,y,image= img_mach_3,tags= postupnost,anchor="nw")
        print(postupnost)

def stvorce():
    c.create_image(100,400,image= img_kocka_0, tags= "cerveny")
    c.create_image(160,400,image= img_kocka_1,tags = "zelena")
    c.create_image(220,400,image = img_kocka_2,tags = "modra")
    c.create_image(280,400,image =img_kocka_3, tags = "zlta")
    
def move_stvorec():
    if 
    c.move("")


stvorce()
 
nakresli_machulu()

c.bind("<Button-1>",)
c.mainloop()
