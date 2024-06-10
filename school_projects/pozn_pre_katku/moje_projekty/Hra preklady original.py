import tkinter as tk 
import random

c = tk.Canvas(width=600, height=600)
c.pack()

Preklady = {
    "boyfrend": "priateľ",
    "discover":"objaviť",
    "Ouch!":"Au!",
    "ancient":"staroveký",
    "backpacker":"turista s batohom",
    "bike ride":"jazda na bicykli",
    "blog":"blog",
    "brilliant":"skvelý",
    "charity":"charita",
    "diarrhoea":"hnačka",
    "emperor":"vládca, cisár",
    "engineering":"technika,strojárstvo",
    "explorer":"objaviteľ",
    "extenssively":"extenzívne, veľmi veľa",
    "fantastic":"fantastický",
    "fortune":"bohatstvo",
    "gold":"zlato",
    "history":"dejiny",
    "hostel":"hostel",
    "jewellery":"šperk, šperky",
    "journey":"cesta",
    "merchant":"obchodník",
    "mug":"prepadnúť a okradnúť (niekoho)",
    "novel":"román",
    "overland": "po súši",
    "party":"chodiť po zábavach"
    
}

count_En = 0
count_Sk = 0

bodiky = 0

def hra():
    global count_En,count_Sk,entry,bodiky
    
    
    
    current_En,current_Sk = random.choice(list(Preklady.items()))
    r_cislo = random.randrange(0,200)
    if r_cislo<=100:
        c.create_text(300,200,text=f"Prelož: {current_En}")
        count_En +=1 
        if count_En >5:
            c.create_text(300,200,text=f"Prelož: {current_Sk}")
            count_En =0

    else: 
        c.create_text(300,200,text=f"Prelož: {current_Sk}")
        count_Sk +=1
        if count_Sk >5:
            c.create_text(300,200,text=f"Prelož: {current_En}")
            count_Sk =0        

    
    if current_En or current_Sk == entry:
        bodiky += 1
        #c.after(1000,hra)
    else: 
        c.create_text(300,500,text="Zle", tags="zla odpoved")
        c.delete(500,"zla odpoved")   
        #c.after(2000,hra)    
entry = tk.Entry()
entry.pack()



hra()
c.mainloop()