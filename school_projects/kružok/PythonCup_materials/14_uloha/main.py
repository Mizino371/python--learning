from turtle import *
from random import *
def metla(dlzka_metly,pocet_ruc,dlzka_stet):
    fd(dlzka_metly)
    left(45)
    uhol = 90/pocet_ruc
    for i in range(pocet_ruc):
        for l in range(2):
            fd(dlzka_stet)
            rt(180)
        right(uhol)
    rt(135)
    fd(dlzka_metly)
    rt(180)
speed(6) 
def vela_metiel():
    r_pocet_metiel = randint(5,20)
    r_rotation = randint(0,360)
    rt(r_rotation)
    for i in range(r_pocet_metiel):
        x_pos_r = randint(0, 500)
        y_pos_r = randint(0, 500)
        r_dlzka_m = randint(50,100)
        r_pocet_ruc = randint(5,20)
        r_dlzka_stet = randint(20,40)
        penup()
        goto(x_pos_r,y_pos_r)
        pendown()
        metla(r_dlzka_m,r_pocet_ruc,r_dlzka_stet)

vela_metiel()
    
mainloop()
    