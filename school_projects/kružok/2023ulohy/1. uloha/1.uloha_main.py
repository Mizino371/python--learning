import random,math,turtle 
t = turtle
x=random.randint(-350,300)          #-350<=x<=300
y = random.randint(100,200)         #100<=y<=220

def obdlznik(a,b):
    for i in range(2):
        t.right(90)
        t.forward(a)
        t.right(90)
        t.forward(b)
    

def slnko(n,strana,luc):                # n  = počet stran/ vrcholov    
    x = random.randint(-350,300)        # -350<=x<=300
    y = random.randint(100,200)         # 100<=y<=220                          
    angle_of_attack = 360 /n
    t.penup()                           # strana = dlzka stran   
    t.goto(x,y)
    t.pendown()
    for i in range(n):
        t.left(angle_of_attack)
        t.forward(strana)
        obdlznik(luc,strana)
                                        # luc = dlžka luca 
                                    # ((n-2)*180)/n ;  5<=n<=1
slnko(5,15,50)
t.mainloop()