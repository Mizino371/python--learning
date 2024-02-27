import tkinter,random
from tkinter import PhotoImage
c= tkinter.Canvas(width=2000,height=560)
c.pack()


def fotky():
    nespr_zver_count = 0
    global zviera
    vyber_zviera = random.randint(0,4)
    zviera =PhotoImage(file=f"school_projects/kružok/2023ulohy/2. uloha/zvierata+stopy/zviera{vyber_zviera}.png", ) 
    stopy = PhotoImage(file=f"school_projects/kružok/2023ulohy/2. uloha/zvierata+stopy/stopy{vyber_zviera}.png", )
   
    for i in range (5):
        if i != vyber_zviera:
            nespr_zver_count += 1 
            nespravne_zviera_img = PhotoImage(file=f"school_projects/kružok/2023ulohy/2. uloha/zvierata+stopy/zviera{i}.png")
            c.create_image(100+nespr_zver_count*100,100,anchor= tkinter.CENTER,image= nespravne_zviera_img ,tags = "nespravne_zviera")

            print(f"pocet nespravnych zver: {nespr_zver_count}")
        elif i == vyber_zviera:
            c.create_image(100,100, anchor = tkinter.CENTER, image = zviera, tags="vyber_zviera")
            print(f"spravne zviera {i}")
            
            
fotky()
c.mainloop()


