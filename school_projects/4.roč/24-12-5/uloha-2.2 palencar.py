import tkinter, math as m
from datetime import datetime
p_hodin = int( input("zadaj polomer hodín: "))
w_platna = (p_hodin*1.5)*2
h_platna = (p_hodin*1.5)*2

c= tkinter.Canvas(width=w_platna,height=h_platna)
c.pack()

hodiny = True 
stred = w_platna/2,h_platna/2
polomer = p_hodin
uhol_zac_cisla = -90
aktualny_cas = datetime.now() 
# určenie posunutia ručičiek na základe aktuálneho času  
s_uhol_rucicka = -90 +(aktualny_cas.second*6)   # -90 je základ pri 12 hodine. K nemu sa priráta počet sekúnd
                                                # a vynásobí sa 6 pretože 360/60 = 6
m_uhol_rucicka = -90 +((aktualny_cas.minute*6)+(aktualny_cas.second*0.1)) # to isté ako pri sekunde, 
                                                            # kedže 60 minút je 360 stupnov a k nemu prirátame
                                                            # ešte aj posunutie medzi minútami 
h_uhol_rucicka = -90 +((aktualny_cas.hour*30)+(aktualny_cas.minute*0.5)+(aktualny_cas.second*(0.5/60)))      
                                                            # to isté ako pri minútach

c.create_oval(stred[0]-polomer, stred[1]-polomer, stred[0]+polomer,stred[1]+polomer,width=3)

def cisla(uhol):
    uhol_r = m.radians(uhol)                        
    x = (m.cos(uhol_r) * ((23/20)*polomer)) + stred[0]     
    y = (m.sin(uhol_r) * ((23/20)*polomer))+ stred[1]
    if i2 == 0:
        c.create_text(x,y,text="12")
    else:
        c.create_text(x,y,text=f"{i2}")

def delete_rucicka():
    c.delete("s_rucicka")
    c.delete("m_rucicka")
    c.delete("h_rucicka")
# vykreslenie sekundovej ručičky   
def s_rucicka(uhol):
    uhol_rad = m.radians(uhol)
    x2 = (m.cos(uhol_rad) * ((17/20)*polomer)) + stred[0]
    y2 = (m.sin(uhol_rad) * ((17/20)*polomer))+ stred[1]
    c.create_line(stred[0],stred[1],x2,y2,tags="s_rucicka")
     
# vykreslenie minútovej ručičky   
def m_rucicka(uhol):
    uhol_rad = m.radians(uhol)
    x2 = (m.cos(uhol_rad) * ((7/10)*polomer)) + stred[0]
    y2 = (m.sin(uhol_rad) * ((7/10)*polomer))+ stred[1]
    c.create_line(stred[0],stred[1],x2,y2,tags="m_rucicka",width=2)
    
# vykreslenie hodinovej ručičky   
def h_rucicka(uhol):
    uhol_rad = m.radians(uhol)
    x2 = (m.cos(uhol_rad) * ((11/20)*polomer)) + stred[0]
    y2 = (m.sin(uhol_rad) * ((11/20)*polomer))+ stred[1]
    c.create_line(stred[0],stred[1],x2,y2,tags="h_rucicka",width=4) 
    
# funkcia na ukončenie programu po stlačení klávesy q 
def koniec(s):
    global hodiny   
    hodiny = False  
    c.delete("all")
    c.after(10) 
    quit()  
    
# vyzobrazenie čísel okolo hodín 
for i2 in range(12):
    cisla(uhol_zac_cisla)
    uhol_zac_cisla += 30

c.bind_all("<q>", koniec ) # <q> ako quit

while hodiny == True: 
    if hodiny == True:
        s_rucicka(s_uhol_rucicka)
        m_rucicka(m_uhol_rucicka)
        h_rucicka(h_uhol_rucicka)
        c.update()
        s_uhol_rucicka += 6
        m_uhol_rucicka += 0.1
        h_uhol_rucicka += 0.5/60
        c.after(1000)
        delete_rucicka() 
    else:
        hodiny = False

c.mainloop()    
