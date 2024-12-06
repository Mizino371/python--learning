import math, tkinter, random as r 
c = tkinter.Canvas(width=500,height=500)
c.pack()
stred_kruhu = 250,250
polomer = 100
c.create_oval(stred_kruhu[0]-polomer,stred_kruhu[1]-polomer,stred_kruhu[0]+polomer,stred_kruhu[1]+polomer)

def gulicka(r_x,r_y):
    dist_f_mid = math.sqrt((r_x-stred_kruhu[0])**2 + (r_y-stred_kruhu[1])**2)
    if  (dist_f_mid >polomer-100 and dist_f_mid < polomer-50) or (dist_f_mid >polomer and dist_f_mid <polomer+50) or (dist_f_mid >polomer+100 and dist_f_mid < polomer+150):
        farba = ("red")
    else:
        farba = ("white")
    c.create_oval(r_x-7,r_y-7,r_x+7,r_y+7,fill=farba)     

for i in range(10000):
    random_x = r.randint(10,490)
    random_y = r.randint(10,490)
    gulicka(random_x,random_y)
  
c.mainloop()