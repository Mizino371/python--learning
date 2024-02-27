

# Moj postup je taký, že som si vytvoril funkciu move_ball, 
# ktorá posúva guľu o 5 px dole. 

import tkinter as tk
c = tk.Canvas( width=400, height=400)
c.pack()

def move_ball():
    c.move(ball, 0, 5)
    c.after(100, move_ball)
    
ball = c.create_oval(195, 195, 205, 205, fill='red')

move_ball()

c.mainloop()

 
# 2. potrebný postup



import tkinter
c= tkinter.Canvas()
c.pack()

def lopta():
    global y 
    c.delete('all')
    c.create_oval(x-5, y-5, x+5, y+5, fill='red')
    y=y+5
    if y<200:
        c.after(100, lopta)
        
x=200
y=5

lopta()

c.mainloop()