import tkinter as t
from random import *
c=t.Canvas(width=500, height=500,bg= "white")
c.pack()



def lopta():
    global x,y
    x= randint(10, 490)
    y= randint(10,400)
    
    lopta_poloha = c.coords("lopta"[1])
    c.create_oval(x,y,x+20,y+20,tags="lopta")
    # if lopta_poloha 
    
def pohyb_ciary(event):
    
    c.create_line(250,490,300,490,tags="ciara")
    if event.keysym =="Left":
        c.move("ciara",-5,0)
    elif event.keysym =="Right":
        c.move("ciara",5,0)
    
def loop():
     c.after(100,loop)
     c.after(100,lopta)
     
    
c.bind_all("<KeyPress>",pohyb_ciary)

c.mainloop()