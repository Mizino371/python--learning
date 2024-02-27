import tkinter
import math 

c  = tkinter.Canvas(height=700,width  = 1000)
c.pack()

c.create_oval(100,100,300,300)
c.create_oval(100,400,300,600)

c.create_line(200,100,200,300)
c.create_line(100,200,300,200)

c.create_line(200,400,200,600)
c.create_line(100,500,300,500)

c.create_line(400,200,900,200)
c.create_line(500,100,500,300)

c.create_line(400,500,900,500)
c.create_line(500,400,500,600)
A = math.radians(0)
a = 1
b = 1
B = math.radians(0)

def start():
    for i in range(360):
        
        
        sinus()
        kosinus() 
        c.after(10)
        c.update()
            
def sinus():
    global A,a
    r = 100
    c.delete('k')
    c.create_line(200,200,200+r*math.cos(A),200-r*math.sin(A),tags = 'k',fill='black',width = 4)
    c.create_line(200,200,200,200-r*math.sin(A),fill ='green',tags='k',width= 4)
    c.create_line(200-0.0001*r*math.cos(A),200-r*math.sin(A),200+r*math.cos(A),200-r*math.sin(A),tags = 'k',width = 4)

    c.create_rectangle(500+a,200,501+a,200-r*math.sin(A),fill='green',outline='green')
    a = a+1
    A = A + math.radians(1)
   
def kosinus():
    global B,b
    r = 100
    c.delete('ki')
    c.create_line(200,500,200+r*math.cos(B),500-r*math.sin(B),tags = 'ki')
    c.create_line(200,500,200+r*math.cos(B),500,tags='ki',fill='red',width = 4)
    c.create_line(200+r*math.cos(B),500-r*math.sin(B),200+r*math.cos(A),500,tags = 'ki')
    
    c.create_rectangle(500+b,500,501+b,500-r*math.cos(B),outline='red',fill='red')
    b = b+1
    B = B + math.radians(1)
    
start()
print(A)
c.mainloop()



