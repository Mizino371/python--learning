import tkinter
import random as r 
c = tkinter.Canvas(width=460,height=330)
c.pack()

def kruzok():
    x = r.randrange(450)
    y = r.randrange(320)
    if 100 < x < 150 or 50 < y < 100:
        c.create_oval(x-5, y-5, x+5, y+5, fill='green')
    else:
        c.create_oval(x-5, y-5, x+5, y+5, fill='yellow')
    c.update()

def loop():
    
    kruzok()
    c.after(100, loop)

c.after(100, loop)
c.mainloop()
