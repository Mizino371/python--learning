import tkinter, random as r
from tkinter import PhotoImage
c=tkinter.Canvas(width=920,height=400)
c.pack()

pie_img_0 = [PhotoImage(file="school projects/kružok/2. uloha/kolace/kolac0.png")]
pie_img_1 = [PhotoImage(file="school projects/kružok/2. uloha/kolace/kolac1.png")]
pie_img_2 = [PhotoImage(file="school projects/kružok/2. uloha/kolace/kolac2.png")]
pie_img_3 = [PhotoImage(file="school projects/kružok/2. uloha/kolace/kolac3.png")]

global_images = []

def load_images():
    paths = ["school projects/kružok/2. uloha/kolace/kolac{}.png".format(i) for i in range(4)]
    for path in paths:
        img = PhotoImage(file=path)
        global_images.append(img)


                      
def tanier_vyzobrazenie():
    x=50
    for i in range(3):
        sirka_strany = 240
        topy= 50
        boty = 230
        c.create_rectangle(x,topy,x+sirka_strany,boty,width=3)
        x+=sirka_strany + 50


def vypocet(x):
     y=85
     for i in range(3):
        Wx = x
        for o in range(4):  
            r_kolac_uno = r.choice(global_images)
            prva_varka = c.create_image(Wx,y,image=r_kolac_uno)
            Wx +=55
        y+=55


def imp_kolace():


    prvy_tanier = ["school projects/kružok/2. uloha/kolace/kolac{}.png".format(i) for i in range(4)]
    druhy_tanier = ["school projects/kružok/2. uloha/kolace/kolac{}.png".format(i) for i in range(4)]
    treti_tanier = ["school projects/kružok/2. uloha/kolace/kolac{}.png".format(i) for i in range(4)]
    for p in range(3):
        if p ==0:

            for path in prvy_tanier:
                vyber_random = r.choice(prvy_tanier)
                img = PhotoImage(file=vyber_random)
                global_images.append(img)
                vypocet(85)
                break
                

        elif p==1:
             for path in druhy_tanier:
                vyber_random = r.choice(druhy_tanier)
                img = PhotoImage(file=vyber_random)
                global_images.append(img)
                vypocet(375)
                break
                
        elif p== 2:
            for path in treti_tanier:
                vyber_random = r.choice(treti_tanier)
                img = PhotoImage(file=vyber_random)
                global_images.append(img)
                vypocet(670)
                break





load_images()
tanier_vyzobrazenie()  
imp_kolace()
c.mainloop()

