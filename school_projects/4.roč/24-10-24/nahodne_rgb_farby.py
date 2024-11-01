# import tkinter, random
# c=tkinter.Canvas(width=600, height=600)
# c.pack()
# r = random.randint(0,255)
# g = random.randint(0,255)
# b = random.randint(0,255)

# print("# {:02x}{:02x}{:02x}".format(r,g,b))
# for i in range(3):
#     c.create_rectangle(20+10*i,20+10*i,40+10*i,40+10*i,fill="#{:02x}{:02x}{:02x}".format(r,g,b))




import tkinter
c= tkinter.Canvas(width=256,height=200)
c.pack()

for i in range(256):
    r = 0
    g = 0
    b = 0+i
    c.create_line(0+i,0,0+i,200,fill="#{:02x}{:02x}{:02x}".format(r,g,b))

c.mainloop()