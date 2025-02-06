# 8 cif. čislo bez 0
#číslica = hrubka čiary
import tkinter, random as r 
c=tkinter.Canvas(width=500,height=500)
c.pack()
posun_y = 80
zac_x = 100

def bar(cifra,opakovnaie):
    if opakovnaie == 0 or opakovnaie == 7:
        c.create_line(zac_x,230,zac_x,200-posun_y,width=cifra)  
    else:
        c.create_line(zac_x,200,zac_x,200-posun_y,width=cifra)
    c.create_text(110+(6*opakovnaie),215,text=str(cifra))
    print(cifra,end="")
    
print("EAN kód je: ",end="")   
for i in range(8):
    r_cifra = r.randint(0,9)
    bar(r_cifra,i)
    zac_x +=10
    
c.mainloop()