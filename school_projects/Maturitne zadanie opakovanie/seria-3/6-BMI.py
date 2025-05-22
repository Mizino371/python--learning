#(m)/(vyska**2) =
import tkinter
c=tkinter.Canvas(width=600, height=500)
c.pack()
entry_hmotnost = tkinter.Entry(bg="red")
entry_hmotnost.pack()
entry_vyska = tkinter.Entry(bg="green")
entry_vyska.pack()


def vypocet_BMI() -> None:
    c.delete("all")
    hmotnost = float(entry_hmotnost.get())
    vyska = float(entry_vyska.get())
    BMi = round(hmotnost/(vyska**2),2)
    if 1< BMi< 18.5:
        c.create_text(300,250,text=f"BMI: {BMi} – Podváha")
    elif 18.5<= BMi < 25:
        c.create_text(300, 250, text=f"BMI: {BMi} – Normálna hmotnosť")
    elif 25<= BMi < 30:
        c.create_text(300, 250, text=f"BMI: {BMi} – Nadváha")
    elif BMi >= 30:
        c.create_text(300, 250, text=f"BMI: {BMi} – Obezita")
    else:
        print("zle zadaná hodnota")
    c.update()

button = tkinter.Button(text="Vypocet BMI", command=vypocet_BMI)
button.pack()
c.mainloop()