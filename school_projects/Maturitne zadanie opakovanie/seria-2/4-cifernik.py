import tkinter , math as m 
c = tkinter.Canvas(width=500,height=500)
c.pack() 
stred = 250
uhol_zaciatocny = -90

def del_rucicka():
    c.delete("sekunda")

def cisla():
    uhl = -60
    for i in range(1,13):
        cisla_s_uhol_rad = m.radians(uhl)
        x = (m.cos(cisla_s_uhol_rad) * 90) + stred
        y = (m.sin(cisla_s_uhol_rad) * 90) + stred
        c.create_text(x,y,text= i)
        uhl += 30
        c.after(100)
        c.update()
        
def sekunda(start_uhol):
    for i in  range(60):
        del_rucicka()
        uhol_rad = m.radians(start_uhol)
        x_rucicka = (m.cos(uhol_rad) * 80) + stred
        y_rucicka = (m.sin(uhol_rad) * 80) + stred
        start_uhol += 6
        c.create_line(250,250,x_rucicka,y_rucicka,tags="sekunda")
        c.after(1000)
        c.update()
    
cisla()
sekunda(uhol_zaciatocny)
c.mainloop()