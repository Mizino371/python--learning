import tkinter as t
import random as r
c=t.Canvas(width=500,height=500, bg="white")
c.pack()


def player():
    # telo...
    r_num =r.randint(1,6)
    x_kocka= r.randint(10,390)
    y_kocka= r.randint(10,190)
    c.create_text(250,300,text=f"chcem hodiť {r_num}", fill="black")
    c.create_rectangle(x_kocka,y_kocka,x_kocka+100,y_kocka+100,outline="black",width=2)
    if r_num == 1 :
        c.create_oval(x_kocka+40,y_kocka+40,x_kocka+60,y_kocka+60,fill="black")
    elif r_num == 2:
        c.create_oval(x_kocka+15,y_kocka+15,x_kocka+35,y_kocka+35,fill="black")
        c.create_oval(x_kocka+65,y_kocka+65,x_kocka+85,y_kocka+85,fill="black")
    elif r_num == 3:
        c.create_oval(x_kocka+40,y_kocka+40,x_kocka+60,y_kocka+60,fill="black")
        c.create_oval(x_kocka+15,y_kocka+15,x_kocka+35,y_kocka+35,fill="black")
        c.create_oval(x_kocka+65,y_kocka+65,x_kocka+85,y_kocka+85,fill="black")
    elif r_num == 4:
        c.create_oval(x_kocka+15,y_kocka+15,x_kocka+35,y_kocka+35,fill="black")
        c.create_oval(x_kocka+15,y_kocka+65,x_kocka+35,y_kocka+85,fill="black")
        c.create_oval(x_kocka+65,y_kocka+65,x_kocka+85,y_kocka+85,fill="black")
        c.create_oval(x_kocka+65,y_kocka+15,x_kocka+85,y_kocka+35,fill="black")
    elif r_num == 5:
        c.create_oval(x_kocka+15,y_kocka+15,x_kocka+35,y_kocka+35,fill="black")
        c.create_oval(x_kocka+15,y_kocka+65,x_kocka+35,y_kocka+85,fill="black")
        c.create_oval(x_kocka+65,y_kocka+65,x_kocka+85,y_kocka+85,fill="black")
        c.create_oval(x_kocka+65,y_kocka+15,x_kocka+85,y_kocka+35,fill="black")
        c.create_oval(x_kocka+40,y_kocka+40,x_kocka+60,y_kocka+60,fill="black")
    elif r_num == 6:
        c.create_oval(x_kocka+15,y_kocka+15,x_kocka+35,y_kocka+35,fill="black")
        c.create_oval(x_kocka+15,y_kocka+65,x_kocka+35,y_kocka+85,fill="black")
        c.create_oval(x_kocka+65,y_kocka+65,x_kocka+85,y_kocka+85,fill="black")
        c.create_oval(x_kocka+65,y_kocka+15,x_kocka+85,y_kocka+35,fill="black")
        c.create_oval(x_kocka+15,y_kocka+40,x_kocka+35,y_kocka+60,fill="black")
        c.create_oval(x_kocka+65,y_kocka+40,x_kocka+85,y_kocka+60,fill="black")
def loop():
    c.delete("all")
    c.after(800,loop)
    c.after(800,player) 
loop()

c.mainloop()