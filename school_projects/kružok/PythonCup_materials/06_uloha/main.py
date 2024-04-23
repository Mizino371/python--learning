# 480x346
import tkinter
import random as r 
c = tkinter.Canvas( width=480, height=380, background="white")
c.pack()
netrafil = 0
ihrisko_img= tkinter.PhotoImage(file="school_projects/kružok/PythonCup_materials/06_uloha/img/ihrisko.png")
lopta_img= tkinter.PhotoImage(file="school_projects/kružok/PythonCup_materials/06_uloha/img/lopta.png")
x_ball=109
y_ball= 177
# ihrisko

# lopta



    
    


def program():
    c.delete("ball")
    global netrafil
    c.create_image(243,176, image = ihrisko_img)
    c.create_image(x_ball,y_ball, image = lopta_img,tags= "ball")
    r_move_x = r.randint(0,371)
    r_move_y = r.randint(-177,177)
    def move_ball ():
        c.move("ball", r_move_x,r_move_y)
    c.after(200,move_ball)
    x_coords_ball,y_coords_ball = c.coords("ball")
    if 453<x_coords_ball <480 and 140<y_coords_ball<205:
        c.create_text(243,176,text="GÓÓÓL !",fill="white")
    else:
        if netrafil == 0:
            netrafil +=1
            c.create_text(243,176,text="SKús znova",fill="white")
            button1 = tkinter.Button(text= "Skús znova", command=program)
            button1.pack()
        else: 
            c.create_text(243,176,text="SKús znova",fill="white")

    

    
    
program()
c.mainloop()