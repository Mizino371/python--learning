from turtle import *
from random import *

def stvorec(dlzka_stvor):
    for i in range(4):
     fd(dlzka_stvor)
     left(90)
    fd(dlzka_stvor)

def stvorec7():
    dlzka = 10
    for k in range(7):
        stvorec(k*10+dlzka)

stvorec7()

mainloop()