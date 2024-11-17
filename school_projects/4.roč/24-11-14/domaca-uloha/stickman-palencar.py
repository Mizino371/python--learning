import tkinter
stickman = tkinter.Canvas(width=500,height=500,bg="white")
stickman.pack()
subor = open("4.roč/24-11-14/domaca-uloha/stickman.txt", "r")

riadok = subor.readline()

pocet_opak = 0
while riadok != "":
    n_riadok = 0
    for i in range(4):      #dalo sa obidvoma spôsobmi
    # while n_riadok < 4:
        if n_riadok <1:
            x1 = int(riadok)
        elif n_riadok <2:
            y1 = int(riadok)
        elif n_riadok <3:
            x2 = int(riadok)
        elif n_riadok <4:
            y2 = int(riadok)
        n_riadok += 1
        riadok = subor.readline() 
    
    if pocet_opak != 0:
        stickman.create_line(x1,y1,x2,y2, fill="black",width=3)
    else:
        stickman.create_oval(x1,y1,x2,y2, outline="black",width=3)
    pocet_opak +=1
subor.close()
stickman.mainloop()
    
    
        

        