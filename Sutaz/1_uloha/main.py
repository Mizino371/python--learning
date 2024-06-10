import tkinter as t
from random import *
c=t.Canvas(width=500,height=200)
x_center = 250
y_center = 100

c.pack()
medz=0
posun = 5
r_zaciatok = randint(100,200)
r_dlzka_c = randint(80,200)

for i in range(6):
    posun += randint(1,3)
    c.create_line(x_center-r_zaciatok+medz,(r_dlzka_c/2)+y_center,x_center-r_zaciatok+medz,(r_dlzka_c/2)-y_center )
    c.create_line(x_center+r_zaciatok-medz,(r_dlzka_c/2)+y_center,x_center+r_zaciatok-medz,(r_dlzka_c/2)-y_center )
    medz += posun
    


c.mainloop()