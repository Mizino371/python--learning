import tkinter
c=tkinter.Canvas(width=600, height=500)
c.pack()

x= 300
y = 30
pohyb = False

def delete():
    c.delete("all")


def gulka(smer):
    global pohyb,x,y
    if not pohyb:
        return

    delete()
    if smer == "dole" and y<500:
        y+=5
    elif smer == "hore" and y>0:
        y-= 5
    else:
        if smer == "dole":
            smer = "hore"
        else:
            smer = "dole"
    c.create_oval(x-5,y-5,x+5,y+5,fill="red")
    c.update()
    c.after(50,gulka,smer)

def akcia():
    global pohyb
    pohyb = True
    gulka("dole")

def stop():
    global pohyb
    pohyb = False
    c.after(800,exit)

but_akcia = tkinter.Button(text="Akcia", command=akcia)
but_akcia.pack()

but_end = tkinter.Button(text="STOP", command=stop)
but_end.pack()

gulka("dole")
c.mainloop()