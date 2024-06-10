import tkinter
import random as r
canvas = tkinter.Canvas (width=700,height=600,bg="white")
canvas. pack () 
def timer1 ():
    canvas.delete ('all')
    global sx, sy
    sx = r.randrange (300)
    sy = r.randint (20, 250)
    canvas.create_rectangle(sx, sy, sx+velkost, sy+velkost, fill='green')
    canvas.create_text (100, 10, text="Pocet ziskaných bodov:",fill="black")
    canvas.create_text (200, 10, text=pocet_bodov,fill="black")
    if -10<pocet_bodov <10:
       canvas.after (800, timer1)
    elif pocet_bodov>=10:
            canvas.create_text(350,300,text="Si dobrý",fill="black")
    elif pocet_bodov<=-10:
        canvas.create_text(350,300,text="Nejdete ti to",fill="black")
        
          
    
def klik (suradnice) :
    global pocet_bodov
    x = suradnice.x
    y = suradnice.y
    if sx < x < sx+velkost and sy < y < sy+velkost:
        pocet_bodov += 1
    else:
        pocet_bodov -= 1
    
pocet_bodov =0
SX = 0
Sy = 0
velkost = 50
timer1 ()
canvas.bind ('<Button-1>', klik)

canvas.mainloop()