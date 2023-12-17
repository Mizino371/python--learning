import turtle as t
import random as r


y=70

t.forward(sirka)
t.left(90)
t.forward(270)
t.left(90)
t.forward(sirka)
t.left(90)
t.forward(270)

def troj(strana):
    t.left(150)
    t.forward(strana)
    t.right(120)
    t.forward(strana)
    t.right(30)

for i in range(22):
    if t.xcor() <=sirka-80:
        dlzka_strany_troj=r.randint(20,80)
        troj(dlzka_strany_troj)
    elif t.xcor() > sirka-80:
        dlzka_strany_troj = sirka - t.xcor()
        troj(dlzka_strany_troj)
        break



t.mainloop()
