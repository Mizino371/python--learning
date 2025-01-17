import tkinter, random as r 
sirka_p = 600
vyska_p = 400
c = tkinter.Canvas(width=sirka_p,height=vyska_p)
c.pack()
strany_kocky_z = []

for i in range(6):
    strany_kocky_z.append(tkinter.PhotoImage(file =f"4.roč/25-1-13/fotka_kocky/kocka_{i+1}.png"))

def vymaž_všetko():
    c.delete("all")

def vyhodnotenie():
    if hod_kociek[0] == hod_kociek[1] ==hod_kociek[2]:
        c.create_text(sirka_p/2,vyska_p/2,text="Bingo",fill = "Blue")

def hod_3_kockami():
    global hod_kociek
    x = (sirka_p/2) - 102
    hod_kociek = 3* [0]
    for i2 in range(3):
        nahodne_cisla = r.randrange(3)
        c.create_image(x,(vyska_p/2)-(vyska_p/6),image =strany_kocky_z[nahodne_cisla])
        x += 102
        hod_kociek[i2] += (nahodne_cisla+1)
    vyhodnotenie()
    c.update()
    c.after(1000,vymaž_všetko())
    
        
but_generuj = tkinter.Button(text="Hod kockou", command=hod_3_kockami)       
but_generuj.pack()

 
c.mainloop()
