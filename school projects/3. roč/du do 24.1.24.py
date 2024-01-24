import tkinter
from random import *
canvas=tkinter.Canvas(width=600, height=600)
canvas.pack()

def stvorcek(x,y,info):
    canvas.create_rectangle(x-10, y-10, x+10, y+10)
    canvas.create_text(x, y, text=info)

def button1_klik():
    stvorcek(randrange(300), randrange(200), randrange(100))

button1 = tkinter.Button(text='kresli stvorcek', command=button1_klik)
button1.pack()

def button2_klik():
    x=randrange(300)
    y=randrange(200)
    for i in range (1,11):
        stvorcek(x+i*20,y,i)

button2=tkinter.Button(text='stvorceky',command=button2_klik)
button2.pack()
canvas.mainloop()