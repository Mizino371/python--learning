import tkinter,random
from tkinter import PhotoImage
c= tkinter.Canvas(width=2000,height=560)
c.pack()

def nakresli_fotky():
    global vyber_zviera_img
    vyber_zvery_int = random.randint(0,4)
    vyber_zviera_img =PhotoImage(file=f"school_projects/kružok/2023ulohy/2. uloha/zvierata+stopy/zviera{vyber_zvery_int}.png")
    for i in range(5):
        vyber_nespr_zver_img = PhotoImage(file=f"school_projects/kružok/2023ulohy/2. uloha/zvierata+stopy/zviera{i}.png")
        # c.create_image(i*50+200,200,anchor = tkinter.CENTER,image = vyber_zviera_img, tags = "spravne zviera")

c.create_image(200,200,image = PhotoImage(file="school_projects/kružok/2023ulohy/2. uloha/zvierata+stopy/zviera0.png"))
    
    
    
nakresli_fotky()

# c.create_image(200,200,anchor = tkinter.CENTER,image = vyber_zviera_img, tags = "spravne zviera")

c.mainloop()