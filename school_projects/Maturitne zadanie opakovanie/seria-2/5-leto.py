import tkinter,random
canvas=tkinter.Canvas(width=800,height=600)
canvas.pack()

def klik(sur):
    x = sur.x
    y = sur.y
    if y<300:
        while y <610:
            balon(x,y)
            canvas.update()
            canvas.after(500)
            canvas.delete("balon")
            y+=10
    else:
        while x <810:
            lodka(x,y)
            canvas.update()
            canvas.after(500)
            canvas.delete("lodka")
            x+=10
def balon(x,y):
       canvas.create_oval(x,y,x+50,y+50,fill='light blue',tags="balon")
       canvas.create_line(x,y+29,x+25,y+80,tags="balon")
       canvas.create_line(x+50,y+29,x+25,y+80,tags="balon")
       canvas.create_rectangle(x+10,y+80,x+40,y+100,fill='brown',tags="balon")

def lodka(x,y):
    canvas.create_polygon(x+120,y-30,x+210,y-30,x+200,y,x+130,y,x+120,y-30,fill='red',tags="lodka")
    canvas.create_polygon(x+165,y-95,x+190,y-65,x+165,y-45,x+165,y-95,fill='white',outline='black',tags="lodka")
    canvas.create_line(x+165,y-30,x+165,y-95,width=2,tags="lodka")

canvas.create_rectangle(0,300,800,600,fill="light blue")

canvas.bind("<Button-1>", klik)
canvas.mainloop()