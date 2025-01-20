import tkinter
c=tkinter.Canvas(width=1000,height=600,background="white")
c.pack()
data = {
    "pocasie": ["jasno","polojasno","polooblacno","oblacno","dazd","snezenie","burka","slovakia"]
        }
index_pocasia = [0]
data["Obrazky"] = [
    tkinter.PhotoImage(file=f"4.roč/25-1-16/obrazky/{pocasie}.png")
    for pocasie in data["pocasie"]
                    ]   

c.create_image(500,260,image= data["Obrazky"][7])
c.create_text(850,560,text="1. Napíš do okienka dolnú hranicu teploty\n2. Vyber si počasie pomocou kliknutia",fill= "Black")

def pocasie_na_vyber():
    x = 50
    for i in range(7):
        tag = str(data["pocasie"][i].strip())
        c.create_image(x,560,image = data["Obrazky"][i], tags = (tag,"image"))
        x+= 100
    c.tag_bind("image", "<Button-1>", klikacka)


def klikacka(sur):
    clicked_tag = c.gettags("current")
    if str(clicked_tag[0]) in data["pocasie"]  :
        index_pocasia[0]= data["pocasie"].index(str(clicked_tag[0]))
    if sur.y < 520:
        teplota_nizsia = entry.get().strip()
        c.create_image(sur.x, sur.y,image = data["Obrazky"][index_pocasia[0]])
        c.create_text(sur.x,sur.y+45,text=f"{teplota_nizsia}/{int(teplota_nizsia)+4}", font="Arial 20 ")
        c.update()
    print(index_pocasia)
   
            
c.bind("<Button-1>",klikacka)
pocasie_na_vyber()

entry = tkinter.Entry()
entry.pack()

c.mainloop()