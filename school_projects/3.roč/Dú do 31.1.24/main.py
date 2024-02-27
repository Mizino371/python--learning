

import tkinter as tk
from random import *
c= tk.Canvas(width = 600, height = 600)
c.pack()

def stvorcek(x,y,info):
    c.create_rectangle(x-10,y-10,x+10,y+10)
    c.create_text(x,y,text = info)

def button1_klik():
    stvorcek(randrange(300),randrange(200),randrange(100))

def button2_klik():
    for i in range(1,11):
        stvorcek(i*20,100,200)



def button3_klik():
    bonus=  0
    for i in range(int(entry1.get()),int(entry2.get())):
        stvorcek(i*20,200,int(entry1.get())+bonus)
        bonus = bonus + 1
        
   

button1 = tk.Button(text="kresli štvorček", command= button1_klik)
button1.pack()

button2  = tk.Button(text="kresli štvorčeky", command= button2_klik)
button2.pack()

button3 = tk.Button(text="postupnosť",command=button3_klik)
button3.pack()


entry1 = tk.Entry()
entry1.pack()

entry2 = tk.Entry()
entry2.pack()

c.mainloop()
