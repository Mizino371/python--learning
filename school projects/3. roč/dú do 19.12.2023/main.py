import tkinter
import random as r 
canvas = tkinter.Canvas(width=460,height=330)
canvas.pack()

def kruzok():
    x = r.randrange(450)
    y = r.randrange(320)
    if 100 < x < 150 or 50 < y < 100:
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='green')
    else:
        canvas.create_oval(x-5, y-5, x+5, y+5, fill='yellow')
    canvas.update()

def loop():
    
    kruzok()
    canvas.after(10, loop)

canvas.after(10, loop)
canvas.mainloop()
