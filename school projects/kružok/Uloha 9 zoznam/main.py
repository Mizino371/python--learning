import tkinter as tk 
import random as r 

c=tk.Canvas(width=600, height=600)
c.pack()
                                                    #tabuľa so skóre
c.create_rectangle(360,270,300,330,width=4)
c.create_rectangle(300,330,240,270,width= 4)


def hrac1():
    if logika == hrac1:      # ak hrac1 vyhrá tak zdvihne ruku 
        posun = 70
    else:
        posun = 0
    
                                                    #trup
    c.create_line(80,80,80,160)
                                                #hlava
    c.create_oval(100,80,60,40,)
                                            #nohy
    c.create_line(80,160,100,220)
    c.create_line(80,160,60,220)
                                        #ruky
    c.create_line(80,100,40,130)
    c.create_line(80,100,120,130-posun)
    
def hrac2():
    if logika == hrac2:       # ak hrac2 vyhrá tak zdvihne ruku 
        posun = 70
    else:
        posun = 0
    
                                                    #trup
    c.create_line(520,80,520,160)
                                                #hlava
    c.create_oval(540,80,500,40)
                                            #nohy
    c.create_line(520,160,540,220)
    c.create_line(520,160,500,220)
                                        #ruky
    c.create_line(520,100,480,130-posun)
    c.create_line(520,100,560,130)

def rozhodca():
    
    if logika == hrac1:
        posun1 = 70
        posun2 = 0
    elif logika == hrac2:
        posun2 = 70
        posun1 = 0
        
                                                    #trup
    c.create_line(300,400,300,480)
                                                #hlava
    c.create_oval(320,400,280,360)
                                            #nohy
    c.create_line(300,480,320,540)
    c.create_line(300,480,280,540)
                                        #ruky
    c.create_line(300,420,260,450-posun1)
    c.create_line(300,420,340,450-posun2)

# def hlavna_hra():
    

logika = hrac2
hrac1()
hrac2()
rozhodca()
c.mainloop()