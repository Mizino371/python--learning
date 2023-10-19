import tkinter,random
c=tkinter.Canvas(width=800, height=600)
c.pack()

def strecha(suradnice):
    x=suradnice.x
    y=suradnice.y
    c.create_polygon(x,y,x+20,y-15,x+40,y,fill="brown",)

def domek(suradnice):
    x=suradnice.x
    y=suradnice.y
    f = random.choice(("blue", "yellow", "red","purple", "green", "light blue", "dark red"))
    c.create_rectangle(x-20,y-20,x+20,y+20,fill=f,outline=f)

def meno(NahodnaVec):
    c.create_text(725,15,text="Michal Palenčár", font="Helvica 15")

c.bind("<Button-3>",strecha)
c.bind("<Button-1>",domek)
c.bind_all("<m>",meno)

c.mainloop()