import tkinter as t
c=t.Canvas(width=500,height=500)
c.pack()

x=20
y=20
c.create_rectangle(x,y,x+20,y+20,tags="stvorec")
pos = 5
def move_obj():
    global pos
    coord_stvor =c.coords("stvorec")    
    
    
    
        # kontrola polohy a okrajov 
    if coord_stvor[0]+15>=500: #pravá stena check
        pos = -5
    
    elif coord_stvor[0]<=0: # ľavá strana check
        pos = 5
    c.move("stvorec",pos,0)

def loop():                 #opakovanie
    c.after(100,loop)
    c.after(100,move_obj)  

loop()
c.mainloop()