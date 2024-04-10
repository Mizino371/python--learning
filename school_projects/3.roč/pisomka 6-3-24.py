import tkinter
canvas=tkinter.Canvas(width=1000,height =500, bg="white")
canvas.pack()


canvas.create_line(0,250,1000,250,width= 5,fill="black")

def klik_na_platno(suradnice):          #vytvoríš si skupinu nejakých príkazov ktoré možeš spustiť naraz
    x=suradnice.x                       # (suradnice) + dva riadky pod dáš stále ked chceš s myšou spustiť príkaz
    y=suradnice.y

    if (y<250):                # vytvorí podmienku že ak poloha myši Y je menšie ako 250 tak nakreslí text v hornom poli červenou farbou 
                               # a ak väčšie, tak vykreslí text v dolnom poli modrou.
        canvas.create_text(x,y,text="Python", fill= "red", angle= x*-1) #angle nieje 
                                                                        #dôležitý ani pri jendom
    elif(y>250):
        canvas.create_text(x,y,text="Python", fill= "blue", angle= x*-1)
    

def stvorceky(suradnice):       #vytvoríš si skupinu nejakých príkazov ktoré možeš spustiť naraz
    x=suradnice.x               # znova tie isté veci na začiatok 
    y=suradnice.y

    for i in range(10):             #opakovanie 10 krát - 
        canvas.create_rectangle(x,y,x+15,y+15,fill="black")
        x = x+20  # ak chceš posúvať tú vytvorenú kocku, tak posúvaš bod z ktorého sa za každý vytvrí kocka.
                  # prvá kocka sa ti spraví od suradnice [0,10] druhá kocka od sáradnie [20,10] stále len x sa ti zväčšuje o 20 

    


canvas.bind("<Button-3>",stvorceky)     # už len vytvorenie príkazu na tlačidlá (tlačidlo na myši, skupina príkazov napr. klika_na_platno/stvorceky)
canvas.bind("<Button-1>",klik_na_platno)

canvas.mainloop()