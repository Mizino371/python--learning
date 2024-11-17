def main():

    import tkinter
    c= tkinter.Canvas(width=1000,height=800,bg= "white")
    c.pack()


    subor = open("štatistika.txt","r")
    pocet_hodnoteni = 0
    dobre_hodnotenie = 0

    for riadok in subor:
        pocet_hodnoteni +=1
        if int(riadok) == 1 :   
            dobre_hodnotenie += 1
    subor.close()

    if pocet_hodnoteni == 0:
        c.create_text(500,400,text="Žiaden zákazník dnes nehodnotil služby",fill="black",font="Arial 50")
    else:
        #a)
        print(pocet_hodnoteni)
        
        percento_dobre = round((dobre_hodnotenie/pocet_hodnoteni) * 100,2)
        percento_zle = 100 - (percento_dobre)
        #c)
        print(f"dobré hodnotenie: {percento_dobre}%" )
        print(f"zle hodnotenie: {percento_zle}%" )
        vyska_podla_percent_d = percento_dobre *5
        vyska_podla_percent_n = percento_zle * 5 
        
        #b)
        #dobre hodnotenie
        c.create_rectangle(150,600,350,600-vyska_podla_percent_d,fill="#005ED9")
        c.create_text(250,570-vyska_podla_percent_d,text=f"{percento_dobre}%",fill="black",font="Arial 35")
        c.create_text(250,700,text="Dobré hodnotenie",fill="black",font="Arial 35")
        
        #zle hodnotenie
        c.create_rectangle(650,600,850,600-vyska_podla_percent_n,fill="red")
        c.create_text(750,570-vyska_podla_percent_n,text=f"{percento_zle}%",fill="black",font="Arial 35")
        c.create_text(750,700,text="Zlé hodnotenie",fill="black",font="Arial 35")

        c.mainloop()
        
