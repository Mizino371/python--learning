import tkinter, math as m 
c= tkinter.Canvas(width=500,height=500)
c.pack()

stred = 250,250
polomer = 100
s_uhol_rucicka = -90
uhol_zac_cisla = -90
m_uhol_rucicka = -90
h_uhol_rucicka = -90
c.create_oval(stred[0]-polomer, stred[1]-polomer, stred[0]+polomer,stred[1]+polomer,width=3)

def cisla(uhol):
    uhol_r = m.radians(uhol)
    x = (m.cos(uhol_r) * (polomer + 15)) + stred[0]
    y =  (m.sin(uhol_r) * (polomer + 15))+ stred[1]
    if i2 == 0:
        c.create_text(x,y,text="12")
    else:
        c.create_text(x,y,text=f"{i2}")


def delete_rucicka():
    c.delete("s_rucicka")
    c.delete("m_rucicka")
    c.delete("h_rucicka")
    
def s_rucicka(uhol):
    uhol_rad = m.radians(uhol)
    x2 = (m.cos(uhol_rad) * (polomer-15)) + stred[0]
    y2 =  (m.sin(uhol_rad) * (polomer-15))+ stred[1]
    
    c.create_line(stred[0],stred[1],x2,y2,tags="s_rucicka") 

def m_rucicka(uhol):
    uhol_rad = m.radians(uhol)
    x2 = (m.cos(uhol_rad) * (polomer-30)) + stred[0]
    y2 =  (m.sin(uhol_rad) * (polomer-30))+ stred[1]
    c.create_line(stred[0],stred[1],x2,y2,tags="m_rucicka",width=2) 

def h_rucicka(uhol):
    uhol_rad = m.radians(uhol)
    x2 = (m.cos(uhol_rad) * (polomer-45)) + stred[0]
    y2 =  (m.sin(uhol_rad) * (polomer-45))+ stred[1]
    c.create_line(stred[0],stred[1],x2,y2,tags="h_rucicka",width=3) 
  
for i2 in range(12):
    cisla(uhol_zac_cisla)
    uhol_zac_cisla += 30
    
for i5 in range(24):    # 24 hodín
    for i3 in range(60):    # 60 minút
        for i4 in range(60):    # 60 sekúnd
            s_rucicka(s_uhol_rucicka)
            m_rucicka(m_uhol_rucicka)
            h_rucicka(h_uhol_rucicka)
            c.update()
            s_uhol_rucicka +=6
            m_uhol_rucicka +=0.1
            h_uhol_rucicka += 0.5/60
            c.after(10)
            delete_rucicka()

c.mainloop()