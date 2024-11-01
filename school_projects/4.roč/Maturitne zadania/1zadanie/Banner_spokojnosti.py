import tkinter
c= tkinter.Canvas(width=500,height=350,bg=("#005ED9"))
c.pack()
subor = open("Maturitne zadania/1zadanie/štatistika.txt","w")
subor.close()

def tabulka_spokojnosti():
    #"Head"
    c.create_text(250,150,text=" Boli ste spokojný \ns našími službami ?",font="Arial 35",fill="white")
    #tlačidla
        #áno
    c.create_rectangle(100,250,200,300,fill="white")
    c.create_text(150,275,text="Áno",font="Arial 30",fill="black")
        #nie
    c.create_rectangle(400,250,300,300,fill="white")
    c.create_text(350,275,text="Nie",font="Arial 30",fill="black")

def skontroluj_klik(suradnice):
    subor = open("Maturitne zadania/1zadanie/štatistika.txt","a")
    x=suradnice.x
    y=suradnice.y
    #áno
    if 100<x<200 and 250<y<300:
        print("OK")
        subor.write("1 "+"\n")
    #nie
    if 300<x<400 and 250<y<300:
       subor.write("0"+"\n")
      
    subor.close()
tabulka_spokojnosti()
    
c.bind("<Button-1>",skontroluj_klik)

c.mainloop()
