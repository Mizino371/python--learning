import tkinter, math, random as r 
c= tkinter.Canvas(width=1000,height=500)
c.pack()

def vymaž():
    c.delete("all")    

def kruh():
    global polomer, stred_kruhu
    
    random_x= r.randint(100,900)
    random_y = r.randint(100,400)
    velkost_kruhu = r.randint(50,120)
    stred_kruhu = random_x + velkost_kruhu/2 , random_y + velkost_kruhu/2
    polomer = (velkost_kruhu+random_x)-stred_kruhu[0]
    c.create_oval(random_x,random_y,random_x+velkost_kruhu,random_y+velkost_kruhu)
    
def skontroluj_klik(suradnice):
    klik_x = suradnice.x
    klik_y = suradnice.y
    vzdialenost_od_kruhu = math.sqrt( (klik_x - stred_kruhu[0])**2 + (klik_y - stred_kruhu[1])**2 )
    if vzdialenost_od_kruhu <= polomer:
        c.create_text(stred_kruhu[0],stred_kruhu[1],text="Trafil si", fill="green", font=("Arial",20))
    else:
        c.create_text(stred_kruhu[0],stred_kruhu[1],text="Netrafil si", fill="red", font=("Arial",20))

    c.after(500,vymaž)
    c.after(550,kruh)
    c.update()


  
    
c.bind("<Button-1>",skontroluj_klik)
kruh()

c.mainloop()