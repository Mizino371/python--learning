import tkinter

subor = open("/Users/m1promichalpalencar/Desktop/python--learning/school_projects/Maturitne zadanie opakovanie/seria-5/zakodovany_obrazok.txt","r")
p_riadkov = 0
strana = int(input("Zadaj stranu stvorca: "))
y = 1
one = 0
for riadok in subor:
    p_riadkov +=1
    riadok = riadok.strip().split(" ")
    if p_riadkov != 1:
        x = 1
        for i in riadok:
            if i == "1":
                color = "black"
                one +=1
            else:
                color = "white"
            c.create_rectangle(x-(strana/2),y-(strana/2),x+(strana/2),y+(strana/2),fill=color)
            x += strana
        y+=strana
    else:
        velkost_obrazku = int(riadok[0]) * int(riadok[1])
        print(f"Velkost obrazku je {velkost_obrazku}px.")
        c= tkinter.Canvas(width=int(riadok[0])*strana,height=int(riadok[1])*strana,bg="white")
        c.pack()

print(f"Na obrázku je {one} jednotiek.")
c.mainloop()

