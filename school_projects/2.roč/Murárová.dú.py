import tkinter
canvas=tkinter.Canvas(width=750,height=400)
canvas.pack()

x=20
y=40
n=143
for i in range(10):
    canvas.create_line(x,y,x+25,y+25)
    canvas.create_line(x+25,y+25,x+50,y)
    canvas.create_line(x+50,y,x+25,y-25)
    canvas.create_line(x+25,y-25,x,y)
    canvas.create_line(x+42,y,x+67,y+25)
    canvas.create_line(x+67,y+25,x+92,y)
    canvas.create_line(x+92,y,x+67,y-25)
    canvas.create_line(x+67,y-25,x+42,y)
    canvas.create_line(x+93,y,x+118,y+25)
    canvas.create_line(x+118,y+25,x+143,y)
    canvas.create_line(x+143,y,x+118,y-25)
    canvas.create_line(x+118,y-25,x+93,y)
    x=+n
    
x=20
y=120
p=71
for i in range(10):
    canvas.create_line(x,y,x+30,y+30)
    canvas.create_line(x+30,y+30,x+60,y)
    canvas.create_line(x+60,y,x+45,y-15)
    canvas.create_line(x+45,y-15,x+30,y)
    canvas.create_line(x+30,y,x+15,y-15)
    canvas.create_line(x+15,y-15,x,y)
    x=x+p


x=20
y=200
m=82
for i in range(11):
    canvas.create_line(x,y+30,x,y)
    canvas.create_line(x,y,x+30,y)
    canvas.create_line(x+30,y,x+30,y+30)
    canvas.create_line(x+30,y+30,x+60,y+30)
    canvas.create_line(x+60,y+30,x+60,y)
    canvas.create_oval(x+15,y+15,x+15,y+15,width="3")
    canvas.create_oval(x+45,y+15,x+45,y+15,width="3")
    x=x+m

x=20
y=280
n=105
for i in range(8):
    canvas.create_line(x,y,x+30,y+30)
    canvas.create_line(x+30,y,x,y+30)
    canvas.create_line(x+40,y+15,x+55,y+30)
    canvas.create_line(x+55,y+30,x+70,y+15)
    canvas.create_line(x+70,y+15,x+55,y)
    canvas.create_line(x+55,y,x+40,y+15)
    canvas.create_line(x+54,y+15,x+69,y+30)
    canvas.create_line(x+69,y+30,x+84,y+15)
    canvas.create_line(x+84,y+15,x+69,y)
    canvas.create_line(x+69,y,x+54,y+15)
    x=x+n

    
x=50
y=360
n=117
for i in range(6):
    canvas.create_line(x,y+20,x+60,y-20)
    canvas.create_line(x+60,y-20,x+75,y+3)
    canvas.create_line(x+75,y+3,x+57,y+17)
    canvas.create_line(x+57,y+17,x+45,y)
    canvas.create_line(x+45,y,x+58,y-10)
    canvas.create_line(x+58,y-10,x+65,y)
    canvas.create_line(x+65,y,x+56,y+6.5)
    canvas.create_line(x,y+20,x-15,y-2)
    canvas.create_line(x-15,y-2,x+7,y-20)
    canvas.create_line(x+7,y-20,x+20,y-3)
    canvas.create_line(x+20,y-3,x+4.5,y+7.5)
    canvas.create_line(x+4.5,y+7.5,x-2.5,y-2)
    canvas.create_line(x-2.5,y-2,x+7.5,y-10)
    canvas.create_oval(x+88,y-12,x+88,y-12,width="2")
    canvas.create_oval(x+88,y+12,x+88,y+12,width="2")
    x=x+n

canvas.create_oval(25,y-12,25,y-12,width="2")
canvas.create_oval(25,y+12,25,y+12,width="2")

canvas.mainloop()

