import tkinter
import random as r
c= tkinter.Canvas()
c.pack()


    
def button_funkcia():
    vstup = entry.get()
    x=50
    y = 100 
    
    for i in range(len(vstup)):
        
        farba_pisma = r.choice(("blue","red","yellow", "green","pink"))
        c.create_text(x,y,text=vstup[i],fill=farba_pisma,font=("Arial", 30),)
        x=x+30
        c.after(500)
        c.update()

      
entry = tkinter.Entry()
button = tkinter.Button(text = "OK", command =button_funkcia,)
entry.pack(side ="left")
button.pack(side ="left")


c.mainloop()

d = "PONDELOK" # string
print(d[3:6]) # DEL
print(d[3:])  # DELOK
print(d[:3])  # POND
print(d[2:7:2]) #NEO 
            