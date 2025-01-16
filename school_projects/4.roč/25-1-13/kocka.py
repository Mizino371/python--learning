import tkinter
c = tkinter.Canvas(width=610,height=150)
c.pack()
strany_kocky_z = []

for i in range(6):
    strany_kocky_z.append(tkinter.PhotoImage(file =f"4.roč/25-1-13/fotka_kocky/kocka_{i+1}.png"))

x = 50
for i2 in range(6):     
    c.create_image(x,75,image =strany_kocky_z[i2])
    x += 102
    
c.mainloop()
