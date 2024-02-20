import tkinter as tk
c = tk.Canvas( width=400, height=300, bg='white')
c.pack()

   

  
   
   

def move_objects():
    tag_coords_auto = c.coords("auto")
    if 0<=tag_coords_auto[0]<=300:
        c.move('auto', 5, 0)
        c.move('bicykel', -5, 0)
    else: 
        c.move("auto",298,tag_coords_auto[1])
        
    

c.create_rectangle(100, 150, 200, 200, fill='blue', tags='auto')
c.create_oval(115, 200, 140, 225, fill='yellow', tags='auto')
c.create_oval(160, 200, 185, 225, fill='yellow', tags='auto')

c.create_oval(200, 100, 230, 130, fill='black', width=5, outline='black', tags='bicykel')
c.create_oval(250, 100, 280, 130, fill='black', width=5, outline='black', tags='bicykel')
c.create_line(215, 115, 230, 70, width=5,fill="black", tags='bicykel')
c.create_line(225, 90, 240,115,width=5,fill="black", tags='bicykel')
c.create_line(240,115,265, 115, width=5,fill="black", tags='bicykel')
c.create_line(265, 115, 270, 85, width=5,fill="black", tags='bicykel')

def loop():
    c.after(100,loop)
    c.after(100, move_objects) 
loop()
c.mainloop()
