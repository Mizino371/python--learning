import tkinter
c=tkinter.Canvas(width=850,height=500)
c.pack()
farby = ["green","red","blue","orange"]

for i in range(4):
    c.create_rectangle(0+(200*i)+20,150,210+(200*i),350,fill=farby[i],tags=f"jedlo{i}")
vyber = open("/Users/m1promichalpalencar/Desktop/python--learning/school_projects/Maturitne zadanie opakovanie/seria-5/vyber_jedla.txt","w")
vyber.write("Dnešny deň:\n")
vyber.close()
def zisti_jedlo(event):
    vyber_jedla = open(
        "/Users/m1promichalpalencar/Desktop/python--learning/school_projects/Maturitne zadanie opakovanie/seria-5/vyber_jedla.txt",
        "a")
    kod_ziaka = int(vstup.get().strip())
    print(kod_ziaka)
    jedlo = 0
    if 0< kod_ziaka < 999:
        if 150< event.y < 350:
            if 20< event.x< 210:
                jedlo = "z"
            elif 220< event.x< 410:
                jedlo = "c"
            elif 420< event.x< 620:
                jedlo = "m"
            elif 620< event.x< 820:
                jedlo = "o"
            else:
                print("Klikni na jedlo ktoré chceš")
            if jedlo != 0:
                vstup.delete(0,tkinter.END)
                vyber_jedla.write(f"{kod_ziaka} {jedlo}\n")
    else:
        print("Zadajte kod ziaka")


c.bind("<Button-1>",zisti_jedlo)

label_student = tkinter.Label(text="Zadajte kód žiaka")
label_student.pack()

vstup = tkinter.Entry()
vstup.pack()

c.mainloop()