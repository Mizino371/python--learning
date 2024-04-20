import tkinter as t
import random as r
c=t.Canvas(width=500,height=500,background="white")
c.pack()



def show_text():
    global r_num
    r_num=r.randint(10000,100000)
    c.create_text(250,250, text=r_num, fill="black",tags="text")

def del_txt():
    c.delete("text")


def program():
    show_text()
    c.after(1000,del_txt)
    inp_answ = int(input("Aké je moje číslo? "))
    if inp_answ == r_num:
        c.create_text(250,250, text="SUPER", fill="black")
    elif inp_answ != r_num:
        c.create_text(250,250, text=f"Dačo nedobre, číslo bolo: {r_num}", fill="black")        
program()

c.mainloop()

