import tkinter, random as r



c=tkinter.Canvas(width=500,height=500,bg='white')
c.pack()
def delete_all():
    c.delete("all")
game_count  = 0
def hra():
    c.delete("all")
    c.update()
    cisla = [0] * 3
    for i in range(3):
        cisla[i] = r.randint(1,6)
        c.after(2000)

        c.create_text(100+(i*100),250,text=cisla[i],font="Arial 60")
        c.update()

    c.after(1000)
    if cisla[0] == cisla[1] ==cisla[2]:
        text = "Bingo"
    elif cisla[0] == cisla[1] or cisla[1] == cisla[2] or cisla[0] == cisla[2]:
        text = "SUPER"
    else:
        text = "NABUDÚCE"
    c.create_text(245,400,text=text,font="Arial 30")

button1 = tkinter.Button(text="Hra",command=hra)
button1.pack()

c.mainloop()

