import random as r 
import tkinter
c = tkinter.Canvas(width=1040,height=500)
c.pack()
cislice = 10*[0]
n = int(input("Zadaj počet opakovaní: "))
for i in range(n):
    r_cifra = r.randint(0,9)
    cislice[r_cifra] +=1

zac_x = 40

for i2 in range(10):
    priemer = round((cislice[i2]/ n) *100,2)
    print(f"Priemerný výskyt čísla {i2} je {priemer}%")
    horne_y = 100+((100-priemer)*4)
    c.create_rectangle(zac_x,500,zac_x+60,horne_y,fill="blue")
    c.create_text(zac_x+30,490,text=i2,fill="yellow")
    c.create_text(zac_x+30,horne_y-10,text=f"{priemer}%")
    zac_x += 100
# X= 60 hrubka 
# X = 40 volne

c.mainloop()
