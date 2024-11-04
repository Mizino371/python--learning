import tkinter
c=tkinter.Canvas(width=600,height=500)
c.pack()
relative_path = "4.roč/24-10-27/Domaca2.0/štatistika-bodov.txt"
počitanie_bodov = 0
def zapis_bodu(suradnice):
    global subor,počitanie_bodov
        
    subor = open(relative_path,"a")
    x = suradnice.x
    y = suradnice.y
    počitanie_bodov += 1
    print(f"{počitanie_bodov}=>\nX = {x} \nY = {y}\n",file=subor)
    c.create_oval(x-10,y-10,x+10,y+10)
    c.create_text(x,y,text=počitanie_bodov)
    subor.close()

def clear(s):
    global subor,počitanie_bodov
    počitanie_bodov = 0
    with open(relative_path,"w") as file:
        pass
    c.delete("all")
      

c.bind("<Button-1>", zapis_bodu)
c.bind_all("<space>",clear)


c.mainloop()
    