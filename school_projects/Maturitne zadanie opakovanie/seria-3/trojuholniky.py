import tkinter, math as m
c=tkinter.Canvas(width=500,height=500,bg="white")
c.pack()
stred = 250
entry1 = tkinter.Entry()
entry1.pack()
def delete():
    c.delete("all")
def p_trojuholnik(dlzka_a,dlzka_b):
    dlzka_c = m.sqrt(dlzka_a**2 + dlzka_b**2)
    c.create_line(stred,stred,stred,stred-dlzka_a,fill="red")
    c.create_text(stred -25,stred-(dlzka_a/2),text=f"a = {dlzka_a}",fill="red")
    c.create_line(stred,stred,stred+dlzka_b,stred,fill="red")
    c.create_text(stred + (dlzka_b / 2),stred +10 , text=f"b = {dlzka_b}",fill="red")
    c.create_line(stred,stred-dlzka_a,stred+dlzka_b,stred,fill="red")
    c.create_text(stred+ (dlzka_b/2)+15,stred - (dlzka_a/2)-15, text=f"c = {round(dlzka_c,2)}",fill="red")

def pusti_program():
    delete()
    entry1_str = entry1.get()
    entry1_str.strip()
    entry1_str = entry1_str.split(",")
    if 250 < int(entry1_str[0]) < 0 or 250 < int(entry1_str[1]) < 0:
        c.create_text(250,490,text="Zadaj čísla (a,b) menšie ako 250 a nie 0")
    else:
        p_trojuholnik(int(entry1_str[0]),int(entry1_str[1]))

button = tkinter.Button(text="Pusti program",command=pusti_program)
button.pack()
c.mainloop()