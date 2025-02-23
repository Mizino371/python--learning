import tkinter, random as r,math as m

sirka_platna = 800
c=tkinter.Canvas(width=800,height=500,bg="light blue")
c.pack()
def delete_all():
    c.delete("all")

def obdlznik():
    for i in range(50000):
        r_x = r.randint(0,sirka_platna)
        r_y = r.randint(0,500)
        if r_x <= 400 and r_y <= 250:
            color = "red"
        elif 400<r_x<= 800 and r_y <= 250  :
            color = "green"
        elif r_x > 400 and r_y > 250:
            color = "blue"
        elif r_x <400 and r_y >= 250:
            color = "yellow"

        c.create_oval(r_x-5,r_y-5,r_x+5,r_y+5,fill=color)

def kruh():
    for i in range(5000):
        r_x = r.randint(150,650)
        r_y = r.randint(0,500)
        s_od_stredu = m.sqrt((400-r_x)**2+(250-r_y)**2)
        if s_od_stredu <= 50:
            color_kruh = "red"
        elif s_od_stredu > 50 and s_od_stredu <= 100:
            color_kruh = "green"
        elif s_od_stredu > 100 and s_od_stredu <= 150:
            color_kruh = "yellow"
        elif s_od_stredu > 150 :
            color_kruh = "blue"
        c.create_oval(r_x-5,r_y-5,r_x+5,r_y+5,fill=color_kruh)


button1 =  tkinter.Button(text = "OBLZNIK",command=obdlznik)
button_del = tkinter.Button(text="ZMAZ",command=delete_all)
button_kruh = tkinter.Button(text="KRUH",command=kruh)
button_kruh.pack()
button_del.pack()
button1.pack()
c.mainloop()
