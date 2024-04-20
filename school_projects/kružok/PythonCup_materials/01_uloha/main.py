import turtle as t

def stvorec(d):
    for i in range(4):
        t.fd(d)
        t.rt(90)
        
def trojuh(strana):
    for i in range(3):
        t.fd(strana)
        t.lt(120)

def dom(velkost):
    stvorec(velkost)
    trojuh(velkost)
    pass

def domy9():
    for i in range(9):
        dom(30)
        t.penup()
        t.forward(40)
        t.pendown()
    pass

t.speed(2)

domy9()

t.mainloop()