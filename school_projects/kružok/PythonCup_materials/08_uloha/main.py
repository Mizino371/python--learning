import tkinter as t
import random as r
c=t.Canvas(width=500,height=500, bg="white")
c.pack()

chrobak_img = t.PhotoImage(file= "kružok/PythonCup_materials/08_uloha/img/chrobacik.png")
lienka_img = t.PhotoImage(file= "kružok/PythonCup_materials/08_uloha/img/lienka.png")

c.create_image(20,480,image= lienka_img, tags="lienka")

x_rand_chrobak = r.randint(20,480)
y_rand_chrobak = r.randint(20,480)
c.create_image(x_rand_chrobak,y_rand_chrobak,image= chrobak_img, tags="chrobak")

def posuny(event):
    if event.keysym == "Up":
        c.move("lienka", 0,-4)
    elif event.keysym == "Down":
        c.move("lienka",0,4)
    elif event.keysym == "Left":
        c.move("lienka",-4,0)
    elif event.keysym == "Right":
        c.move("lienka",4,0)
    elif event.keysym =="Up" and "Right":
        c.move("lienka",4,-4)
    elif event.keysym =="Up" and "Left":
        c.move("lienka",-4,-4)
    elif event.keysym =="Down" and "Right":
        c.move("lienka",4,4)
    elif event.keysym =="Down" and "Left":
        c.move("lienka",-4,4)
    check_collision()
def check_collision():
    lienka_pos = c.coords("lienka")
    chrobak_pos = c.coords("chrobak")
    if chrobak_pos[0]-25 <lienka_pos[0] < chrobak_pos[0]+25 and chrobak_pos[1]-25 <lienka_pos[1] < chrobak_pos[1]+25:
        print("Ahoj Chrobáčik")




c.bind_all("<KeyPress>",posuny)

c.mainloop()