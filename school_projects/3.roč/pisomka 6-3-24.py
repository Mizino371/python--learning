import tkinter,random
c=tkinter.Canvas(width=1000,height =500)
c.pack()


c.create_line(0,250,1000,250,width= 5)

def klik_na_platno(suradnice):
    x=suradnice.x
    y=suradnice.y

    if (y<250):
        c.create_text(x,y,text="Python", fill= "red", angle= x*-1)

    elif(y>250):
        c.create_text(x,y,text="Python", fill= "blue", angle= x*-1)
    else:
        print("Error")


def stvorceky(suradnice):
    x=suradnice.x
    y=suradnice.y

    for i in range(10):
        c.create_rectangle(x,y,x+15,y+15)
        x +=20

    


c.bind("<Button-3>",stvorceky)
c.bind("<Button-1>",klik_na_platno)
