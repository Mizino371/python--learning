import random,math, tkinter as tk 
c=tk.Canvas()
c.pack()
x=random.randint(-350,300)          #-350<=x<=300
y = random.randint(100,200)         #100<=y<=220

def slnko(n,strana,luc):        # n  = počet stran/ vrcholov    strana = dlzka stran   luc = dlžka luca 
    c.create_polygon()                  #((n-2)*180)/n ;  5<=n<=15

    
def obdlznik(a,b):
    c.create_rectangle(x,y,x+a,y+b)
    
# slnko(random.randint(5,15),random.randint(9,20),obdlznik)

