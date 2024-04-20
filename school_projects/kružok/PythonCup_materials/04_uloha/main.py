from turtle import *
from random import *

def kniha(sirka,vyska):
    for i in range(2):
        fd(sirka)
        rt(-90)
        fd(vyska)
        rt(-90)
    fd(sirka)
    pass        

def okraje ():
    for i in range(2):
        fd(15)
        rt(-90)
        fd(70)
        rt(-90)
    penup()
    fd(20)
    pendown()  
    pass

def knihy10 ():
    okraje()
    for i in range(10):
        r_sirka = randint(5,15)
        r_vyska = randint(30,45)
        kniha(r_sirka,r_vyska)
        if i ==9:
          kniha(r_sirka,r_vyska)
          fd(5)
          okraje()     
    
speed(5)
knihy10()
mainloop()