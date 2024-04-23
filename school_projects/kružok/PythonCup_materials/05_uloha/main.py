import tkinter
import random as r 
c = tkinter.Canvas( width=500, height=500, bg='white')
c.pack()

mesec_img = tkinter.PhotoImage(file="school_projects/kružok/PythonCup_materials/05_uloha/img/mesec.png")
mince_img = tkinter.PhotoImage(file="school_projects/kružok/PythonCup_materials/05_uloha/img/minca.png")

mesec=c.create_image(250,300,image= mesec_img)
def user_input():
    num_of_coins = int(input("Koľko mincí potrebujeme? "))
    for i in range(num_of_coins):
        r_pos_x = r.randint(10 , 490)
        r_pos_y = r.randint(10 , 490)
                    #position check --> nemôže byť tam kde je mešec
        if 200<r_pos_x <300 and 250<r_pos_y<350:
            r_pos_x += 60
            r_pos_y -=60
        c.create_image(r_pos_x,r_pos_y,image =mince_img)

user_input()
c.mainloop()