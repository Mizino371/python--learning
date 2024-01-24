

import tkinter, random 
canvas= tkinter.Canvas(width = 600, height = 600)
canvas.pack()

def stvorcek(x,y,info):

    canvas.create_rectangle(x-10,y-10,x+10,y+10)

    canvas.create_text(x,y,text = info)

def button1_klik():
    stvorcek(random.randrange(300),random.randrange(200),random.randrange(100))

def button2_klik():
    for i in range(1,11):
        stvorcek(i*20,100,200)



def button3_klik():
    plus1=  0
    for i in range(int(entry1.get()),int(entry2.get())):
        stvorcek(i*20,200,int(entry1.get())+plus1)
        plus1 = plus1 + 1
        
   


button1 = tkinter.Button(text="kresli štvorček", command= button1_klik)
button1.pack()

button2  = tkinter.Button(text="kresli štvorčeky", command= button2_klik)
button2.pack()

button3 = tkinter.Button(text="postupnosť",command=button3_klik)
button3.pack()


entry1 = tkinter.Entry()
entry1.pack()

entry2 = tkinter.Entry()
entry2.pack()

canvas.mainloop()
