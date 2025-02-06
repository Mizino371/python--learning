import tkinter, random as r 

sirka_platna = 500
c=tkinter.Canvas(width=500,height=sirka_platna,bg="light blue")
c.pack()

def steblo_travy(dlzka_stebla,n_steblo):
    if dlzka_stebla < 20:
       farba = "Yellow"
    elif 20<=dlzka_stebla <=50:
        farba = "Green"
    c.create_line(n_steblo,500,n_steblo,500-dlzka_stebla,fill=farba)
    
for i in range(sirka_platna):
    r_stebiel = r.randint(3,50)
    steblo_travy(r_stebiel,i)
 
for i in range(100):
    r_farba = r.choice(("blue", "yellow", "red","purple", "green", "light blue", "dark red"))
    r_x = r.randint(-100,100)
    r_y = r.randint(-100,100)
    
    c.create_line(250,250,250+r_x,250+r_y,fill=r_farba)  

c.mainloop()