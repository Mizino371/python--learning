import tkinter as tk 
import random as r 

c=tk.Canvas(width=600, height=600)
c.pack()
                                                    #tabuľa so skóre

hrac1_score,hrac2_score = 0,0

def hrac1():
    global posun1    # if logika == hrac1:      # ak hrac1 vyhrá tak zdvihne ruku 
    #     posun = 70
    # else:
    #     posun = 0
    
                                                    #trup
    c.create_line(80,80,80,160)
                                                #hlava
    c.create_oval(100,80,60,40)
                                            #nohy
    c.create_line(80,160,100,220)
    c.create_line(80,160,60,220)
                                        #ruky
    c.create_line(80,100,40,130)
    c.create_line(80,100,120,130-posun1)
    
def hrac2():
    global posun2
    # if logika == hrac2:       # ak hrac2 vyhrá tak zdvihne ruku 
    #     posun = 70
    # else:
    #     posun = 0
    
                                                    #trup
    c.create_line(520,80,520,160)
                                                #hlava
    c.create_oval(540,80,500,40)
                                            #nohy
    c.create_line(520,160,540,220)
    c.create_line(520,160,500,220)
                                        #ruky
    c.create_line(520,100,480,130-posun2)
    c.create_line(520,100,560,130)

def rozhodca():
    global posun1,posun2
    # if logika == hrac1:
    #     posun1 = 70
    #     posun2 = 0
    # elif logika == hrac2:
    #     posun2 = 70
    #     posun1 = 0
        
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

def hlavna_hra():
    c.create_rectangle(360,270,300,330,width=4)
    c.create_rectangle(300,330,240,270,width= 4)
    global posun2
    global posun1
    global hrac1_score, hrac2_score
    posun2 = 0
    posun1 = 0
    hrac1_vyber =r.randint(1,100)
    hrac2_vyber = r.randint(1,100)
    if hrac1_vyber > hrac2_vyber:
        posun1 = 70
        posun2 = 0
        hrac1_score +=1
    elif hrac1_vyber < hrac2_vyber:
        posun1 = 0
        posun2 = 70
        hrac2_score +=1
    elif hrac1_vyber == hrac2_vyber:
        posun1,posun2 = 70,70
    else:
        print("EROR OCCURED")
        
    c.create_text(270,300,text=f"{hrac1_score}",font= ("Helvitica", "30"))
    c.create_text(330,300,text=f"{hrac2_score}", font=("Helvitica", "30"))
    c.create_text(150,300,text=f"nNáhodný výber hráča 2: {hrac1_vyber}")
    c.create_text(450,300,text=(f"Náhodný výber hráča 1: {hrac2_vyber}"))
    
    hrac1()
    hrac2()
    rozhodca()
    
def clear_canvas():
    c.delete("all")
    
    
def loop():
    hlavna_hra()
    c.after(1500,loop)       
    c.after(3000,clear_canvas)
    
c.after(1500,loop)
c.mainloop()