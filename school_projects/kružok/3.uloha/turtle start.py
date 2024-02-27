import turtle as t
import random as r

class KlreslenieTrojuholnika:
    def __init__(self):
        self.y=0
        self.sirka = r.randint(100,400)

    def podklad(self):
        for i in range(4):
            t.goto(0,self.y)
            for i in range(2):
                t.forward(self.sirka)
                t.left(90)
                t.forward(70)
                t.left(90)
            self.y +=70
        t.goto(0,0)       
        t.seth(270)

    def troj(self,strana):
        t.left(150)
        t.forward(strana)
        t.right(120)
        t.forward(strana)
        t.right(30)


    def logika(self):
        self.y = 0
        for i in range(4):
            for i in range(22):
                if t.xcor() <=self.sirka-80:
                    dlzka_strany_troj=r.randint(20,80)
                    self.troj(dlzka_strany_troj)
                elif t.xcor() > self.sirka-80:
                    dlzka_strany_troj = self.sirka - t.xcor()
                    self.troj(dlzka_strany_troj)
                    break

            self.y += 70
            if self.y<280:
                t.penup()
                t.goto(0,self.y)
                t.pendown()
            else:
                break

if __name__ == "__main__":
    kreslenie = KlreslenieTrojuholnika()
    kreslenie.podklad()
    kreslenie.logika()
    t.mainloop()
