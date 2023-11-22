import tkinter
c=tkinter.Canvas(width=1600,height=800)
c.pack()
x1 = 200
x2 = 1400
y = 400

def štovrec(suradnice):
    y = suradnice.y
    x = suradnice.x
    if 398<=y<=402 and 200<=x<=1400:
        c.create_rectangle(x-10,y-10,x+10,y+10,fill="blue",outline="blue")
    else:
        c.create_oval(x-10,y-10,x+10,y+10,fill="yellow",outline="yellow")

c.create_line(x1,y,x2,y,width=4)

c.bind("<Button-1>",štovrec)

c.mainloop()