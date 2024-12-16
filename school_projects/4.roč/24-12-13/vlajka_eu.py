import tkinter
import math as m
c= tkinter.Canvas(width=600,height=400,bg="blue")
c.pack()
stred = 300,200
polomer = 100
hviezda_obr = tkinter.PhotoImage(file= "4.roč/24-12-13/hviezda.png")
zac_uhol = 0
def hviezda(uhol):
    uhol_r = m.radians(uhol)
    x = (m.cos(uhol_r) * (polomer )) + stred[0]
    y =  (m.sin(uhol_r) * (polomer ))+ stred[1]
    c.create_image(x,y,image =hviezda_obr)
    
    
for i in range(12):
    hviezda(zac_uhol)
    zac_uhol += 30
    
c.mainloop()