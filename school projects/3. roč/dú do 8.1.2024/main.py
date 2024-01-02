

# Moj postup je taký, že som si vytvoril funkciu move_ball, 
# ktorá posúva guľu o 5 px dole. 

# import tkinter as tk
# c = tk.Canvas( width=400, height=400)
# c.pack()
# 
# def move_ball():
    # c.move(ball, 0, 5)
    # c.after(100, move_ball)
    # 
# ball = c.create_oval(195, 195, 205, 205, fill='red')
# 
# move_ball()
# 
# c.mainloop()
# 
 
# 2. potrebný postup
import tkinter as tk
c = tk.Canvas( width=400, height=400)
c.pack()
x=195
y = 195
ball = c.create_oval(x, y, x+10, y+10, fill='red')
def move_ball():
    global x, y
   
    c.after(1,ball)
    y += 5

def vym_lopty():
    c.delete(100,ball)



def loop():
    move_ball()
    
    c.after(100,loop,)

loop()


c.mainloop()

# import tkinter as tk
# 
# c = tk.Canvas(width=400, height=400)
# c.pack()
# 
# Globálne premenné pre x, y súradnice a identifikátor loptičky
# x = 195
# y = 195
# ball = None  # Na začiatku nemáme žiadnu loptičku
# 
# def move_ball():
    # global x, y, ball
# 
    # Vymažeme starú loptičku
    # if ball is not None:
        # c.delete(ball)
# 
    # Vytvoríme novú loptičku a posunieme ju dolu
    # y += 5
    # ball = c.create_oval(x, y, x+10, y+10, fill='red')
    # c.after(100, move_ball)
# 
# Spustenie prvej iterácie
# 
# def loop():
    # move_ball()
    # c.after(100, loop)
# lopp()
# c.mainloop()
# 