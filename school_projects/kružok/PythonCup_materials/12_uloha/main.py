import tkinter as t
from random import *
from math import *
c=t.Canvas(width=500,height=500,bg="white",)
c.pack()

typ = 1
kaktus_img = t.PhotoImage(file="school_projects/kružok/PythonCup_materials/12_uloha/zadanie/img/kaktus.png")
balon1_img = t.PhotoImage(file=f"school_projects/kružok/PythonCup_materials/12_uloha/zadanie/img/balon_praskni/balon{typ}.png")
balon2_img = t.PhotoImage(file=f"school_projects/kružok/PythonCup_materials/12_uloha/zadanie/img/balon_praskni/balon{typ}.png")
balon3_img = t.PhotoImage(file=f"school_projects/kružok/PythonCup_materials/12_uloha/zadanie/img/balon_praskni/balon{typ}.png")


x_kaktus_r = randrange(400, 450)
y_kaktus_r = randrange(400, 450)


x_balon_r = randrange(50,100)
y_balon_r = randrange(50,100)
  
x_krok = (x_kaktus_r - x_balon_r) /10
y_krok = (y_kaktus_r - y_balon_r)/10

def kaktus():
    
    c.create_image(x_kaktus_r,y_kaktus_r,image=kaktus_img)
    
kaktus()

def move_baloon():
    x_krok = (x_kaktus_r - x_balon_r) /10
    y_krok = (y_kaktus_r - y_balon_r)/10
    c.move("balon",x_krok,y_krok,)

c.create_image(x_balon_r,y_balon_r,image= balon1_img,tags = "balon")

    
    
def loop():
    global typ
   
    
    x_balon_coords,y_balon_coords = c.coords("balon")
    if x_balon_coords != x_kaktus_r and y_balon_coords != y_kaktus_r:
        c.after(1000,loop)
        c.after(1000,move_baloon)
    elif x_balon_coords == x_kaktus_r and y_balon_coords == y_kaktus_r:
       typ +=1
       
        
       
    



loop()
c.mainloop()
    