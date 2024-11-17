import tkinter
c=tkinter.Canvas(width=400,height=430)
c.pack()

subor = open("4.roč/24-11-8/text.txt", "r")
y_textu = 50
def vypisanie_riadku(c_riadku):
    global y_textu
    c.create_text(200,y_textu,text=f"{c_riadku}" )
    y_textu +=30
for riadok in subor:
    c.after(1000,vypisanie_riadku(riadok))
    c.update()
    
    
    
    


c.mainloop()
