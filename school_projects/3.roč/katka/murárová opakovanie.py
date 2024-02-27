import tkinter,random
canvas=tkinter.Canvas(height=600,width=800)
canvas.pack()

x=50
y=50
f=random.choice(("orange","blue","red","green"))

def stvorec(suradnice):
    x=suradnice.x
    y=suradnice.y
    f=random.choice(("orange","blue","red","green"))
    canvas.create_rectangle(x,y,x+40,y+40,fill=f)
canvas.bind("<Button-1>",stvorec)

def trojuholnik(suradnice):
    x=suradnice.x
    y=suradnice.y
    canvas.create_polygon(x,y,x+20,y-20,x+40,y,fill="brown")

canvas.bind("<Button-3>",trojuholnik)

x=750
y=10
def meno(event):
    x=750
    y=10
    canvas.create_text(x,y,text="KATKA")
canvas.bind_all("<m>",meno)

canvas.mainloop()
