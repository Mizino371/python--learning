import tkinter 
vstupny_obrazok = open("4.roč/zimne-prazdniny/obrazok.txt","r")
n_o = True
for riadok in vstupny_obrazok:
    suradnice = riadok.strip().split(" ")
    if suradnice[0] =="r":
        sur_r = list(suradnice[1:5])

    elif suradnice[0] =="o" and n_o is True:
        sur_oval1 = list(suradnice[1:5])
        n_o = False
        
    elif suradnice[0] =="o" and n_o is not True:
        sur_oval2 = list(suradnice[1:5])
         
    elif suradnice[0] =="l":
        sur_line = list(suradnice[1:5])

vstupny_obrazok.close()

c=tkinter.Canvas(width=400,height=400)
c.pack()
sur_oval1.append("red")
sur_oval2.append("red")
sur_r.append("blue")

c.create_oval(sur_oval1[0],sur_oval1[1],sur_oval1[2],sur_oval1[3],fill=sur_oval1[4])
c.create_oval(sur_oval2[0],sur_oval2[1],sur_oval2[2],sur_oval2[3],fill=sur_oval2[4])
c.create_rectangle(sur_r[0],sur_r[1],sur_r[2],sur_r[3],fill=sur_r[4])
c.create_line(sur_line[0],sur_line[1],sur_line[2],sur_line[3])
c.mainloop()
