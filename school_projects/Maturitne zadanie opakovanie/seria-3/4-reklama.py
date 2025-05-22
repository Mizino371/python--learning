import tkinter, random as r
c=tkinter.Canvas(width=500,height=500)
c.pack()

def delete_all():
    end = True
    c.delete("all")


def nadpis():
    nadpis = entry.get()
    delete_all()
    for i in range(len(nadpis)):
        farba = r.choice(("blue", "red", "green", "yellow", "purple"))
        c.create_text(100+(i*30),250,text =nadpis[i],fill=farba,font=  "Arial 30")
    c.update()
    c.after(1000)

def run():
    nadpis()
    c.update()
    c.after(1000)
    delete_all()


def stop():
    delete_all()
    exit()


entry = tkinter.Entry()
entry.pack()

button = tkinter.Button(text = "OK" ,command=run)
button.pack()

# button_end = tkinter.Button(text = "KONIEC" ,command=stop)
# button_end.pack()

c.mainloop()