import tkinter
c=tkinter.Canvas(width=200,height=200,bg="white")
c.pack()

c.create_oval(140,140,160,160,fill="brown",tags = "had")
def posun(sur):
    if sur.keysym == "Up":
        c.move("had",0,-2)
        if 0 >= c.coords("had")[1]:

    elif sur.keysym == "Down":
        c.move("had",0,2)
    elif sur.keysym == "Left":
        c.move("had",-2,0)
    elif sur.keysym == "Right":
        c.move("had",0,2)



c.mainloop()