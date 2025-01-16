import tkinter
c = tkinter.Canvas( width=600, height=400)
c.pack()

obrazok_zaba_1 = tkinter.PhotoImage(file="4.roč/25-1-13/fotky zaba/zaba1.png")
obrazok_zaba_2 = tkinter.PhotoImage(file="4.roč/25-1-13/fotky zaba/zaba2.gif")

def klik_L(sur):
    c.create_image(sur.x,sur.y,image = obrazok_zaba_1)

def klik_R(sur):
    c.create_image(sur.x,sur.y,image = obrazok_zaba_2)
    
c.bind("<Button-1>",klik_L)
c.bind("<Button-3>",klik_R)



c.mainloop()